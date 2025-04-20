import subprocess

def summarize_with_ollama(text):
    prompt = f"summarize this academic content:\n\n{text[:3000]}"
    result = subprocess.run(["ollama", "run", "llama3", prompt], capture_output=True, text=True)
    return result.stdout.strip()
