#!/bin/bash

# This script sets up the ability to use ChatGPT as an API
# Directions from: https://github.com/mmabrouk/chatgpt-wrapper
# Accurate as of 2022-02-19

pip install git+https://github.com/mmabrouk/chatgpt-wrapper
playwright install firefox
chatgpt install
