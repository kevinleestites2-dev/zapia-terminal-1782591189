import os
import subprocess
import sys

def run(cmd):
    print(f"Executing: {cmd}")
    try:
        res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        print(res)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
        return False

# Step 1: Clean and Clone
if os.path.exists("mercury-agent"):
    run("rm -rf mercury-agent")

if not run("git clone https://github.com/cosmicstack-labs/mercury-agent"):
    sys.exit(1)

# Step 2: Install
os.chdir("mercury-agent")
if not run("pip install -r requirements.txt"):
    # Try a more forceful install if it fails
    run("pip install --user -r requirements.txt")

# Step 3: Verify
run("python3 -m mercury_agent --version")
