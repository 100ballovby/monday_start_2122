import json as j
import requests as r
# JSON - JavaScript Object Notation

response = r.get('https://api.github.com/users/100ballovby')
user = j.loads(response.text)

#print(user)
#print(user['html_url'])
response2 = r.get(user['repos_url'])
repos = j.loads(response2.text)

sto_ballov_rep_py = {}
for repo in repos:  # для каждого репозитория
    if repo['language'] == 'Python':  # если основной язык Python
        sto_ballov_rep_py[repo['name']] = repo['svn_url']

print(sto_ballov_rep_py)
