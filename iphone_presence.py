import subprocess

IPHONE_MAC = "50:B1:27:38:56:30"  # iPhone's Bluetooth MAC

def is_iphone_home():
    try:
        result = subprocess.check_output(["hcitool", "name", IPHONE_MAC])
        return bool(result.strip())  # Returns True if device is detected
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    import time
    while True:
        if is_iphone_home():
            print("iPhone is home!")
        else:
            print("iPhone not detected.")
        time.sleep(2)
