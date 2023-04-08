#!/usr/bin/bash

# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your SSH key to the agent and cache the passphrase for 1 hour
ssh-add -t 3600 -k ~/.ssh/id_ed25519 <<< "1fjieqmi12"

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
