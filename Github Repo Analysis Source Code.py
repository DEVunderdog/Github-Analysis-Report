import requests
import plotly.express as px
import contextlib

# The API Link must design in the following way:
""" https://api.github.com/search/repositories?q=language:language_type&sort=sorting_factor."""

# Processing An API response:



url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
p_my_headers = {'Accept': 'application/vnd.github.v3+json'} # Requesting to use this version
r = requests.get(url, headers = p_my_headers) # Making call to API
print(f"Status Code: {r.status_code}") # Status Code 200 means successful response
response_dict = r.json() # Store API response in a variable

repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Making Visualization

pro_fig = px.bar(x = repo_names, y = stars, labels= dict(x = "Repo's Names", y = "Stars"))
pro_fig.write_image("Analysis Report/python.webp")

# Storing in Text File
path = "Github Repo Analysis python.txt"
with open(path, 'w') as f:
    with contextlib.redirect_stdout(f):
        for repo_dict in repo_dicts:
            print(f"\nName: {repo_dict['name']}")
            print(f"Owner: {repo_dict['owner']['login']}")
            print(f"Stars: {repo_dict['stargazers_count']}")
            print(f"Repository: {repo_dict['html_url']}")






