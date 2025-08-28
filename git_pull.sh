#!/bin/bash

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_proxmox_websites_server
ssh-add -l
ssh -T git@github.com

git pull
