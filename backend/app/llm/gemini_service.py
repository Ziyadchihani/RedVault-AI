import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Client (automatically reads GEMINI_API_KEY from environment)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(question: str, documents: list[str]) -> str:
    """
    Send the retrieved chunks to Gemini and return the answer.
    """

    context = "\n\n".join(documents)

    prompt = f"""
You are an AI assistant.

Answer the user's question ONLY using the provided context.
If the answer cannot be found in the context, reply:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text