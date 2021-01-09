#!/bin/bash/

#https://www.taniarascia.com/how-to-create-and-use-bash-scripts/
echo
echo This will add everything, commit and push
echo
read -r -p 'Enter Commit message: ' desc  # prompt user for commit message
git add .                           # track all files
#git add -u                          # track deletes
git commit -m "$desc"               # commit with message
git push
