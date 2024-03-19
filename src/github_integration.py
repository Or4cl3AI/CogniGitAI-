import requests
import base64

class GitHubIntegration:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'token {self.token}'}

    def get_repository(self, owner, repo):
        url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_repository(self, name, description):
        url = "https://api.github.com/user/repos"
        payload = {
            "name": name,
            "description": description,
            "private": False
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def add_file_to_repository(self, owner, repo, file_path, file_content):
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
        content_base64 = base64.b64encode(file_content.encode()).decode()
        payload = {
            "message": "Add file",
            "content": content_base64
        }
        response = requests.put(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()
