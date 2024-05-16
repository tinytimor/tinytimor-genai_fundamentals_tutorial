# GenAI Fundamentals Tutorial

The repository serves as a resource for learning about Generative AI for all levels of Python programmers. 

The Python code leverages LangChain, OpenAI's API, Anthropic's API, Google Gemini's API, ChromaDB, Sqlite libraries. For user engagement, the tutorial is centered around clinical case studies to showcase practical applications of Generative AI in healthcare and biomedical data science.

![Screenshot 2024-04-26 at 1 50 18 PM](https://github.com/tinytimor/tinytimor-genai_fundamentals_tutorial/assets/108763451/5dd9e2e7-18b7-4220-b508-b4c738c415cf)


## Contents - 🚧 Work in Progress 🚧
- `intro_tutorial`: Tutorial explaining how to use these different Large Language Models (LLMs) in Python. 
  - `tutorial0a_intro_to_llms.ipynb`: Jupyter notebook introducing users how to interact with the different LLM APIs with Python libraries - Software Developer Kits (SDKs).
  - `tutorial0b_intro_to_langchain.ipynb`: Jupyter notebook showing users how to use LangChain with different LLMs, OpenAI's GPT, Google', and Anthropic's Claude, for easy of use. 

- `rag_tutorial`: Tutorial in creating a Retrieval Augmented Generation (RAG) system using LangChain and OpenAI. 
  - `tutorial1_implementation_rag.ipynb`: Jupyter notebook with step-by-step instructions on setting up and utilizing Vector Databases and RAG for a clinical case study.
  - `medical_handbooks/`: Folder containing clinical data in PDF format, used for the case study.
 
- `text-to-sql`: Tutorial creating a Text-to-Sql Agent using LangChain and Claude to create complex SQL queries.
  - `tutorial2a_sqlite_db_creator.ipynb`: Jupyter notebook with step-by-step instructions on creating a SQLite Database locally to your computer.
  - `tutorial2b_sql_agent_claude.ipynb`: Jupyter notebook showing users how to create a the SQL Agent to allow them to query their database using natural language.
  - `csv_data/`: Folder containing clinical CSV data.
  - `sql_db`: Folder containing the local SQLite database. 

- `requirements.txt`: A list of Python packages required for the tutorial.


## Getting Started

### Prerequisites

+ Ensure you have Python installed on your system. This tutorial is tested on Python 3.8+.
+ Generate [OpenAI API key](https://openai.com/)
+ Generate [Claude API Key](https://docs.anthropic.com/claude/docs/getting-access-to-claude)
+ Generate [Gemini API Key](https://ai.google.dev/aistudio/?utm_source=aistudio.google.com&utm_medium=referral&utm_campaign=logged_out)

### Installation
1. Clone the repository to your local machine: `git clone https://github.com/tinytimor/tinytimor-genai_fundamentals_tutorial.git`
2. Enter into the downloaded repository that is on your local machine: `cd tinytimor-genai_fundamentals_tutorial`
3. Install the required Python packages: `pip install -r requirements.txt`
