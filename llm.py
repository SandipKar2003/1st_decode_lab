from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def ask_llm(query):

    retries = 3

    for _ in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
You are a friendly AI chatbot.

Instructions:
- Answer naturally and conversationally.
- Keep simple answers short.
- Give detailed explanations only when the question requires it.
- For programming questions, include examples when useful.
- For greetings, reply in one short sentence.
- Avoid repeating information.
- Use bullet points for lists when appropriate.

User Question:
{query}
"""
            )

            return response.text

        except Exception as e:

            error = str(e)

            if "503" in error:
                time.sleep(2)
                continue

            return f"Error: {error}"

    return "Gemini server is currently busy. Please try again later."