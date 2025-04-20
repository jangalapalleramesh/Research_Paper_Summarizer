from .summarize_agent import summarize_with_ollama

def synthesize_summaries(summaries):
    joined = "\n\n".join(summaries)
    return summarize_with_ollama(f"Combine and summarize:\n{joined}")
