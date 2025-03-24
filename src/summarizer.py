import google.generativeai as genai
import os

# Load API key from environment variable
genai.configure(api_key="")


def summarize_text(text):
    """Summarizes a given text using Google Gemini AI."""
    model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Free model
    response = model.generate_content(f"Summarize this text:\n{text}")
    return response.text.strip()

# Test it
if __name__ == "__main__":
    test_text = "Artificial Intelligence is a field of computer science that aims to create machines that mimic human intelligence. It involves machine learning, deep learning, and natural language processing."
    summary = summarize_text(test_text)
    print("Summary:\n", summary)
