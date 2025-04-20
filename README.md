# 🧠 Research Paper Summarizer - Multi-Agent AI System

This project is a **multi-agent system** designed to automate the discovery, processing, summarization, classification, and podcast-style narration of research papers. It supports inputs via **file upload, URLs, and DOI references**, and uses **local LLMs via Ollama** for secure and efficient summarization.

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/research-summarizer.git
cd research-summarizer
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and Run Ollama
Download Ollama from https://ollama.com  
Then run the following command to start the LLaMA model:
```bash
ollama run llama3
```

### 4. Launch the API
```bash
uvicorn api.main:app --reload
```

### 5. Test the system
Open your browser and navigate to:
```
http://localhost:8000/docs
```
Use the Swagger UI to test endpoints for:
- PDF upload
- URL/DOI ingestion
- ArXiv search

---

## 🏗️ System Architecture

```
                      +------------------+
                      |   User / Client  |
                      +--------+---------+
                               |
                               v
          +---------------- FastAPI Backend ----------------+
          |                                                 |
          |  +---------+   +---------+   +---------+        |
          |  | Search  |   | Ingest  |   | Classify|        |
          |  | Agent   |-->| Agent   |-->| Agent   |        |
          |  +---------+   +---------+   +---------+        |
          |                                   |             |
          |                             +-----v------+       |
          |                             | Summarizer |       |
          |                             +-----+------+       |
          |                                   |              |
          |    +----------+      +------------v-----------+  |
          |    | Citation |<-----| Synthesis + Audio Agent|  |
          |    | Agent    |      +------------------------+  |
          +--------------------------------------------------+
```

---

## 🤖 Multi-Agent Design & Coordination

| Agent              | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `search_agent.py`     | Uses ArXiv API to search papers by topic, with filters for recency and relevance |
| `ingest_agent.py`     | Accepts papers via file upload, DOI, or URL and extracts textual content         |
| `classify_agent.py`   | Matches paper text to the best topic from a user-provided list                    |
| `summarize_agent.py`  | Uses Ollama's local LLaMA model to summarize the paper content                   |
| `synthesis_agent.py`  | Combines multiple summaries into a single synthesized overview                   |
| `audio_agent.py`      | Uses gTTS to generate an MP3 audio summary                                       |
| `citation_agent.py`   | Fetches citation metadata from DOI using CrossRef                               |

The agents are orchestrated through FastAPI endpoints, triggered either individually or sequentially.

---

## 📝 Paper Processing Methodology

- PDFs are parsed using **PyMuPDF**, extracting clean textual content
- DOI inputs are resolved using the **CrossRef API** to fetch metadata and (sometimes) content
- URLs fetch raw HTML content (simplified), which can be upgraded with full scraping logic
- The extracted text is truncated and passed to a local Ollama model for summarization

---

## 🔊 Audio Generation Implementation

- We use **Google Text-to-Speech (gTTS)** to convert the LLM-generated summaries into `.mp3` files
- These are saved in the `outputs/audios/` folder
- The response includes the file path so it can be streamed/downloaded via a frontend

---

## 📚 Example Usage

#### Upload PDF:
- Go to `/summarize/upload/`
- Choose file + topic list (e.g., `AI, Robotics, Quantum Computing`)

#### Ingest from DOI:
- Go to `/summarize/doi/`
- Enter: `10.1145/3366423.3380143`
- Add your topics

#### Search for Recent Papers:
- Use `/search/?topic=AI`

---

## ⚠️ Limitations

- URL handling is basic (fetches raw HTML without semantic parsing)
- DOI content may not always be accessible or full-text
- ArXiv API doesn't support full paper content — only abstract & metadata
- Ollama summarization is limited to local context window (~3000 tokens)

---

## 🔮 Future Improvements

- Use `BeautifulSoup` or `newspaper3k` to better parse full-text from URLs
- Add ArXiv PDF auto-download for full content summarization
- Integrate an advanced topic modeling approach (e.g., BERTopic)
- Extend to handle batch ingestion and topic-wise clustering
- Add a front-end dashboard for better usability (Streamlit or React)

---

## 🙌 Credits

- [Ollama](https://ollama.com) for offline LLM support  
- [arXiv API](https://arxiv.org/help/api/index) for research discovery  
- [CrossRef API](https://api.crossref.org/) for citation data  
- [gTTS](https://pypi.org/project/gTTS/) for audio generation  

---

## 📫 Contact

*Created by [Venkata Ramesh Jangalapalle]*  
*Email: venkataramesh255@gmail.com *  
*GitHub: https://github.com/jangalapalleramesh/ *
