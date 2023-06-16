import os
import hashlib

directory = os.environ['GITHUB_WORKSPACE'] + "/wargames4.0"
updateFile = None

def check(hash,dockerfile):
    print("Checking " + dockerfile,end='')
    sha256_hash = hashlib.sha256()

    with open(dockerfile,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    
    if(not os.path.exists(hash)):
        open(hash, 'w+')
    
    with open(hash, 'r') as file:
        fileHash = file.read().replace('\n', '')

        fileHash = fileHash.split(' ')[0]

        if(fileHash==sha256_hash.hexdigest()):
            print(" - Not Modified")
            return 
        else:
            print(" - Modified")
            updateFile.write(dockerfile+" "+hash+"\n")

def process(parent_dir, file):
    for filename in os.listdir(file):
        f = os.path.join(file, filename)
        if not os.path.isfile(f):
            process(file, f)
        elif filename=="Dockerfile":
            check(file+"/hash", f)

def main():
    global updateFile
    updateFile = open(os.environ['GITHUB_WORKSPACE'] + "/wargames4.0", "w+")
    process(directory, directory)
    updateFile.close()

if __name__=="__main__":
    main()
