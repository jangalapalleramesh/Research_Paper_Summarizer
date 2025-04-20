import requests
import xml.etree.ElementTree as ET

def search_arxiv(topic, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    query = f"search_query=all:{topic}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    response = requests.get(base_url + query)

    papers = []
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
            link = entry.find('{http://www.w3.org/2005/Atom}id').text
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
            papers.append({'title': title, 'url': link, 'summary': summary})
    return papers
