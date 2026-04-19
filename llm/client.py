# llm/client.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    def __init__(self):
        api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            raise EnvironmentError(
                "GROQ_API_KEY nahi mila!\n"
                "Check karo .env file mein key likhi hai ya nahi."
            )

        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def complete(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"\n[LLMClient Error]: {e}")
            raise
