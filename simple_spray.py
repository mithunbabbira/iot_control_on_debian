import requests
import json
import subprocess
import time

IPHONE_MAC = "50:B1:27:38:56:30"  # iPhone's Bluetooth MAC

def spray_room_freshener():
    """
    Simple function to trigger room freshener spray via NodeMCU
    """
    url = "https://io.adafruit.com/api/v2/babbiramithun/feeds/command/data"
    headers = {
        'X-AIO-Key': 'REPLACE_WITH_YOUR_KEY',  # Set your real key locally on the Pi, do not push to GitHub
        'Content-Type': 'application/json'
    }
    data = {"value": "SPRAY"}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("✅ Room freshener sprayed!")
            return True
        else:
            print(f"❌ Failed to spray. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def is_iphone_home():
    try:
        result = subprocess.check_output(["hcitool", "name", IPHONE_MAC])
        return bool(result.strip())  # Returns True if device is detected
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    spray_room_freshener() 