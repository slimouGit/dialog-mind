from agents.LMStudioAgent import LMStudioAgent
from agents.OllamaAgent import OllamaAgent
from config import OLLAMA_URL, LOCAL_API_URL
from orchestrator import orchestrate

def main():
    # Initialize models
    ollama = OllamaAgent(OLLAMA_URL, model="gemma3")
    lmstudio = LMStudioAgent(LOCAL_API_URL, model="granite-3.1-8b-instruct")

    # Prompt user for input
    user_prompt = input("📝 Please enter your request: ").strip()
    if not user_prompt:
        print("⚠️ No input detected. Exiting program.")
        return

    # Start orchestration
    result = orchestrate(lmstudio, ollama, user_prompt, max_rounds=4)

    print("\n✅ Final result:\n", result)

if __name__ == "__main__":
    main()