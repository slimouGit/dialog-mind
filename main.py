from Config import OLLAMA_URL, OLLAMA_MODEL, LM_STUDIO_MODEL, LM_STUDIO_URL
from agents.LMStudioAgent import LMStudioAgent
from agents.OllamaAgent import OllamaAgent

from orchestrator import orchestrate

def main():
    ollama = OllamaAgent(OLLAMA_URL, model=OLLAMA_MODEL)
    lmstudio = LMStudioAgent(LM_STUDIO_URL, model=LM_STUDIO_MODEL)

    user_prompt = input("📝 Please enter your request: ").strip()
    if not user_prompt:
        print("⚠️ No input detected. Exiting program.")
        return

    result = orchestrate(lmstudio, ollama, user_prompt, max_rounds=4)

    print("\n✅ Final result:\n", result)

if __name__ == "__main__":
    main()