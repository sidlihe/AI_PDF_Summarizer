from text_splitter import split_text
from summarizer import summarize_text

def stuff_summarization(text):
    """Performs simple summarization on small documents."""
    return summarize_text(text)

def map_reduce_summarization(text):
    """Breaks text into chunks, summarizes each, and combines results."""
    chunks = split_text(text)
    
    summarized_chunks = [summarize_text(chunk) for chunk in chunks]
    
    # Reduce phase: Summarize the summarized chunks
    final_summary = summarize_text("\n".join(summarized_chunks))
    
    return final_summary

# Test
if __name__ == "__main__":
    sample_text = "This is a long document. " * 200
    print("Stuff Summarization:\n", stuff_summarization(sample_text))
    print("\nMapReduce Summarization:\n", map_reduce_summarization(sample_text))
