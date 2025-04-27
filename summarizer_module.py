from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, max_len=130, min_len=30) -> str:
    if len(text.split()) < 30:
        return "Text too short to summarize."
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']
