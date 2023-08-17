import requests
import json

class GitHubIntegration:
    def __init__(self):
        pass

    def get_repository(self, owner, repo):
        url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(url)
        return response.json()

    def create_repository(self, name, description):
        url = "https://api.github.com/user/repos"
        payload = {
            "name": name,
            "description": description
        }
        response = requests.post(url, json=payload)
        return response.json()

    def add_file_to_repository(self, owner, repo, file_path, file_content):
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
        payload = {
            "message": "Add file",
            "content": file_content
        }
        response = requests.put(url, json=payload)
        return response.json()

