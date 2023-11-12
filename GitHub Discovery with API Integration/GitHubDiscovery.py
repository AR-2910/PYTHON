# Project using GitHub API to retrieve information of a user
import requests

# Input GitHub username
username = input("GitHub Username: ")

# GitHub API URLs for user repositories and pull requests
url_1 = f"https://api.github.com/users/{username}/repos"
url_2 = f"https://api.github.com/search/issues?q=is:pr+author:{username}"

# Send HTTP GET requests to GitHub API
response_1 = requests.get(url_1)
response_2 = requests.get(url_2)

# Process user repositories
if response_1.status_code == 200:
    repositories = response_1.json()
    print(f"User: {username} has the following repositories:")
    for repo in repositories:
        print(repo["name"])
else:
    # Print error message if unable to retrieve repositories
    print(f"Failed to retrieve repositories for {username}, error code: {response_1.status_code}")

# Process user pull requests
if response_2.status_code == 200:
    pull_requests = response_2.json()
    print(f"User: {username} has made the following Pull Requests:")
    for pr in pull_requests["items"]:
        repo_name = pr["repository_url"]
        pr_title = pr["title"]
        print(f"Repository: {repo_name} , PR Title: {pr_title}")
else:
    # Print error message if unable to retrieve pull requests
    print(f"Failed to retrieve pull requests for {username}, error code: {response_2.status_code}")
