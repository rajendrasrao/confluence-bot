Confluence Q&A Bot

This repository contains the code for a question-answering bot that retrieves information from Confluence pages and utilizes vector databases for information retrieval.

Project Setup

Prerequisites:
Python 3.x
Libraries:
requests
llangchain
chroma
streamlit
Clone the repository:
Bash

git clone https://<your_github_username>/confluence-qa-bot.git
Create a virtual environment (recommended):
Bash

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate.bat  # For Windows
Install dependencies:
Bash

pip install -r requirements.txt
Create a .env file:
Create a file named .env in the project root directory.

Add the following environment variables to the .env file, replacing placeholders with your actual values:

GOOGLE_API_KEY=<your_google_api_key>
CONF_DOMAIN=<your_confluence_domain>
USER_NAME=<your_confluence_username>
PASSWORD=<your_confluence_password>
Running the Bot

Download Confluence Pages:

The code to download Confluence pages using the API and password is not provided in this READEME for security reasons. It's recommended to implement a secure mechanism for authentication and avoid storing passwords in plain text.
Make sure you have a script or function that retrieves Confluence pages based on the provided variables and stores the content in a suitable format (e.g., JSON).
Create Vector Database:

The script to create a vector database using llangchain and chroma is also not included. You'll need to develop code that processes the downloaded Confluence content and builds the vector database using these libraries.
Run Streamlit App:

Once you have the downloaded Confluence content and the vector database, navigate to the project directory in your terminal and run the following command:

Bash

streamlit run app.py
This will launch the Streamlit web app where users can ask questions about the Confluence content.

Additional Notes

This READEME provides a general outline. You'll need to implement the specific logic for downloading Confluence pages, creating the vector database, and handling user queries within the app.py script.
Consider using environment variables to store sensitive information like API keys and passwords.
Explore techniques for improving the accuracy and efficiency of the information retrieval process.
