import time

seconds = int(input("Enter time in seconds: "))
while seconds:
    mins, secs = divmod(seconds, 60)
    print(f"\rTime left: {mins:02}:{secs:02}", end="")
    time.sleep(1)
    seconds -= 1

print("\n⏰ Time's up!")
