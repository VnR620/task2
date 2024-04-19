import gradio as gr
import requests

# 定义发送POST请求并获取结果的函数
def http_add(a, b):
    data = {'a': a, 'b': b}
    response = requests.post('http://localhost:5000/add', data=data)
    return response.json()['result']

# 创建Gradio界面
iface = gr.Interface(
    fn=http_add,  # 指定处理函数
    inputs=[gr.Number(label="输入a"), gr.Number(label="输入b")],  # 创建两个数字输入框
    outputs=gr.Textbox(label="结果")  # 创建一个文本输出框用于显示结果
)

# 运行应用
iface.launch()
