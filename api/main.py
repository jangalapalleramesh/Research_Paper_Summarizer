from fastapi import FastAPI, UploadFile, File, Form
from agents.ingest_agent import extract_text_from_pdf, extract_text_from_url, extract_text_from_doi
from agents.summarize_agent import summarize_with_ollama
from agents.classify_agent import classify_topic
from agents.audio_agent import generate_audio
from agents.synthesis_agent import synthesize_summaries
from agents.search_agent import search_arxiv
from agents.citation_agent import fetch_citation_metadata

import os

app = FastAPI()

@app.post("/summarize/upload/")
async def summarize_pdf(file: UploadFile = File(...), topics: str = Form(...)):
    path = f"data/sample_papers/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(path)
    topic = classify_topic(text, topics.split(","))
    summary = summarize_with_ollama(text)
    audio_path = generate_audio(summary, file.filename.replace('.pdf', '.mp3'))

    return {"topic": topic, "summary": summary, "audio": audio_path}

@app.post("/summarize/url/")
async def summarize_from_url(url: str = Form(...), topics: str = Form(...)):
    text = extract_text_from_url(url)
    topic = classify_topic(text, topics.split(","))
    summary = summarize_with_ollama(text)
    audio_path = generate_audio(summary, "url_summary.mp3")
    return {"topic": topic, "summary": summary, "audio": audio_path}



@app.post("/summarize/doi/")
async def summarize_from_doi(doi: str = Form(...), topics: str = Form(...)):
    text = extract_text_from_doi(doi)
    if not text or text.strip() == "":
        return {"error": "Unable to extract text from DOI. It might be a metadata-only record."}

    topic = classify_topic(text, topics.split(","))
    summary = summarize_with_ollama(text)
    audio_path = generate_audio(summary, "doi_summary.mp3")
    citation = fetch_citation_metadata(doi)
    return {"topic": topic, "summary": summary, "audio": audio_path, "citation": citation}


@app.get("/search/")
def search_papers(topic: str):
    return search_arxiv(topic)
