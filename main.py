import time
from datetime import datetime
try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:
    from pytz import timezone as ZoneInfo  # fallback for older Python
from iphone_presence import is_iphone_home
from simple_spray import spray_room_freshener

class MainController:
    def __init__(self):
        pass  # Will add logic for time, presence, and spray

    def is_time_allowed(self):
        # Always use Indian Standard Time (IST)
        now = datetime.now(ZoneInfo('Asia/Kolkata'))
        start = now.replace(hour=9, minute=0, second=0, microsecond=0)
        end = now.replace(hour=23, minute=0, second=0, microsecond=0)
        return start <= now <= end

    def is_iphone_present(self):
        present = is_iphone_home()
        print(f"[LOG] iPhone present: {present}")
        return present

    def run(self):
        print("[LOG] MainController started. Monitoring...")
        while True:
            if self.is_time_allowed():
                if self.is_iphone_present():
                    print("[LOG] Spraying room freshener...")
                    spray_room_freshener()
                else:
                    print("[LOG] iPhone not present. Skipping spray.")
            else:
                print("[LOG] Time is outside allowed range (9am-11pm). Skipping spray.")
            # Wait for 30 minutes before next check/spray
            time.sleep(1800)

if __name__ == "__main__":
    controller = MainController()
    controller.run() 