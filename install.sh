#!/bin/bash

TARGET_DIR=~/Recipes/Voltaic_Recipe_Manager/

mkdir -p $TARGET_DIR

git clone https://github.com/VoltaicGRiD/Recipe_Manager $TARGET_DIR

chmod +x $TARGET_DIR/script.py

ln -s $TARGET_DIR/RecipeManager.py /usr/local/bin/recipe-manager
