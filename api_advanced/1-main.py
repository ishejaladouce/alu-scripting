#!/usr/bin/python3
"""
Test script for 1-top_ten.py
"""
import importlib.util
import sys

module_name = "1-top_ten"
file_path = "./1-top_ten.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
top_module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = top_module
spec.loader.exec_module(top_module)

if __name__ == "__main__":
    print("Testing an existing subreddit:")
    top_module.top_ten("programming")
    print("\nTesting a non-existent subreddit:")
    top_module.top_ten("this_subreddit_does_not_exist_12345")
