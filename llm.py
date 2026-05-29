import requests
import json

class OllamaLLM:
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.base_url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str, stream: bool = False) -> str:
        """
        Send prompt to Ollama and get response
        """
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream
        }

        try:
            response = requests.post(self.base_url, json=payload)

            if response.status_code != 200:
                raise Exception(f"Error: {response.status_code} - {response.text}")

            data = response.json()
            return data.get("response", "")

        except requests.exceptions.ConnectionError:
            return "❌ ERROR: Ollama server not running. Start with `ollama serve`"
        except Exception as e:
            return f"❌ ERROR: {str(e)}"


# 🔹 Simple test (this acts as debug)
if __name__ == "__main__":
    llm = OllamaLLM()

    prompt = "Explain what is an AI agent in simple terms."

    print("\n🧠 Sending prompt to LLaMA3...\n")
    output = llm.generate(prompt)

    print("✅ Response:\n")
    print(output)