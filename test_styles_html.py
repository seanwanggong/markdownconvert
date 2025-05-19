
from tools.markdownconvert_html import MarkdownConvertHtmlProvider


styles = ["default", "tech_blue", "business_dark", "pastel","grand"]
test_markdown = '''
# 测试标题 Test Title

这是一个中英文混合的段落。This is a mixed paragraph。

- 列表项一
- Item Two
  - 嵌套子项
    - 更深层子项

1. 有序列表一
2. 有序列表二

> 这是引用 blockquote
> 
> - 引用里的列表
> - 依然支持

---

**粗体文本**、*斜体文本*、~~删除线~~、`行内代码`

```python
# 代码块示例
def hello():
    print("Hello, 世界！")
```

| 姓名   | 年龄 | 城市   |
|--------|------|--------|
| 张三   | 28   | 北京   |
| 李四   | 32   | 上海   |
| Alice  | 25   | London |
| Bob    | 30   | New York |

![Dify Logo](http://localhost/logo/logo.png)

[百度](https://baidu.com) | [Google](https://google.com)

---

最后一行，混合**样式**和[链接](https://dify.ai)。
'''

provider = MarkdownConvertHtmlProvider()

for style in styles:
    print(f"正在测试风格: {style}")
    result = provider.invoke({'markdown': test_markdown, 'style': style})
    if result.get('status') == 'success':
        with open(f'test_output_{style}.html', 'wb') as f:
            f.write(result.get('result', b''))
        print(f"{style} 风格 html 生成成功")
    else:
        print(f"{style} 风格 html 生成失败: {result.get('message')}")