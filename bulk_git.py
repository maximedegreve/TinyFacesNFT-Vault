import subprocess
import os

# Set the name of the branch you want to push to
BRANCH = "feature/kickoff"

# Find all changed or untracked files in the current directory and its subdirectories
output = subprocess.check_output(["git", "status", "--porcelain"])
files = [line.split(" ")[-1].strip() for line in output.decode("utf-8").split("\n") if line.startswith(" M") or line.startswith("??")]

print ("👀 New or changed files detected: ", files)

for file in files:
    # Push the file to the branch
    print ("🔄 Syncing file:", file)
    subprocess.run(["git", "add", file])
    subprocess.run(["git", "commit", "-m", f"Pushing {os.path.basename(file)}"])
    subprocess.run(["git", "push", "origin", BRANCH])
