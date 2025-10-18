# RETAIL SQL DB Assistant(SQL-on-LLM)
This project is an end-to-end Generative AI application that allows users to query a MySQL database using natural language. Built for a retail environment (Atliq T-shirts store), it enables non-technical users, like a store manager, to ask complex questions about inventory, stock, and sales without writing a single line of SQL.

## Key Features

- **Natural Language to SQL**: Converts plain English questions (e.g., "How much revenue will I generate if I sell all Levi's t-shirts after discount?") into executable MySQL queries.
- **Few-Shot Learning**: Implements few-shot prompting with a Vector Database (ChromaDB) and Hugging Face   embeddings to guide the LLM, ensuring it generates highly accurate SQL queries and overcomes common LLM 'hallucinations' about database structure.
- **Interactive UI**: A simple, user-friendly interface built with **Streamlit**.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google API key (or compatible LLM API)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudharshanreddyt/retail_sqldb_assistant.git
   cd retail_sqldb_assistant
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Create the SQL connection**

    Make sure you are actually connecting to the sql server in the local host and replace the variables for db_user, db_password in `langchain_helper.py`


### Run the Main Application

```bash
streamlit run main.py
```

## Project Structure

```
RETAIL_SQLDB_ASSISTANT/
├── .venv/                      # Virtual environment (not in git)
├── __pycache__/                # Python cache (not in git)
├── .env                        # Environment variables (not in git)
├── .gitignore                  # Git ignore file
├── langchain_helper.py         # Core LangChain chains and logic
├── main.py                     # Main application entry point
├── requirements.txt            # Project dependencies
├── few_shots.py                # Few shot examples
├── retail_sqldb.ipynb          # Jupyter notebook for experimentation
└── README.md                   # This file
```

## Sample Outputs
![alt text](/outputs/output1.png)