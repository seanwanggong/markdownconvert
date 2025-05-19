from typing import Any, Dict, Generator
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from dify_plugin import ToolProvider
import markdown
import re
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


class MarkdownConvertHtmlProvider(ToolProvider):
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

            return {
                "status": "success",
                "result": full_html,
                "execution_metadata": {
                    "format": "html"
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


class MarkdownConvertHtmlTool(Tool):
    def __init__(self, runtime=None, session=None):
        super().__init__(runtime=runtime, session=session)
        self.provider = MarkdownConvertHtmlProvider()

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        result = self.provider.invoke(tool_parameters)
        if result.get("status") == "success":
            yield ToolInvokeMessage(
                type=ToolInvokeMessage.MessageType.TEXT,
                message=ToolInvokeMessage.TextMessage(text=result["result"]),
                meta={
                    "mime_type": "text/html",
                    "filename": "markdown_converted.html"
                }
            )
        else:
            yield self.create_text_message(result.get("message", "Unknown error"))
