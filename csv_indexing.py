from langchain.vectorstores import Chroma
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import csv_loader
from langchain_experimental.agents import create_csv_agent
from langchain.agents.agent_types import AgentType
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate; 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

load_dotenv()

#loader=csv_loader("final_text.csv")
#data = loader.load()
loader=TextLoader("final_text.txt",encoding="utf8")
docs=loader.load()
llm=GoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.0)
splliter=RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=15)
splited_docs=splliter.split_documents(documents=docs)
template=PromptTemplate.from_template("Answer the following question based only the provided context:"+
                                      "documents:{context}"
                                       "Question:{input}"+
                                      "");

persist_directory = 'docs/chroma/'
emb=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectordb = Chroma.from_documents(
    documents=splited_docs,
    embedding=emb,
    persist_directory=persist_directory
)


doc_chain=create_stuff_documents_chain(llm=llm,prompt=template)
retriver=vectordb.as_retriever()
ret_chain=  create_retrieval_chain(retriver,doc_chain)
response=ret_chain.invoke({"context":"please alanlyze all documents provided and answer question: "
                  ,"input":"can you give summary with Manu Bhaker."})
print(response["answer"])
