import fitz
import requests
from urllib.parse import quote

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)

def extract_text_from_url(url):
    response = requests.get(url)
    return response.text[:3000]  # Simplified — use full scraper in prod


def extract_text_from_doi(doi):
    headers = {"Accept": "application/vnd.crossref.unixref+xml"}
    url = f"https://doi.org/{quote(doi)}"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.ok:
            return res.text[:3000] if res.text else "No content available"
    except:
        return "Could not fetch DOI content"

