import requests

from chat_agents import ChatAgent


class LMStudioAgent(ChatAgent):
    def __init__(self, url, model):
        self.url = url
        self.model = model

    def chat(self, system_prompt, user_prompt, history):
        messages = [{"role": "system", "content": system_prompt}] + history
        messages.append({"role": "user", "content": user_prompt})
        request_body = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 300
        }
        response = requests.post(self.url, json=request_body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]