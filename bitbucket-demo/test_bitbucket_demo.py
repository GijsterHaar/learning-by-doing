import pytest
from bitbucket_demo  import get_repositories, get_commits_by_name_per_repository

def test_get_the_repositories():
    data = {'values': [{'name': 'gijs'}, {'name': 'captain jock strap'}], 'irrelevant': "ignore me"}
    result = get_repositories(data)
    assert result == ['gijs', "captain jock strap"]



def test_get_the_commits_by_name_per_repository():
    data = {'values': [{"author": {'name': 'Berend Botje'}}]}
    repository = 'blue'
    result = get_commits_by_name_per_repository(data, repository)
    assert result == "Berend Botje has contributed 1 commits to the blue repository"
