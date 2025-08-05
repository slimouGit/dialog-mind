import os

import openai

from chat_agents import ChatAgent
from config import OPENAI_API_KEY


class OpenAIAgent(ChatAgent):
    def __init__(self, url, model):
        self.url = url
        self.model = model

    def chat(self, system_prompt, user_prompt, history):
        openai_client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY") or OPENAI_API_KEY,
            base_url=self.url
        )
        messages = [{"role": "system", "content": system_prompt}] + history
        messages.append({"role": "user", "content": user_prompt})
        response = openai_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content