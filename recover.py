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

# Ensure we are in the right spot
base_dir = os.getcwd()
agent_dir = os.path.join(base_dir, "mercury-agent")

if os.path.exists(agent_dir):
    os.chdir(agent_dir)
    # Check if dist/index.js exists
    if os.path.exists("dist/index.js"):
        print("SUCCESS: found dist/index.js")
        # Run the help command to see available commands
        run("node dist/index.js --help")
    else:
        print("dist/index.js not found. Listing dist contents:")
        run("ls -R dist")
else:
    print("mercury-agent directory not found.")
