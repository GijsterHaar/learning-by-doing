import requests
print()

def main():
    arguments = {'limit': 15}
    # we call the get obj function with the extension of the path into the customer repos
    repo_obj = get_obj("/api/latest/projects/CUSTOMER/repos", arguments)
    repositories = get_repositories(repo_obj)
    name_committer = input("Please enter the name you want to search for in the commits: ")

    # line 16 - 28 all use the get_commit_list function to first:
    # - get commits by name per repository
    # - get average time for commits per repository
    # - get personal average for cvommits per repository
    print()
    for repository in repositories:
        committer = get_commits_by_name_per_repository(get_commit_list(repository), repository, name_committer)
        print(f"{committer}")

    print()
    for repository in repositories:
        average_time = get_average_time_for_commits_per_repository(get_commit_list(repository), repository)        
        print(f"{average_time}")
    
    print()
    for repository in repositories:
        personal_average_time = get_personal_average_per_repository(get_commit_list(repository), repository, name_committer)
        print(personal_average_time)
    
    

# URL and HEADERS are used as such in whole programm so made them CONSTANTS
URL = "https://bitbucket.detact.fox.local/rest"
HEADERS = {'Authorization': 'Bearer Njc0MDE4NTkzMTg2OtA13694w2W0nl1ppGTm/O4C+Uc6'}

# get the customer repo object, it takes the URL en HEADERS from the constants
# the path en arguments from the function call
def get_obj(path, arguments):
    r = requests.get(URL+path, arguments, headers=HEADERS)
    return r.json()

# this function only gets a list with all the names of the repositories
# to itterate over to extract data per or for all repos
def get_repositories(repo_obj):
    repositories = [i['name'] for i in repo_obj['values']]
    return repositories

# this function gets a list of all commits per repository, and extends
# that list every time it goes through the while loop until it reaches the last page
def get_commit_list(repository):
    arguments = {'limit': 100}
    path = f"/api/latest/projects/CUSTOMER/repos/{repository}/commits"
    obj = get_obj(path, arguments)
    commit_list = obj['values']
    while obj['isLastPage'] != True:
        arguments['start'] = obj['nextPageStart']
        obj = get_obj(path, arguments)
        commit_list.extend(obj['values'])
    return commit_list

# this function gets the number of commits per repository per person/committer
def get_commits_by_name_per_repository(commit_list, repository, name_committer):
    committer = [commit['author']['name'] for commit in commit_list if commit['author']['name'] == name_committer]
    if committer == []:
        return f"{name_committer} contributed no commits to the {repository} repository"
    return f"{name_committer} has contributed {len(committer)} commits to the {repository} repository"

# this function deducts the author timestamp (when ticket was created) from committer timestamp (time of commit)
# Then divide by 1000 to get rid of milliseconds, by 60 to turn seconds into minutes, and by 60 to turn minutes into hours
# formatted two decimals behind the comma
def get_average_time_for_commits_per_repository(commit_list, repository, ):
    time_spend_list = [(commit['committerTimestamp'] - commit['authorTimestamp']) // 1000 // 60 / 60 for commit in commit_list \
                        if (commit['committerTimestamp'] - commit['authorTimestamp']) != 0]
    average_time = sum(time_spend_list) / len(time_spend_list)
    return f"the average time for commits in the {repository} repository is {average_time:.2f} hours"

# this function is a combination of the previous two, here we get a personal average for commits per repository
def get_personal_average_per_repository(commit_list, repository, name_committer):
    time_spend_list = [(commit['committerTimestamp'] - commit['authorTimestamp']) // 1000 // 60 / 60 for commit in commit_list \
                        if (commit['committerTimestamp'] - commit['authorTimestamp']) != 0 \
                            and commit['author']['name'] == name_committer]
    if time_spend_list == []:
        return f"{name_committer} contributed no commits to the {repository} repository"
    average_time = sum(time_spend_list) / len(time_spend_list)
    return f"the average time for commits in the {repository} repository for {name_committer} is {average_time:.2f} hours"


if __name__ == '__main__':
    main()

print()
