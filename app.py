import gradio as gr
from example_model import get_response

def chat(input_text):
    return get_response(input_text)

iface = gr.Interface(fn=chat, inputs="text", outputs="text", title="My Local AI")
iface.launch()
