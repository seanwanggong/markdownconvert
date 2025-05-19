from typing import Any, Dict, Generator
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from dify_plugin import ToolProvider
import markdown
import re
from weasyprint import HTML, CSS
import io
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

PDF_STYLE = "body { font-family: 'Helvetica Neue', Arial, sans-serif; color: #222; background: #fff; } h1,h2,h3 { color: #1976d2; }"

class MarkdownConverter:
    def __init__(self):
        self.md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables'])

    def to_html(self, markdown_text: str) -> str:
        return self.md.convert(markdown_text)

class MarkdownConvertPDFProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        pass  # No credentials needed

    def invoke(self, tool_parameters: dict) -> Dict[str, Any]:
        try:
            markdown_text = tool_parameters.get('markdown', '')
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
            pdf_io = io.BytesIO()
            HTML(string=html).write_pdf(pdf_io, stylesheets=[CSS(string=PDF_STYLE)])
            pdf_io.seek(0)
            return {
                "status": "success",
                "result": pdf_io.read(),
                "execution_metadata": {
                    "format": "pdf"
                }
            }
        except Exception as e:
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
