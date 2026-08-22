import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


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

    response = model.generate_content(prompt)

    return response.text