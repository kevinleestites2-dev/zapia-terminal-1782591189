import os, subprocess, sys

def run(cmd, cwd=None):
    print(f"Executing: {cmd}")
    try:
        res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, cwd=cwd)
        print(res)
        return res
    except subprocess.CalledProcessError as e:
        print(f"Error (Exit {e.returncode}):\n{e.output}")
        return None

# Find where we are
base_dir = os.getcwd()
print(f"Current directory: {base_dir}")

# Check if agent exists anywhere
agent_dir = None
for root, dirs, files in os.walk(base_dir):
    if "package.json" in files and "mercury-agent" in root:
        agent_dir = root
        break

if not agent_dir:
    print("Agent not found. Re-cloning...")
    run("git clone https://github.com/cosmicstack-labs/mercury-agent")
    # Search again
    for root, dirs, files in os.walk(base_dir):
        if "package.json" in files and "mercury-agent" in root:
            agent_dir = root
            break

if agent_dir:
    print(f"Agent found at: {agent_dir}")
    # Ensure it's built
    if not os.path.exists(os.path.join(agent_dir, "dist/index.js")):
        print("Building agent...")
        run("npm install && npm run build", cwd=agent_dir)
    
    # Show help
    run("node dist/index.js --help", cwd=agent_dir)
else:
    print("FATAL: Could not locate mercury-agent.")
