import os
import subprocess

def run_command(commands):
    result = subprocess.run(commands, stdout=subprocess.PIPE)
    output = str(result.stdout.decode("utf-8"))
    return output

def ls_a():
    return run_command(["ls", "-a"])

def pwd():
    return run_command(["pwd"])

def cd(path):
    os.chdir(path)
