import os, subprocess, sys

def run(cmd, cwd=None):
    print(f"Executing: {cmd} in {cwd or 'current dir'}")
    try:
        res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, cwd=cwd)
        print(res)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error (Exit {e.returncode}):\n{e.output}")
        return False

# 1. Locate the agent
base_dir = os.getcwd()
agent_dir = os.path.join(base_dir, "mercury-agent")

if not os.path.exists(agent_dir):
    print("Agent not found, rebuilding...")
    run("git clone https://github.com/cosmicstack-labs/mercury-agent")
    run("npm install && npm run build", cwd=agent_dir)

# 2. Run the transfer command
# Note: User needs to provide the real TO address
to_address = sys.argv[1] if len(sys.argv) > 1 else "DLos..." # Placeholder

cmd = f"node dist/index.js transfer --from 8xQ77uxSjvmfcjReEGAWydpH4PBxUoXx6p46GEpMtZg1 --to {to_address} --amount 31.50"
run(cmd, cwd=agent_dir)
