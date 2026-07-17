import paramiko
import os
import io

# Get secrets from GitHub Actions
HOST = os.getenv("EC2_HOST")
USERNAME = os.getenv("EC2_USERNAME")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Set up SSH
key = paramiko.RSAKey.from_private_key(io.StringIO(PRIVATE_KEY))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect
client.connect(hostname=HOST, username=USERNAME, pkey=key)

# Execute deployment command
command = "cd /usr/share/nginx/html && sudo git pull origin main && sudo systemctl restart nginx"
print(f"Executing: {command}")
stdin, stdout, stderr = client.exec_command(command)

print(stdout.read().decode())
error = stderr.read().decode()
if error:
    print(f"Error: {error}")

client.close()
print("Deployment Completed!")
