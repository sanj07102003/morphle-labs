from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Full Name (Replace with your actual name)
    full_name = "sanjana balasubramanya"
    
    # System Username
    username = os.getlogin(sanjana@07)
    
    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    # Top command output
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
