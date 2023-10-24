import requests
print()

def main():

    repo_obj = get_obj("/api/latest/projects/CUSTOMER/repos")
    repositories = get_repositories(repo_obj)
    name_author = input("Please enter the name you want to search for in the commits: ")

    print()
    for repository in repositories:
        path = f"/api/latest/projects/CUSTOMER/repos/{repository}/commits"
        obj = get_obj(path)
        # if obj['isLastPage'] != True:
        #     arguments['start'] = obj['nextPageStart']
        author = get_commits_by_name_per_repository(obj, repository, name_author)
        print(f"{author}")

    print()
    for repository in repositories:
        path = f"/api/latest/projects/CUSTOMER/repos/{repository}/commits"
        obj = get_obj(path)
        average_time = get_average_time_for_commits_per_repository(obj, repository)        
        print(f"{average_time}")
        
URL = "https://bitbucket.detact.fox.local/rest"
HEADERS = {'Authorization': 'Bearer Njc0MDE4NTkzMTg2OtA13694w2W0nl1ppGTm/O4C+Uc6'}

arguments = {'start': 0, 'limit': 10000}


def get_obj(path):
    r = requests.get(URL+path, arguments, headers=HEADERS)
    return r.json()

def get_repositories(repo_obj):
    repositories = [i['name'] for i in repo_obj['values']]
    return repositories

def get_commits_by_name_per_repository(obj, repository, name_author):
    author = [d['author']['name'] for d in obj['values'] if d['author']['name'] == name_author]
    if author == []:
        return f"{name_author} contributed no commits to the {repository} repository"
    return f"{author[0]} has contributed {len(author)} commits to the {repository} repository"

def get_average_time_for_commits_per_repository(obj, repository, ):
    for d in obj['values']:
        print(d['committerTimestamp'])
    time_spend_list = [(d['committerTimestamp'] - d['authorTimestamp']) for d in obj['values']]
    time_spend_list = set(time_spend_list)
    time_spend_list.remove(0)
    average_time = sum(time_spend_list) / len(time_spend_list)
    return f"the average time for commits in the {repository} repository is {average_time // 1000 // 60 // 60} hours"

if __name__ == '__main__':
    main()

print()
