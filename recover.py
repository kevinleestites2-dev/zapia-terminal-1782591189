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

# It's a Node project (has package.json)
os.chdir("mercury-agent")
if run("npm install"):
    run("npm run build")
    print("SUCCESS: Mercury Agent is built and ready.")
else:
    print("FAILED: Could not install dependencies.")
