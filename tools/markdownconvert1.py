from typing import Any, Dict
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from dify_plugin import ToolProvider
import markdown
import re
from weasyprint import HTML, CSS
import io

PDF_STYLES = {
    "default": "",
    "modern": "body { font-family: 'Helvetica Neue', Arial, sans-serif; color: #222; background: #fff; } h1,h2,h3 { color: #1976d2; }",
    "classic": "body { font-family: 'Times New Roman', serif; color: #333; background: #fff; } h1,h2,h3 { color: #800000; }",
    "dark": "body { background: #222; color: #eee; font-family: 'Arial', sans-serif; } h1,h2,h3 { color: #90caf9; }"
}

class MarkdownConverter:
    def __init__(self):
        self.md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables'])

    def to_html(self, markdown_text: str) -> str:
        """Convert markdown text to HTML."""
        return self.md.convert(markdown_text)

    def to_plain_text(self, markdown_text: str) -> str:
        """Convert markdown text to plain text by removing markdown syntax."""
        # Remove headers
        text = re.sub(r'#{1,6}\s+', '', markdown_text)
        # Remove bold and italic
        text = re.sub(r'[*_]{1,2}(.*?)[*_]{1,2}', r'\1', text)
        # Remove links
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
        # Remove code blocks
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        # Remove inline code
        text = re.sub(r'`(.*?)`', r'\1', text)
        # Remove horizontal rules
        text = re.sub(r'[-*_]{3,}', '', text)
        # Remove blockquotes
        text = re.sub(r'^\s*>\s*', '', text, flags=re.MULTILINE)
        # Remove lists
        text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
        return text.strip()


class MarkdownConvertProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        # No credentials needed for markdown conversion
        pass

    def invoke(self, tool_parameters: dict) -> str | bytes:
        markdown_text = tool_parameters.get('markdown_text', '')
        output_format = tool_parameters.get('output_format', 'html')
        style = tool_parameters.get('style', 'default')
        if not markdown_text:
            raise ValueError("markdown_text is required")
        html = markdown.markdown(markdown_text, extensions=['extra', 'codehilite', 'tables'])
        if output_format == 'html':
            return html
        elif output_format == 'plain_text':
            text = re.sub(r'#{1,6}\s+', '', markdown_text)
            text = re.sub(r'[*_]{1,2}(.*?)[*_]{1,2}', r'\1', text)
            text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
            text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
            text = re.sub(r'`(.*?)`', r'\1', text)
            text = re.sub(r'[-*_]{3,}', '', text)
            text = re.sub(r'^\s*>\s*', '', text, flags=re.MULTILINE)
            text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
            text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
            return text.strip()
        elif output_format == 'pdf':
            pdf_io = io.BytesIO()
            css = PDF_STYLES.get(style, PDF_STYLES['default'])
            HTML(string=html).write_pdf(pdf_io, stylesheets=[CSS(string=css)])
            pdf_io.seek(0)
            return pdf_io.read()
        else:
            raise ValueError("output_format must be 'html', 'plain_text' 或 'pdf'")
