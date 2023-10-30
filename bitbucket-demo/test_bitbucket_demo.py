
from bitbucket_demo  import get_repositories, get_commits_by_name_per_repository,\
get_average_time_for_commits_per_repository


def test_get_the_repositories():
    data = {'values': [{'name': 'gijs'}, {'name': 'captain jock strap'}], 'irrelevant': "ignore me"}
    result = get_repositories(data)
    assert result == ['gijs', "captain jock strap"]


def test_get_the_commits_by_name_per_repository():
    data = [{"author": {'name': 'tim.vandermeij'}}]
    repository = 'blue'
    name_commiter = 'tim.vandermeij'
    result = get_commits_by_name_per_repository(data, repository, name_commiter)
    assert result == "tim.vandermeij has contributed 1 commits to the blue repository"


def test_get_the_commits_by_name_per_repository_failed():
    data = []
    repository = 'blue'
    result = get_commits_by_name_per_repository(data, repository, 'tim.vandermeij')
    assert result == "tim.vandermeij contributed no commits to the blue repository"


def test_get_average_time_for_commits_per_repository():
    data = [{'committerTimestamp': 1679585391000, 'authorTimestamp': 1679571522000} ,
            {'committerTimestamp': 1679586391000, 'authorTimestamp': 1679571522000}]
    repository = 'blue'
    result = get_average_time_for_commits_per_repository(data, repository)
    assert result == 'the average time for commits in the blue repository is  3.98 hours'


def test_get_average_time_for_commits_per_repository_with_a_zero_as_sum_deduction():
    data = [{'committerTimestamp': 1679585391000, 'authorTimestamp': 1679571522000},
            {'committerTimestamp': 1679586391000, 'authorTimestamp': 1679571522000},
            {'committerTimestamp': 1679586391000, 'authorTimestamp': 1679586391000}] # these deduct to zero
    repository = 'blue'
    result = get_average_time_for_commits_per_repository(data, repository)
    assert result == 'the average time for commits in the blue repository is  3.98 hours'