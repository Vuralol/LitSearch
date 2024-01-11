import requests
from urllib.parse import quote
import json

with open('config.json', 'r') as f:
  data = json.load(f)

api_key = data['API-Key']
api_insttoken = data['API-Insttoken']

print(api_key)
print(api_insttoken)
api_url = f'https://api.elsevier.com/content/search/scopus'
# api_url_Textsearch = 'https://api.elsevier.com/content/search/scopus'

#api_url_title = https://api.elsevier.com/content/serial/title
#api_url_issn = https://api.elsevier.com/content/serial/title/issn/%7Bissn%7D
#api_url_author = https://api.elsevier.com/content/author
# api_url_author_id= https://api.elsevier.com/content/ author/author_id/{author_id} AUTHROSEARCH API maybe
# api_url_subject = https://api.elsevier.com/content/subject/scopus
# api_ul_subject_scidir = https://api.elsevier.com/content/subject/scidir



headers =\
    {'Accept': 'application/json',
   'X-ELS-APIKey': {api_key},
   'X-ELS-Insttoken': {api_insttoken}
    }

keyword = input("Enter the keyword: ")
author = input("Enter the author's name: ")

processed_keyword = quote(keyword)
processed_author = quote(author)


query = {
 'query': f'AUTHOR({processed_author}) AND TITLE-ABS-KEY({processed_keyword})',
 'httpAccept': 'application/json'
}

#URL-encode the query string
encoded_query = quote(query['query'])

# Update the query with the URL-encoded string
query['query'] = encoded_query



response = requests.get(api_url, params=query, headers=headers)

if response.status_code == 200:
  print(f"Status code: {response.status_code}")
  print(f"Response body: {response.json()}")
else:
  print(f"Request failed with status code: {response.status_code}")