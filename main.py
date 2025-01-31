#see https://www.gradio.app/guides/chatinterface-examples#anthropics-claude
import gradio as gr
import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

placeholder = """
<center><h1>10 Questions</h1><br>Think of a person, place, or thing. I'll ask you 10 yes/no questions to try and guess it.
</center>
"""

load_dotenv()

def predict(message, history):
    api_key = os.getenv("AZURE_INFERENCE_CREDENTIAL", '')
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    client = ChatCompletionsClient(
        endpoint='',
        credential=AzureKeyCredential(api_key)
    )

    model_info = client.get_model_info()
    print("Model name:", model_info.model_name)
    print("Model type:", model_info.model_type)
    print("Model provider name:", model_info.model_provider_name)

    payload = {
        "messages": [
            {
                "role": "user",
                "content": "I am going to Paris, what should I see?"
            },
            {
                "role": "assistant",
                "content": "Paris, the capital of France, is known for its stunning architecture, art museums, historical landmarks, and romantic atmosphere. Here are some of the top attractions to see in Paris:\n\n1. The Eiffel Tower: The iconic Eiffel Tower is one of the most recognizable landmarks in the world and offers breathtaking views of the city.\n2. The Louvre Museum: The Louvre is one of the world's largest and most famous museums, housing an impressive collection of art and artifacts, including the Mona Lisa.\n3. Notre-Dame Cathedral: This beautiful cathedral is one of the most famous landmarks in Paris and is known for its Gothic architecture and stunning stained glass windows.\n\nThese are just a few of the many attractions that Paris has to offer. With so much to see and do, it's no wonder that Paris is one of the most popular tourist destinations in the world."
            },
            {
                "role": "user",
                "content": "What is so great about #1?"
            }
        ],
        "max_tokens": 2048
    }
    response = client.complete(payload)
    return {
        "role": "assistant",
        "content": response.choices[0].message.content
    }

demo = gr.ChatInterface(
    predict,
    examples=["Start!"],
    chatbot=gr.Chatbot(placeholder=placeholder),
    type="messages"
)

demo.launch()