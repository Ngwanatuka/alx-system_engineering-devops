#!/usr/bin/bash

# Prompt user for commit message
read -p "Enter commit message: " message

# Add changes to Git staging area
sudo git add .

# Commit changes with commit message
sudo git commit -m "$message"

# Push changes to remote repository
sudo git push

# Stop the SSH agent
ssh-agent -k
