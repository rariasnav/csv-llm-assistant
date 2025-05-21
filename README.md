# 🧠 CSV LLM Assistant

An interactive assistant that allows you to explore CSV files with the help of LLMs. Upload any dataset, ask questions in natural language, and receive answers — with automatically suggested visualizations and context-aware responses.

> Example:  
> **“What’s the average salary by job title?”** → AI suggests a bar chart comparing roles and salaries.

---

## 🚀 Features

- Upload your own **CSV file**.
- Generates an automatic **data summary** using `pandas`.
- Asks **natural language** questions (e.g., “Which job pays the most?”).
- Uses **LangChain + OpenAI** to answer questions.
- Suggests **data visualization** (bar, box, histogram) with justification.
- Optionally explore charts manually (Streamlit controls)
- Modular structure (utils for summaries, LLM, and plots).

---

## 🛠️ Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/) + [Seaborn](https://seaborn.pydata.org/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/rariasnav/csv-llm-assistant.git
cd pdf-llm-assistant

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Then add your OpenAI API key to .env
```
---

## 🧪 Run the App

```bash
# Web UI (Streamlit)
streamlit run app.py

### Terminal Mode
python main.py
```

---

📁 Folder Structure
```bash
.
├── app.py                  # Web interface
├── main.py                 # Terminal mode            # Folder for uploaded PDFs
├── vectorstore/            # FAISS vector indexes
├── utils/ 
│   ├── data_summary.py     # Summary logic
│   ├── question_answering.py # LLM question handler
│   └── visualizer.py       # Chart generation                 # Modular functions (PDF, embeddings, QA)
├── .env.example
├── requirements.txt
└── README.md
```

---

👤 Author
Rafael Arias – [LinkedIn](https://www.linkedin.com/in/rafael-arias-navarro/)
AI Developer | 🇨🇴 Seeking opportunities with relocation in Europe or UK# csv-llm-assistant
# csv-llm-assistant
