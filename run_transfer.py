import os, subprocess, sys

def run(cmd, cwd=None):
    print(f"Executing: {cmd}")
    try:
        res = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, cwd=cwd)
        print(res)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error (Exit {e.returncode}):\n{e.output}")
        return False

base_dir = os.getcwd()
agent_dir = os.path.join(base_dir, "mercury-agent")

# Just list commands to see the correct syntax
print("Checking Mercury Agent commands...")
run("node dist/index.js --help", cwd=agent_dir)
