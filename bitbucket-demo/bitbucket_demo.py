import requests
from pprint import pprint
print()



URL = "https://bitbucket.detact.fox.local/rest"
HEADERS = {'Authorization': 'Bearer Njc0MDE4NTkzMTg2OtA13694w2W0nl1ppGTm/O4C+Uc6'}

def main():

    repo_obj = get_obj("/api/latest/projects/CUSTOMER/repos")
    repositories = get_repositories(repo_obj)


    for repository in repositories:
        path = f"/api/latest/projects/CUSTOMER/repos/{repository}/commits"
        
        obj = get_obj(path)

        author = get_commits_by_name_per_repository(obj, repository)
        print(author)


def get_obj(path):
    r = requests.get(URL+path, headers=HEADERS)
    return r.json()

def get_repositories(repo_obj):
    repositories = []
    for i in repo_obj['values']:
        repositories.append(i['name'])
    return repositories

def get_commits_by_name_per_repository(obj, repository):
    author = [d['author']['name'] for d in obj['values'] if d['author']['name'] == 'Berend Botje']
    return f"{author[0]} has contributed {len(author)} commits to the {repository} repository"
    


if __name__ == '__main__':
    main()

print()