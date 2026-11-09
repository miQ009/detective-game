# Cold Case Files

**Cold Case Files is an AI-powered, point-and-click-style detective mystery game** built with Python, Streamlit, and SQLite. Suspects are driven by a Large Language Model (Groq / `gpt-oss-120b`) but strictly bounded: they remember what you tell them, hide secrets until you find the evidence, and cannot invent facts. 

---

## 🔗 Project Links
* **Live Demo:** https://miq-detective-game.streamlit.app/
* **GitHub Repository:** https://github.com/miQ009/detective-game

---

## 📝 Short Description
Each case is a fixed, predefined mystery. The player examines clues in a room, interrogates three suspects, and submits a written theory. An AI “chief” judges the theory based on *who*, *why*, and *where*. Players earn points for correct supporting details and lose points for extra attempts. 

The main design goal was keeping the AI reliable inside a game ecosystem: suspects only unlock a secret *after* the player finds the matching clue, preventing them from leaking or inventing evidence.

---

## ✨ Key Features

### 🕵️‍♂️ Grounded AI Characters
* **Predefined Facts:** Characters operate within strict boundaries.
* **Evidence-Unlocked Secrets:** Suspects cannot leak information until the player uncovers the matching clue.
* **Anti-Hallucination Prompting:** Strict prompt engineering ensures characters never invent outside details.

### 🧠 Persistent Memory with Relevance Retrieval
* **SQLite Storage:** Every suspect possesses persistent conversational memory.
* **Context Optimization:** A maximum of 4 relevant memories are sent per request to keep API calls cheap.
* **Information Layering:** Secondhand information (*“Clara told me...”*) is stored and processed separately from firsthand observations.

### ⚖️ LLM Judge with Structured Output
* **JSON Responses:** The LLM judge evaluates the final theory and returns structured JSON data.
* **Deterministic Scoring:** The final win/lose decision and score calculations are handled securely in plain Python.

### ⚙️ Architecture & Operations
* **Extensible Architecture:** Each case is a self-contained file. Adding a new mystery requires zero changes to core game logic.
* **Per-Player Progress:** Each visitor gets an isolated session, even when running on a shared database.
* **Production Ready:** Includes automated tests for the memory layer, a password-protected admin page, and deployment configurations.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend/UI:** Streamlit
* **Database:** SQLite
* **LLM Engine:** Groq API (`gpt-oss-120b`)
* **Version Control:** Git / GitHub
* **Deployment:** Streamlit Community Cloud (with integrated secrets management)

---

## ⚠️ Current Limitations
* **Memory Retrieval:** Uses keyword-based memory retrieval rather than vector embeddings.
* **API Constraints:** Subject to free-tier rate limits on the Groq API under heavy traffic.
