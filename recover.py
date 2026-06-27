import os, subprocess, sys

def run(cmd):
    print(f"Executing: {cmd}")
    try:
        res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        print(res)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
        return False

# Clean start
if os.path.exists("mercury-agent"):
    run("rm -rf mercury-agent")

if not run("git clone https://github.com/cosmicstack-labs/mercury-agent"):
    sys.exit(1)

# The repo structure might have requirements inside mercury-agent/
# Let's find where requirements.txt actually is
print("Searching for requirements.txt...")
req_path = None
for root, dirs, files in os.walk("mercury-agent"):
    if "requirements.txt" in files:
        req_path = os.path.join(root, "requirements.txt")
        break

if req_path:
    print(f"Found requirements at: {req_path}")
    run(f"pip install -r {req_path}")
    # Run the module from the correct directory
    os.chdir(os.path.dirname(req_path))
    run("python3 -m mercury_agent --version")
else:
    print("Could not find requirements.txt in the repo.")
    # List files to help debug
    run("find mercury-agent -maxdepth 2")
