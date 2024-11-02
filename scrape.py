import requests
import csv
import hashlib
import os 
from tqdm import tqdm
import json
from sec import TOKE

# GitHub authentication token (replace 'YOUR_TOKEN' with your actual token)
TOKEN = TOKE
HEADERS = {'Authorization': f'token {TOKEN}'}

# GitHub API endpoints
BASE_URL = "https://api.github.com"

if not os.path.exists("cache"):
    os.makedirs("cache")


def cached_get_det(url, headers={}):
    filename = hashlib.md5(url.encode()).hexdigest() + ".json"
    path = os.path.join("cache", filename)
    if not os.path.exists(path):
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(path, 'w', encoding='utf-8', errors='replace') as f:
            f.write(response.text)
    with open(path, 'r', encoding='utf-8', errors='ignore' ) as f:
        return f.read()


def fetch_users():
    user_login = []
    # Fetching users with at least 100 followers in Austin
    location="Austin"
    min_followers=100
    for i in tqdm(list(range(1, 6))):
        url = f"{BASE_URL}/search/users?q=location:{location}+followers:>={min_followers}&page={i}&per_page=100"
        response = cached_get_det(url, headers=HEADERS)
        if not response:
            print("Response is empty or contains only whitespace.")
        else:
            try:
                parsed_response = json.loads(response)  # Attempt to parse the JSON
                if "items" in parsed_response and parsed_response["items"]:
                    for user in parsed_response["items"]:
                        user_login.append(user["login"])
                else:
                    pass
            except json.JSONDecodeError:
                pass
    return user_login

logins = fetch_users()
print("|")
users_details = []

def clean_company_name(company_name):
    if company_name:
        return company_name.strip().lstrip('@').upper()
    return None

def fetch_user_details(logins):
    for user_login in tqdm(logins):
        url = f"{BASE_URL}/users/{user_login}"
        response = cached_get_det(url, headers=HEADERS)
        if not response:
            print("Response is empty or contains only whitespace.")
        else:
            try:
                user_data = json.loads(response)
                user_details = {
                    "login" : user_data["login"],
                    "name"  : user_data["name"],
                    "company" : clean_company_name(user_data["company"]),
                    "location" : user_data["location"],
                    "email" : user_data["email"],
                    "hirable": user_data["hireable"],
                    "bio" : user_data["bio"],
                    "public_repos" : user_data["public_repos"],
                    "followers" : user_data["followers"],
                    "following" : user_data["following"],
                    "created_at" : user_data["created_at"]
                }
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON for user {user_login} - {e}")
                continue

        users_details.append(user_details)
        # time.sleep(1)


fetch_user_details(logins)

def fetch_repositories(logins):
    repos = []
    
    for login in tqdm(logins):
        page = 1
        repos_for_login = []
        
        while True:
            url = f"{BASE_URL}/users/{login}/repos?page={page}&per_page=100&sort=pushed"
            response = cached_get_det(url, headers=HEADERS)
            repo_data = json.loads(response)

            if not repo_data:
                break
            
            for repo in repo_data:
                if len(repos_for_login) < 500:
                    repos_for_login.append({
                        "login": login,
                        "full_name": repo["full_name"],
                        "created_at": repo["created_at"],
                        "stargazers_count": repo["stargazers_count"],
                        "watchers_count": repo["watchers_count"],
                        "language": repo["language"],
                        "has_projects": repo["has_projects"],
                        "has_wiki": repo["has_wiki"],
                        "license_name": repo["license"]["key"] if repo.get('license') else None
                    })
                else:
                    print(f"Reached limit of 500 repositories for user {login}. Skipping further repositories.")
                    break
            
            if len(repos_for_login) >= 500:
                print("if idk")
                break
            
            page += 1  

        repos.extend(repos_for_login)
        # time.sleep(1)

    return repos

to_be_saved_repo = fetch_repositories(logins)

def save_to_csv(users_data, repos_data):
    with open("users.csv", mode="w", newline='', encoding="utf-8") as users_file:
        user_writer = csv.DictWriter(users_file, fieldnames=users_data[0].keys())
        user_writer.writeheader()
        user_writer.writerows(users_data)

    with open("repositories.csv", mode="w", newline='', encoding="utf-8") as repos_file:
        repo_writer = csv.DictWriter(repos_file, fieldnames=repos_data[0].keys())
        repo_writer.writeheader()
        repo_writer.writerows(repos_data)

save_to_csv(users_details, to_be_saved_repo)