import requests
print()

url = "https://bitbucket.detact.fox.local/rest"
path = "/api/latest/projects/CUSTOMER/repos"
headers = {'Authorization': 'Bearer Njc0MDE4NTkzMTg2OtA13694w2W0nl1ppGTm/O4C+Uc6'}

r = requests.get(url+path, headers=headers)
obj = r.json()

for i in obj['values']:
    repository = i['name']

    url = "https://bitbucket.detact.fox.local/rest"
    path = f"/api/latest/projects/CUSTOMER/repos/{repository}/commits"
    headers = {'Authorization': 'Bearer Njc0MDE4NTkzMTg2OtA13694w2W0nl1ppGTm/O4C+Uc6'}

    r = requests.get(url+path, headers=headers)

    obj = r.json()

    author = [d['author']['name'] for d in obj['values'] if d['author']['name'] == 'Berend Botje']
    print(f"{author[0]} has contributed {len(author)} commits to {repository} the repository")


print()