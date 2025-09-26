# from git import Repo
# import os

# repo_dir = r"D:\sep\26092025\3"  # Local repo path
# remote_url = "https://github.com/Bha834/demo-git.git"  # GitHub repo URL
# branch_name = "master"  # Default branch
# file_to_add = "sample.py"  # File to create/add


# # Create repo directory if not exists
# os.makedirs(repo_dir, exist_ok=True)

# # Initialize repo
# repo = Repo.init(repo_dir)
# print(f"Initialized repo at: {repo.working_tree_dir}")

# # Create a sample file
# file_path = os.path.join(repo_dir, file_to_add)
# with open(file_path, "w") as f:
#     f.write("print('Hello GitPython!')")

# # Stage the file
# repo.index.add([file_path])

# # Commit with user input message
# commit_msg = input("Enter commit message: ")
# repo.index.commit(commit_msg)
# print(f"Committed: {commit_msg}")

# # Setup remote
# if "origin" not in [remote.name for remote in repo.remotes]:
#     origin = repo.create_remote("origin", remote_url)
#     print(f"Remote 'origin' added with URL: {remote_url}")
# else:
#     origin = repo.remotes.origin
#     print("Remote 'origin' already exists")

# # Push to GitHub
# origin.push(refspec=f"{branch_name}:{branch_name}")
# print("Pushed to remote successfully!")

from git import Repo
import os

repo_dir = r"D:\sep\26092025\3"   # Tumhara project path
remote_url = "https://github.com/Bha834/demo-git.git"  # GitHub repo
branch_name = "master"  # Branch ka naam

# Initialize ya open repo
if not os.path.exists(os.path.join(repo_dir, ".git")):
    repo = Repo.init(repo_dir)
    print("New repo initialized")
else:
    repo = Repo(repo_dir)
    print("Existing repo opened")

# Stage all files (jitni files already present hain)
repo.git.add(A=True)   # "git add ."

# Commit with user input
commit_msg = input("Enter commit message: ")
if commit_msg.strip():   # Empty message avoid
    repo.index.commit(commit_msg)
    print(f"Committed: {commit_msg}")
else:
    print("No commit message given, skipping commit.")

# Setup remote
if "origin" not in [remote.name for remote in repo.remotes]:
    origin = repo.create_remote("origin", remote_url)
    print(f"Remote 'origin' added with URL: {remote_url}")
else:
    origin = repo.remotes.origin
    print("Remote 'origin' already exists")

# Push changes
origin.push(refspec=f"{branch_name}:{branch_name}")
print("Pushed to remote successfully!")
