from abc import ABC, abstractmethod

class ChatAgent(ABC):
    @abstractmethod
    def chat(self, system_prompt, user_prompt, history):
        pass
