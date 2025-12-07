import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") 

import streamlit as st

st.title("心身を健康に保つ余暇の過ごし方、運動と読書に特化したアドバイスアプリ")

st.write("##### 専門家1: 運動ならまかせとけ先生")
st.write("入力フォームに運動に関する質問を入力し、「実行」ボタンを押してください。")
st.write("##### 専門家2: 読書ならなんでもアドバイス先生")
st.write("入力フォームに読書に関する疑問を入力し、「実行」ボタンを押してください。")

selected_item = st.radio(
    "専門家を選択してください。",
    ["運動ならまかせとけ先生", "読書ならなんでもアドバイス先生"]
)

st.divider()

if selected_item == "運動ならまかせとけ先生":
    input_message = st.text_input(label="運動に関する質問を入力してください。")
    
else:
    input_message = st.text_input(label="読書に関する疑問を入力してください。")
    

if st.button("実行"):
    st.divider()

    if selected_item == "運動ならまかせとけ先生":
        if input_message:
            from langchain_openai import ChatOpenAI
            from langchain_core.messages import SystemMessage, HumanMessage

            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

            messages = [
                SystemMessage(content="あなたは運動に詳しい専門家です。"),
                HumanMessage(content=input_message),
            ]

            result = llm.invoke(messages)

            st.write(result.content)

        
    else:
        if input_message:
            from langchain_openai import ChatOpenAI
            from langchain_core.messages import SystemMessage, HumanMessage

            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

            messages = [
                SystemMessage(content="あなたは読書に詳しい専門家です。"),
                HumanMessage(content=input_message),
            ]

            result = llm.invoke(messages)

            st.write(result.content)