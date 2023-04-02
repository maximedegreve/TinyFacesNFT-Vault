import subprocess
import os

# Find all changed or untracked files in the current directory and its subdirectories
output = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=all", "--ignore-submodules=dirty"])
files = [line.split(" ")[-1].strip() for line in output.decode("utf-8").split("\n") if line.startswith(" M") or line.startswith("??")]

print ("📁 Total new or changed files detected: ", len(files))

for file in files:
    # Push the file to the branch
    print ("🔄 Syncing file:", file)
    subprocess.run(["git", "add", file])
    subprocess.run(["git", "commit", "-m", f"Pushing {os.path.basename(file)}"])
    subprocess.run(["git", "push"])

