import requests

from chat_agents import ChatAgent


class OllamaAgent(ChatAgent):
    def __init__(self, url, model):
        self.url = url
        self.model = model

    def chat(self, system_prompt, user_prompt, history):
        prompt = f"{system_prompt}\n\n" + "\n".join(
            [f"{m['role'].capitalize()}: {m['content']}" for m in history]
        ) + f"\nUser: {user_prompt}"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(self.url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()