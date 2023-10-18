import openai
import os
from dotenv import load_dotenv

def get_response(response):
    return response['choices'][0]['message']

def get_response_content(response):
    return response['choices'][0]['message']["content"]

def send_to_OpenAI(conversation, model="gpt-3.5-turbo", temp=1, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation,
        temperature=temp,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    return response