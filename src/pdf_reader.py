from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path, word_limit=500):
    """Extracts text from a given PDF file and returns the first `word_limit` words."""
    reader = PdfReader(pdf_path)
    text = ""
    
    for page in reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text + " "
    
    words = text.strip().split()  # Split text into words
    return " ".join(words[:word_limit])

# Test it
if __name__ == "__main__":
    text = extract_text_from_pdf("data/wings_of_fire.pdf")  # Replace with your actual PDF
    print(text[:100])  # Print first 1000 characters for preview
