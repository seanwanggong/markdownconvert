from typing import Any, Dict, Generator
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from dify_plugin import ToolProvider
import markdown
import re
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import os
import uuid
from datetime import datetime
import base64

from fonts.style import DEFAULT_STYLE, TECH_BLUE_STYLE, BUSINESS_DARK_STYLE, PASTEL_STYLE, GRAND_STYLE

STYLE_MAP = {
    "default": DEFAULT_STYLE,
    "tech_blue": TECH_BLUE_STYLE,
    "business_dark": BUSINESS_DARK_STYLE,
    "pastel": PASTEL_STYLE,
    "grand": GRAND_STYLE,
}

# 创建输出目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, 'static', 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

            # 生成唯一的文件名
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            unique_id = str(uuid.uuid4())[:8]
            filename = f"markdown_{timestamp}_{unique_id}.html"
            filepath = os.path.join(OUTPUT_DIR, filename)

            # 保存HTML文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_html)

            # 构建可访问的URL
            file_url = f"/static/output/{filename}"

            # 将HTML内容转换为bytes
            html_bytes = full_html.encode('utf-8')

            return {
                "status": "success",
                "result": html_bytes,  # 直接返回bytes类型
                "execution_metadata": {
                    "format": "html",
                    "filename": filename,
                    "filepath": filepath,
                    "url": file_url
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
            # 创建文件消息
            file_message = ToolInvokeMessage(
                type=ToolInvokeMessage.MessageType.BLOB,
                message=ToolInvokeMessage.BlobMessage(
                    blob=result["result"],  # 直接使用bytes数据
                    meta={
                        "mime_type": "text/html",
                        "filename": result["execution_metadata"]["filename"]
                    }
                )
            )
            
            # 创建文本消息
            text_message = ToolInvokeMessage(
                type=ToolInvokeMessage.MessageType.TEXT,
                message=ToolInvokeMessage.TextMessage(
                    text=f"HTML文件已生成，点击链接查看: {result['execution_metadata']['url']}"
                )
            )
            
            # 先发送文件消息
            yield file_message
            # 再发送文本消息
            yield text_message
        else:
            yield self.create_text_message(result.get("message", "Unknown error"))
