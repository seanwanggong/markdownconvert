from typing import Generator
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin import Tool

from tools.markdownconvert_pdf import MarkdownConvertPDFProvider


class MarkdownConvertTool(Tool):
    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage, None, None]:
        """
        Markdown 转换工具
        tool_parameters:
            - markdown_text: 要转换的 markdown 文本
            - output_format: 输出格式（'html' 或 'plain_text'）
        """
        provider = MarkdownConvertPDFProvider()
        try:
            result = provider.invoke(tool_parameters)
            if result.get('status') == 'success':
                yield self.create_text_message(str(result.get('result', '')))
            else:
                yield self.create_text_message(str(result.get('message', '转换失败')))
        except Exception as e:
            yield self.create_text_message(f"转换失败: {str(e)}")
