import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
import pandas as pd
import requests
import base64

import sys
from bs4 import BeautifulSoup
import json

# Load environment variables from .env file
data_list=list()
load_dotenv()
confluence_domain =os.getenv('CONF_DOMAIN')
username =os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
# Set your Confluence details here
#space_key =  os.getenv('space_key')   # replace with your info

import requests
base_url=url =  os.getenv('BASE_URL')

def get_content(path):
    custom_url=""
    if path is not None:
        custom_url=path
    else:
         custom_url=base_url
    authorization = f"Basic {base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')}"

    headers = {
       "Authorization": authorization
     }

    response = requests.get(custom_url, headers=headers)
    return response
    #print(response.text)

def main():
    response=get_content(None)
    #print(type(response))
    json_resp=json.loads( response.text)
    json_resp['results']
    pages=list()
    list_dict=list()
    for resp in json_resp['results']:
        pages.append(resp['_links']['self'])

    for p in pages:
        cont=get_content(p+"?expand=body.view")
        inner_json_obj=json.loads(cont.text)
    
        print(inner_json_obj['title'])
        #print(type(inner_json_obj['body']))
        if inner_json_obj['body'] is None:
            print("*****************")
            continue
        if isinstance(inner_json_obj['body'], bytes):
            body_content = inner_json_obj['body'].decode('utf-8')  # Decode bytes to string
        elif isinstance(inner_json_obj['body'], str):
            body_content = inner_json_obj['body']
        else:
            print(type(inner_json_obj['body']['view']['value']))
            body_content=inner_json_obj['body']['view']['value'] 
            #raise ValueError("inner_json_obj['body'] must be a string or bytes.")
        
        soup = BeautifulSoup(body_content, 'html.parser')
        data_dict={"title":inner_json_obj['title'],"text":soup.text,"link":p}
        list_dict.append(data_dict)
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
    return list_dict

if __name__=="__main__":
   list_dict=main()
   df=pd.DataFrame(list_dict)
   csv=df.to_csv('final_text.csv')
