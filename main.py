# from git import Repo
# import os

# # ===== CONFIG =====
# repo_dir = r"D:\sep\0\6-Git_python\1"  # Local repo path
# remote_url = "https://github.com/Bha834/new123.git"  # GitHub repo URL
# branch_name = "main"  # Default branch
# file_to_add = "sample.py"  # File to create/add
# # ==================

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


# import os
# from git import Repo

# # ===== CONFIG =====
# repo_dir = r"D:\sep\0\6-Git_python\1"  # Local repo path
# branch_name = "main"
# # ==================

# # Initialize repo
# repo = Repo.init(repo_dir)

# # Stage all .py files in the repo_dir
# for root, dirs, files in os.walk(repo_dir):
#     py_files = [os.path.join(root, f) for f in files if f.endswith(".py")]
#     if py_files:
#         repo.index.add(py_files)
#         print(f"Staged files: {py_files}")

# # Commit (example commit message)
# commit_msg = "Add all Python files"
# repo.index.commit(commit_msg)
# print(f"Committed: {commit_msg}")

from git import Repo
import os

# ===== CONFIG =====
repo_dir = r"D:\sep\0\6-Git_python\1"  # Local repo path
remote_url = "https://github.com/Bha834/new123.git"  # GitHub repo URL
# ==================

# -------- Helper: Unique file handling --------
def get_unique_filename(folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

# -------- Initialize repo --------
repo = Repo.init(repo_dir)
print(f"Initialized repo at: {repo.working_tree_dir}")

# -------- Create a sample file safely --------
file_to_add = "sample.py"
unique_file = get_unique_filename(repo_dir, file_to_add)
file_path = os.path.join(repo_dir, unique_file)
with open(file_path, "w") as f:
    f.write("print('Hello GitPython!')")

print(f"File created: {unique_file}")

# -------- Stage all .py files --------
staged_files = []
for root, dirs, files in os.walk(repo_dir):
    py_files = [os.path.join(root, f) for f in files if f.endswith(".py")]
    if py_files:
        repo.index.add(py_files)
        staged_files.extend(py_files)

print(f"Staged files: {staged_files}")

# -------- Commit --------
commit_msg = input("Enter commit message: ")
repo.index.commit(commit_msg)
print(f"Committed: {commit_msg}")

# -------- Branch name input --------
branch_name = input("Enter branch name to push (default 'main'): ") or "main"
print(f"Using branch: {branch_name}")

# Ensure local branch matches user input
if repo.active_branch.name != branch_name:
    try:
        repo.git.branch('-M', branch_name)
        print(f"Local branch renamed to '{branch_name}'")
    except Exception as e:
        print("Error renaming branch:", e)

# -------- Setup remote --------
if "origin" not in [remote.name for remote in repo.remotes]:
    origin = repo.create_remote("origin", remote_url)
    print(f"Remote 'origin' added with URL: {remote_url}")
else:
    origin = repo.remotes.origin
    print("Remote 'origin' already exists")

# -------- Push to GitHub --------
try:
    push_info = origin.push(refspec=f"{branch_name}:{branch_name}", set_upstream=True)
    for info in push_info:
        if info.flags & info.ERROR:
            print("Push error:", info.summary)
        else:
            print("Push successful:", info.summary)
except Exception as e:
    print("Exception during push:", e)
