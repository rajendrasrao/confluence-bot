from langchain.vectorstores import Chroma
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import CSVLoader
from langchain_experimental.agents import create_csv_agent
from langchain.agents.agent_types import AgentType
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate; 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
import streamlit as st
from bs4 import BeautifulSoup
import base64
import requests
import json

load_dotenv()
confluence_domain =os.getenv('CONF_DOMAIN')
username =os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
# Set your Confluence details here
space_key =  os.getenv('space_key')   # replace with your info

llm=GoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.0)
template=PromptTemplate.from_template("Answer the following question based only the provided context:"+
                                      "documents:{context}"
                                       "Question:{input}"+
                                      " response should be in json format if not then convert it in json format with two field (1)summary (2)url  ")
persist_directory = 'csv_docs/chroma/'
emb=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectordb = Chroma(persist_directory=persist_directory, embedding_function=emb)

retriver=vectordb.as_retriever()


def get_question_response(user_input):
 

#doc_chain=create_stuff_documents_chain(llm=llm,prompt=template)
    chain = (
    {"context": retriver, "input": RunnablePassthrough()}
    | template
    | llm
    | StrOutputParser()
)

    response=chain.invoke(user_input)
    return response

def get_content(path):
    custom_url=""
    if path is not None:
        custom_url=path
    
    authorization = f"Basic {base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')}"

    headers = {
       "Authorization": authorization
     }

    response = requests.get(custom_url, headers=headers)
    return response

def main():
    st.title("your confluence bot")
    user_input = st.text_input("enter your question and we "+
                               "will try to get response and pages link where full answer could be there ")
    
    if st.button("Submit"):
       
       response=get_question_response(user_input)
       json_resp=response.replace("```json","").replace("```","")
       print("resp:",json_resp)
       json_resp=json.loads(json_resp)
       st.session_state['json_resp'] = json_resp

       st.write(json_resp['summary'])
    if 'json_resp' in st.session_state:
        if st.button("see full page"):
            json_resp=st.session_state['json_resp']
            if json_resp['url'] is not None: 
               cont=get_content(json_resp['url']+"?expand=body.view")
               inner_json_obj=json.loads(cont.text)
               print(inner_json_obj)
               st.write("Title:",inner_json_obj['title'])
               st.markdown(inner_json_obj['body']['view']['value'], unsafe_allow_html=True)

 

if __name__=="__main__":
   main() 