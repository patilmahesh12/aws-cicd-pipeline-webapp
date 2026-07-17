import paramiko
import os
import io

# Securely grab the secrets from GitHub Actions environment
HOST = os.getenv("EC2_HOST")
USERNAME = os.getenv("EC2_USERNAME")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

print(f"Starting real deployment to {HOST}...")

# Load the private key securely from memory (no files needed!)
key = paramiko.RSAKey.from_private_key(io.StringIO(PRIVATE_KEY))

# Set up the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the EC2 server
client.connect(hostname=HOST, username=USERNAME, pkey=key)

# The commands to run on the EC2 server
commands = [
    "cd /usr/share/nginx/html && git pull origin main && systemctl restart nginx"
]

# Execute command
for command in commands:
    print(f"Executing: {command}")
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    error = stderr.read().decode()
    if error:
        print(f"Error: {error}")

client.close()
print("Deployment Completed Successfully!")
