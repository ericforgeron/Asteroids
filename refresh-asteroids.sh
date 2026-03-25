#!/bin/bash

cd ~
FOLDER="Asteroids"
REPO="https://github.com/ericforgeron/Asteroids.git"

if [ -d "$FOLDER" ]; then
    echo "Updating existing Asteroids folder..."
    cd "$FOLDER"
    git fetch origin
    git reset --hard origin/main 2>/dev/null || git reset --hard origin/master
else
    echo "Cloning fresh Asteroids repo..."
    git clone "$REPO"
    cd "$FOLDER"
fi

echo "Asteroids is now fully synced with GitHub."
