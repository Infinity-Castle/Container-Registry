import hashlib
from importlib.resources import path
import os
import sys
import pathlib as Path
from xml.etree.ElementTree import tostring

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def update_hash_file(file_path, hash_value):
    with open(file_path, "w") as file:
        file.write(hash_value)

def store_changed_dockerfile(file_path, dockerfile_location):
    with open(file_path, "a") as file:
        file.write(dockerfile_location + "\n")

def check_dockerfile_hashes(directory, changed_dockerfiles_file):
    for root, dirs, files in os.walk(directory):
        if "Dockerfile" in files and "hashfile" in files:
            dockerfile_path = os.path.join(root, "Dockerfile")
            hashfile_path = os.path.join(root, "hashfile")

            existing_hash = None
            with open(hashfile_path, "r") as file:
                existing_hash = file.read().strip()

            current_hash = calculate_sha256(dockerfile_path)

            if existing_hash == current_hash:
                print(f"Dockerfile in {root} has not changed.")
            else:
                print(f"Dockerfile in {root} has been updated.")
                update_hash_file(hashfile_path, current_hash)
                store_changed_dockerfile(changed_dockerfiles_file, dockerfile_path)

# Specify the root directory where Dockerfiles are located
root_directory = os.environ['GITHUB_WORKSPACE'] + "/wargames4.0"
# Specify the path to the text file to store changed Dockerfile locations
changed_dockerfiles_file = os.environ['GITHUB_WORKSPACE'] + "/.github/updates/linuxdiary-4.0.txt"
# check_dockerfile_hashes(root_directory, changed_dockerfiles_file)
