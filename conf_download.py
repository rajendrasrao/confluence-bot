from atlassian import Confluence
import requests


confluence = Confluence(
    url='https://raorsingh.atlassian.net/',
    username="rao.rsingh@gmail.com",
    password="ATATT3xFfGF0l8e28FHhc9t65uNeBDUQ4UW3qateNYdbezY-SA7aUVerz7eTk8-tvkLl7zaTPac2sPOpGGHRMZVgV12AIXorI_l8o2oE6maDze-FdKU8TdBy5A4vQOjkD7j4rvDE9p_o7yUXtJdi4j0TYs10cvJk0TGDHvwX011PEro93uCfTyM=CB7F1186",
    cloud=True)

pages=confluence.get_all_pages_from_space(space=any,content_type="page")
print(pages)

attachments_container = confluence.get_attachments_from_content(page_id=12345678, start=0, limit=500)
attachments = attachments_container['results']
for attachment in attachments:
        fname = attachment['title']
        download_link = confluence.url + attachment['_links']['download']
        r = requests.get(download_link, auth=(confluence.username, confluence.password))
        if r.status_code == 200:
            with open(fname, "wb") as f:
                for bits in r.iter_content():
                    f.write(bits)
'''
url = 'https://raorsingh.atlassian.net/'
token="ATATT3xFfGF0l8e28FHhc9t65uNeBDUQ4UW3qateNYdbezY-SA7aUVerz7eTk8-tvkLl7zaTPac2sPOpGGHRMZVgV12AIXorI_l8o2oE6maDze-FdKU8TdBy5A4vQOjkD7j4rvDE9p_o7yUXtJdi4j0TYs10cvJk0TGDHvwX011PEro93uCfTyM=CB7F1186"

user_name="rao.rsingh@gmail.com"
headers={
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}
params = {
  "spaceKey": 'Documentation',
  "type": "page",
  "limit": 1000
}
response = requests.get(url, headers=headers, auth=(user_name, token))
print(response.text)
'''