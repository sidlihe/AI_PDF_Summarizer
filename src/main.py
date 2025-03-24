import os
import google.generativeai as genai
from pdf_reader import extract_text_from_pdf
from summarization_pipeline import stuff_summarization, map_reduce_summarization

def main():
    pdf_path = "data/wings_of_fire.pdf"  # Change to actual path
    text = extract_text_from_pdf(pdf_path)

    if len(text) < 150:
        summary = stuff_summarization(text)
    else:
        summary = map_reduce_summarization(text)

    print("\nFinal Summary:\n", summary)

if __name__ == "__main__":
    main()

