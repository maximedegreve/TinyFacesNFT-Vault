#!/bin/bash

# Set the name of the branch you want to push to
BRANCH="feature/kickoff"

# Count the number of files in the directory
FILES_COUNT=$(ls -1 | wc -l)

# Loop through the files, pushing 10 at a time
for (( i=1; i<=$FILES_COUNT; i+=10 )); do
  # Add the next 10 files to the commit
  git add $(ls -1 | head -n $i | tail -n 10)

  # Commit the changes with a message containing the range of files
  git commit -m "Pushing files $i to $(($i+9))"

  # Push the changes to the branch
  git push origin $BRANCH
done