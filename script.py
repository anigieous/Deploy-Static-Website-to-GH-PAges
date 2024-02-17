import os
import shutil
import subprocess
from git import Repo
from github import Github

# Get environment variables
token = os.getenv('GITHUB_TOKEN')
repo_name = os.getenv('REPO')

# Initialize GitHub API client
g = Github(token)
repo = g.get_repo(repo_name)

# Clone the repository
Repo.clone_from(repo.clone_url, 'repo')

# Change the current working directory to the cloned repository
os.chdir('repo')

# Step 1: Setup pages
# This assumes that you have a repository cloned locally and you're currently in its root directory
# Create a new branch if it doesn't exist and switch to it
subprocess.run(["git", "checkout", "-b", "gh-pages"], check=True)

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Step 2: Upload artifacts
# This assumes that you have a directory called 'output' that contains the files you want to upload
# Use ghp-import tool to move files into the gh-pages branch
os.environ['GH_TOKEN'] = token
subprocess.run(["ghp-import", "-n", "-p", "-f", "output"], check=True)

# Step 3: Deploy to GitHub Pages
# Push the changes to remote gh-pages branch
subprocess.run(["git", "push", "-f", "origin", "gh-pages"], check=True)

user = repo.owner.login
page_url = f"https://{user}.github.io/{repo_name}"

# Update the repository description with the page URL
repo.edit(homepage="page_url")

# Clean up the cloned repository
shutil.rmtree('repo')

print("::set-output name=page_url::" + page_url)
