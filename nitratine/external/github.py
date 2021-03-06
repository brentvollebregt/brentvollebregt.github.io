from dataclasses import dataclass
from typing import Optional, List

import requests

from ..config import site_config


@dataclass
class GitHubRepository:
    """ Details of a GitHub repository """
    name: str
    full_name: str
    private: bool
    html_url: str
    description: str
    fork: bool
    url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    forks_count: int
    open_issues_count: int
    license: Optional[str]
    forks: int
    open_issues: int
    watchers: int
    default_branch: str

    @staticmethod
    def from_json(json: dict):
        return GitHubRepository(
            json["name"],
            json["full_name"],
            json["private"],
            json["html_url"],
            json["description"],
            json["fork"],
            json["url"],
            json["created_at"],
            json["updated_at"],
            json["pushed_at"],
            json["git_url"],
            json["size"],
            json["stargazers_count"],
            json["watchers_count"],
            json["language"],
            json["forks_count"],
            json["open_issues_count"],
            json["license"],
            json["forks"],
            json["open_issues"],
            json["watchers"],
            json["default_branch"],
        )


def __request_for_github_user_repos(github_username: str):
    """ Get details about the repositories associated with a user """
    response = requests.get(f'https://api.github.com/users/{github_username}/repos')
    github_repos_request_data = response.json()

    available_repos = [
        GitHubRepository.from_json(r)
        for r in github_repos_request_data
    ]

    sorted_available_repos = sorted(
        available_repos,
        key=lambda x: x.stargazers_count,
        reverse=True
    )

    return sorted_available_repos


__github_user_repos_cache = None


def get_github_user_repos() -> List[GitHubRepository]:
    """ Get the cached github_user_repos or make a request to get them and return them """
    global __github_user_repos_cache

    if __github_user_repos_cache is None:
        __github_user_repos_cache = __request_for_github_user_repos(
            github_username=site_config.github_username
        )

    return __github_user_repos_cache
