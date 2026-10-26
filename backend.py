from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)


def ask_gemini(question, context):
    """
    Ask Gemini a question using the provided knowledge context.
    """

    prompt = f"""
You are an AI Personal Knowledge Assistant.

Use ONLY the information provided in the knowledge below.

If the answer is not available in the knowledge,
say that you could not find the information.

Knowledge:
{context}

User Question:
{question}

Give a clear and useful answer.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text


def generate_decision_brief(decision, context):
    """
    Generate a decision brief using the provided knowledge.
    """

    prompt = f"""
You are an AI Decision Assistant.

Use ONLY the information provided in the knowledge.

Decision to make:
{decision}

Knowledge:
{context}
Create a concise, evidence-based decision brief.

Use exactly these sections:

## 1. Decision
Clearly state the decision being considered.

## 2. Key Findings
List the most important findings from the provided knowledge.

## 3. Options
List the realistic options found in the knowledge.

## 4. Comparison
Compare the options using only the available evidence.

## 5. Advantages & Disadvantages
Give important advantages and disadvantages for each option.

## 6. Evidence
Mention which source supports the important findings.
For PDFs, include the page number when available.

## 7. Recommendation
Give one practical recommendation based only on the evidence.
Explain why.

## 8. Risks & Considerations
Mention important risks, limitations, or missing information.

Rules:
- Use ONLY the provided knowledge.
- Do not invent facts.
- If information is missing, clearly say "Not available in the provided sources."
- Keep the response concise and easy to understand.
- Use bullet points where appropriate.

Do not invent information.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text