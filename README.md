# 🧠 File-Search-MCP

It is an AI assistant that leverages the Model Context Protocol (MCP) to search and retrieve answers from a structured knowledge base (qa.txt). 

---

## 🚀 Features

- MCP Integration: Utilizes MCP to standardize communication between AI models and external tools.

- Tool-Based Retrieval: Employs a custom search_qa tool to fetch answers from qa.txt.

- Interactive CLI: Provides a command-line interface for user interaction.

---

## 🧰 Project Structure

```bash
ExamBOT/
├── connect.py          # Main script to run the AI assistant
├── main.py             # MCP server defining the search tool
├── tools.py            # Additional tool definitions (optional)
├── qa.txt              # Knowledge base with question-answer pairs
├── .env                
```
---

## 🛠️ Setup & Installation

- Clone the Repository:
```bash 
git clone https://github.com/ItshMoh/file-search-mcp
cd file-search-mcp
```
- Install Dependencies:

Ensure you have Python 3 installed. Then, install required packages:
```bash
pip install -r requirements.txt
```

- Set Up Environment Variables:

Create a .env file in the project root and add your OpenAI API key, leave it empty when running the LLAMAEDGE server:
```bash
OPENAI_API_KEY=""
```
- Prepare the Knowledge Base:

Ensure qa.txt contains your question-answer pairs in the following format:

```txt
What is Python?::Python is a high-level, interpreted programming language.
Who wrote Hamlet?::William Shakespeare wrote the play “Hamlet”.
```
---

## ▶️ Running the Application

```bash
python connect.py
```
You'll be prompted to enter your questions. Type your query and press Enter. To exit, type exit.