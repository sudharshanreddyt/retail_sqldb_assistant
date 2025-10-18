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

5. **Set Up the MySQL Database Locally**
    Execute the `db_creation_atliq_t_shirts.sql` file (found in the `database` folder of the project repository) in your `MySQL Workbench`.

    This script will:
        1. Create a new database named atliq_tshirts.
        2. Create the necessary tables (e.g., t_shirts, discounts).
        3. Populate those tables with sample inventory data for the retail store.

6. **Create the SQL connection**

    Add the following variables to your existing .env file, replacing the placeholders with your actual MySQL credentials:
    
    ```env 
    MYSQL_HOST="localhost"
    MYSQL_USER="root" # Or your MySQL username
    MYSQL_PASSWORD="YOUR_MYSQL_PASSWORD" # Your MySQL password
    MYSQL_DATABASE="atliq_tshirts" # The database created in Step 5
    ```

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
├── database                    # Folder that contains the mysql file for creating the database
├── outputs                     # Folder that contains the final streamlit output images
├── langchain_helper.py         # Core LangChain chains and logic
├── main.py                     # Main application entry point
├── requirements.txt            # Project dependencies
├── few_shots.py                # Few shot examples
├── retail_sqldb.ipynb          # Jupyter notebook for experimentation
└── README.md                   # This file
```

## Sample Outputs
![alt text](/outputs/output1.png)