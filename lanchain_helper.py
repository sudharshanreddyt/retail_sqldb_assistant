import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase # for establishing connection
from langchain_experimental.sql import SQLDatabaseChain # for connection llm and db
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.example_selectors.semantic_similarity import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from few_shots import few_shots

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


def get_fewshot_db_chain():
    # 1. Initialize the LLM
    llm = ChatGoogleGenerativeAI(
        model='gemini-2.5-flash',
        temperature = 0.1
    )

    # 2. Create the SQL connection
    db_user = "root"
    db_password = "your_password"
    db_host = "localhost"
    db_name="atliq_tshirts"

    database_uri = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"
    db = SQLDatabase.from_uri(database_uri = database_uri, sample_rows_in_table_info = 3)

    # Initialize the Huugingface embeddings
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')

    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vector_store = Chroma.from_texts(
        texts=to_vectorize,
        embedding=embeddings,
        metadatas=few_shots
    )

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vector_store,
        k = 2
    )

    template = "Question: {Question} \n SQLQuery: {SQLQuery} \n SQLResult: {SQLResult}\n Answer: {Answer}"
    example_prompt = PromptTemplate.from_template(template)

    fewshot_template = FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt = example_prompt,
        prefix = _mysql_prompt,
        suffix = PROMPT_SUFFIX,
        input_variables = ["input", "table_info", "top_k"]
    )

    # Create the Database chain
    db_chain = SQLDatabaseChain.from_llm(llm = llm, db = db, prompt=fewshot_template)
    return db_chain


if __name__ == "__main__":
    chain = get_fewshot_db_chain()
    qns = chain.invoke("How many white color Levi's t-shirts are available?")
    print(qns)