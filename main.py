# Try to handle imports to make it work no matter what the set up of the computer is
try:
    import tkinter
    import time
    import os
    import subprocess
    import base64
except ImportError:
    os.system('pip install tkinter subprocess base64')
    time.sleep(1)
    import tkinter
    import time
    import os
    import subprocess
    import base64

# Functions

import subprocess

import subprocess

def run_sudo_brew(command):
    try:
        # Open a file descriptor that mimics pressing the Enter key
        devnull = open('/dev/null', 'w')
        
        # Add a delay before executing the command
        time.sleep(3)
        
        # Execute the command
        process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check if sudo password is prompted
        sudo_prompt = False
        for line in iter(process.stderr.readline, b''):
            if b'[sudo] password' in line:
                sudo_prompt = True
                break
        
        if sudo_prompt:
            # Path to the file containing the sudo password
            password_file = "/Users/Shared/driver/pw.txt"
            
            # Read the sudo password from the file
            with open(password_file, 'r') as file:
                sudo_password = file.read().strip()

            # Send the sudo password to the process
            process.stdin.write(f"{sudo_password}\n".encode())
            process.stdin.flush()
        
        # Wait for the command to finish
        output, error = process.communicate()
        
        if process.returncode != 0:
            print(f"Error executing command: {error.decode('utf-8')}")
        else:
            print("Command executed successfully.")
            print(output.decode('utf-8'))
    except FileNotFoundError:
        print(f"Error: Command '{command}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def run_sudo(command):
    # Path to the file containing the sudo password
    password_file = "/Users/Shared/driver/pw.txt"
    
    try:
        # Read the sudo password from the file
        with open(password_file, 'r') as file:
            sudo_password = file.read().strip()

        # Build the sudo command
        sudo_command = f"echo '{sudo_password}' | sudo -S {command}"

        # Execute the sudo command
        process = subprocess.Popen(sudo_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode != 0:
            print(f"Error executing command with sudo: {error.decode('utf-8')}")
        else:
            print("Command executed successfully with sudo.")
            print(output.decode('utf-8'))
    except FileNotFoundError:
        print(f"Error: Password file '{password_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")






# Install brew
print("Installing brew...")
brew_install = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
run_sudo_brew(brew_install)

# Install tor
print("Installing tor...")
os.system("brew install tor")

# Install torsocks
print("Installing torsocks...")
os.system("brew install torsocks")

# Start tor
print("Starting tor...")
os.system("tor")
