import time
from datetime import datetime

log_file = "study_log.txt"

def log_study(minutes):
    with open(log_file, "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"{date} - Studied: {minutes} minutes\n")
    print(f"📝 Logged: {minutes} minutes")

print("=== Study Countdown Timer ===")
print("Controls:")
print(" p = pause")
print(" r = resume")
print(" s = stop")
print("-----------------------------")

while True:
    try:
        minutes = int(input("⏱️ Enter study duration (in minutes): "))
        break
    except:
        print("Enter a valid number please.")

remaining_seconds = minutes * 60
running = True
start_time = time.time()

print(f"▶️ Timer Started for {minutes} minutes.\nFocus.")

while remaining_seconds > 0 and running:
    time.sleep(1)
    remaining_seconds -= 1
    mins = remaining_seconds // 60
    secs = remaining_seconds % 60
    print(f"Time Left: {mins:02d}:{secs:02d}", end="\r")

    # Check if there is a user command without interrupting timer display
    if remaining_seconds % 2 == 0:  # Check input periodically
        import msvcrt
        if msvcrt.kbhit():
            key = msvcrt.getwch().lower()

            if key == "p":  # Pause
                print("\n⏸️ Paused.")
                running = False

                # Wait for resume
                while True:
                    key2 = msvcrt.getwch().lower()
                    if key2 == "r":  # Resume
                        print("▶️ Resumed.")
                        running = True
                        start_time = time.time()
                        break
                    elif key2 == "s":  # Stop while paused
                        studied_minutes = (minutes * 60 - remaining_seconds) // 60
                        print("\n⏹️ Stopped early.")
                        log_study(studied_minutes)
                        exit()

            elif key == "s":  # Stop immediately
                studied_minutes = (minutes * 60 - remaining_seconds) // 60
                print("\n⏹️ Stopped early.")
                log_study(studied_minutes)
                exit()

# Timer finished normally
print("\n✅ TIME'S UP! Good job.")
log_study(minutes)
