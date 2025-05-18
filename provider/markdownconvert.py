from typing import Generator
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin import Tool

from markdownconvert.tools.markdownconvert1 import MarkdownConvertProvider

class MarkdownConvertTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        Markdown 转换工具
        tool_parameters:
            - markdown_text: 要转换的 markdown 文本
            - output_format: 输出格式（'html' 或 'plain_text'）
        """
        provider = MarkdownConvertProvider()
        try:
            result = provider.invoke(tool_parameters)
            yield self.create_text_message(result)
        except Exception as e:
            yield self.create_text_message(f"转换失败: {str(e)}")
