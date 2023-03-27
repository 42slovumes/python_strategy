import gradio as gr
import markdown

# 建立Gradio Text框元件
code_textbox = gr.inputs.Textbox(type="text", label="Enter Code Here", lines=15)

def display_code_as_markdown(code):
    # 將輸入的代碼轉換為Markdown格式的代碼塊
    markdown_code = f'<pre><code>{code}</code></pre>'

    # 將轉換後的Markdown格式代碼塊返回給Gradio Text框元件進行顯示
    return markdown_code

# 建立Gradio介面
gr.Interface(fn=display_code_as_markdown, inputs=code_textbox, outputs="markdown").launch()
