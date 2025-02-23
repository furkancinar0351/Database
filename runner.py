import subprocess

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    run_script("bot.py")
    run_script("modal.py")
