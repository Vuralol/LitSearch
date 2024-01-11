import requests

api_key = 'e06b8d66547acd3743143196a83a2d58'
scopus_id = '84980079927'

api_url = f'https://api.elsevier.com/content/search/scopus/{scopus_id}'
# api_url_Textsearch = 'https://api.elsevier.com/content/search/scopus'

#api_url_title = https://api.elsevier.com/content/serial/title
#api_url_issn = https://api.elsevier.com/content/serial/title/issn/%7Bissn%7D
#api_url_author = https://api.elsevier.com/content/author
# api_url_author_id= https://api.elsevier.com/content/ author/author_id/{author_id} AUTHROSEARCH API maybe
# api_url_subject = https://api.elsevier.com/content/subject/scopus
# api_ul_subject_scidir = https://api.elsevier.com/content/subject/scidir



headers =\
    {
    'Accept': 'application/json',
   'X-ELS-APIKey': 'e06b8d66547acd3743143196a83a2d58',
   'X-ELS-Insttoken': '6441054b64ac034be8481aaea2b77707'
    }

query = {'query': 'TITLE-ABS-KEY(Global warming)'}
response = { requests.get(api_url, params=query, headers=headers)}

print(f"Status code: {response.status_code}")
print(f"Response body: {response.json()}")