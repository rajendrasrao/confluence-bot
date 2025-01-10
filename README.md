# Confluence Q&A Bot

This repository contains the code for a question-answering bot that retrieves information from Confluence pages and utilizes vector databases for information retrieval.

## Project Setup

**1. Prerequisites:**

* Python 3.x
* Libraries:
    * `requests`
    * `llangchain`
    * `chroma`
    * `streamlit`

**2. Clone the repository:**

```bash
git clone https://<your_github_username>/confluence-qa-bot.git


**3. Create a virtual environment (recommended):**

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate.bat  # For Windows

**4. Install dependencies:**
pip install -r requirements.txt

**5. Create a .env file:**
GOOGLE_API_KEY=<your_google_api_key>
CONF_DOMAIN=<your_confluence_domain>
USER_NAME=<your_confluence_username>
PASSWORD=<your_confluence_password>

**Running the Bot**
Running the Bot
1. Download Confluence Pages:

The code to download Confluence pages using the API and password is not provided in this README for security reasons. It's recommended to implement a secure mechanism for authentication and avoid storing passwords in plain text.
Make sure you have a script or function that retrieves Confluence pages based on the provided variables and stores the content in a suitable format (e.g., JSON).
2. Create Vector Database:

The script to create a vector database using llangchain and chroma is also not included. You'll need to develop code that processes the downloaded Confluence content and builds the vector database using these libraries.
3. Run Streamlit App:

Once you have the downloaded Confluence content and the vector database, navigate to the project directory in your terminal and run the following command:
Bash

streamlit run app.py
This will launch the Streamlit web app where users can ask questions about the Confluence content.




