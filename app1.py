from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your full name
    full_name = "sanjana balasubramanya gowda"
    
    # System Username
    username = os.getlogin(sanjana@0710)
    
    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    # Fetch top command output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")
    
    return f"""
    <h1>System Stats</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
