# see https://www.gradio.app/guides/chatinterface-examples#anthropics-claude
import gradio as gr
import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()


def format_output(message):
    text_formatted = message.replace("\n\n", "")
    text_formatted = text_formatted.replace("<think>", "")
    text_formatted = text_formatted.replace("</think>", "")
    print(text_formatted)
    return text_formatted

def predict(message, history):
    keys_to_keep = ["role", "content"]
    history = [{k: d[k] for k in keys_to_keep if k in d} for d in history]
    history.append({"role": "user", "content": message})

    payload = {"max_tokens": 4096, 'messages': history}

    api_key = os.getenv("DEEPSEEK_KEY", '')
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    client = ChatCompletionsClient(
        endpoint=os.getenv("DEEPSEEK_ENDPOINT", ''),
        credential=AzureKeyCredential(api_key)
    )

    response = client.complete(payload)
    return {
        "role": "assistant",
        "content": format_output(response.choices[0].message.content)
    }


demo = gr.ChatInterface(
    predict,
    examples=["Start!"],
    chatbot=gr.Chatbot(),
    type="messages"
)

demo.launch()
