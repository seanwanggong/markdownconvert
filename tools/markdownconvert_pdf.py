from typing import Any, Dict, Generator
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from dify_plugin import ToolProvider
import markdown
import re
from weasyprint import HTML, CSS
import io
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import os

from fonts.style import DEFAULT_STYLE, TECH_BLUE_STYLE, BUSINESS_DARK_STYLE, PASTEL_STYLE, GRAND_STYLE

STYLE_MAP = {
    "default": DEFAULT_STYLE,
    "tech_blue": TECH_BLUE_STYLE,
    "business_dark": BUSINESS_DARK_STYLE,
    "pastel": PASTEL_STYLE,
    "grand": GRAND_STYLE,
}


class MarkdownConverter:
    def __init__(self):
        self.md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables'])

    def to_html(self, markdown_text: str) -> str:
        return self.md.convert(markdown_text)


class MarkdownConvertPDFProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        pass  # No credentials needed

    def invoke(self, tool_parameters: dict) -> Dict[str, Any]:
        from pygments.formatters import HtmlFormatter
        try:
            markdown_text = tool_parameters.get('markdown', '')
            style_key = tool_parameters.get('style', 'default')
            pygments_css = HtmlFormatter(style="default").get_style_defs('.codehilite')
            custom_style = STYLE_MAP.get(style_key, DEFAULT_STYLE)
            final_style = custom_style + "\n" + pygments_css
            if not markdown_text:
                return {
                    "status": "error",
                    "message": "markdown content is required",
                    "execution_metadata": {
                        "error": "Missing required parameter: markdown"
                    }
                }
            converter = MarkdownConverter()
            html = converter.to_html(markdown_text)
            full_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset=\"UTF-8\">
                <title>Markdown Converted Document</title>
                <style>
                    {final_style}
                </style>
            </head>
            <body>
                {html}
            </body>
            </html>
            """
            with open('test.html', 'w', encoding='utf-8') as f:
                f.write(full_html)
            pdf_io = io.BytesIO()
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            font_path = os.path.join(BASE_DIR, 'fonts', '方正兰亭黑简体.ttf')
            HTML(string=full_html, base_url=BASE_DIR).write_pdf(
                pdf_io,
                stylesheets=[CSS(string=final_style)]
            )
            print('[invoke] BASE_DIR:', BASE_DIR)
            print('[invoke] font_path:', font_path)
            print('[invoke] font exists:', os.path.exists(font_path))
            pdf_io.seek(0)
            return {
                "status": "success",
                "result": pdf_io.read(),
                "execution_metadata": {
                    "format": "pdf"
                }
            }
        except Exception as e:
            import traceback
            error_msg = str(e) + "\n" + traceback.format_exc()
            print('[invoke] Exception:', error_msg)
            with open('error.log', 'w', encoding='utf-8') as f:
                f.write(error_msg)
            return {
                "status": "error",
                "message": str(e),
                "execution_metadata": {
                    "error": str(e)
                }
            }


class MarkdownConvertPDFTool(Tool):
    def __init__(self, runtime=None, session=None):
        super().__init__(runtime=runtime, session=session)
        self.provider = MarkdownConvertPDFProvider()

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        result = self.provider.invoke(tool_parameters)
        if result.get("status") == "success":
            pdf_bytes = result["result"]
            yield ToolInvokeMessage(
                type=ToolInvokeMessage.MessageType.BLOB,
                message=ToolInvokeMessage.BlobMessage(blob=pdf_bytes),
                meta={
                    "mime_type": "application/pdf",
                    "filename": "markdown_converted.pdf"
                }
            )
        else:
            yield self.create_text_message(result.get("message", "Unknown error"))
