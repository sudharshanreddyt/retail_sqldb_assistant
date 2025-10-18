import streamlit as st
from lanchain_helper import get_fewshot_db_chain

st.title("T-Shirts Database : Q&A")

question = st.text_input("Question : ")

get_btn = st.button("Get Data")

if get_btn:
    if question:
        st.write("The question is : ", question)
        
        with st.spinner("Getting Data...."):
            chain = get_fewshot_db_chain()
            answer = chain.invoke(question)
            st.subheader("Answer : ")
            st.write(answer["result"])
    else:
        st.error("Please enter the question...")