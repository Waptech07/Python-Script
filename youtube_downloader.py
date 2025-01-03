from pytube import YouTube

def download_video():
    link = input("Enter the YouTube video link: ")
    try:
        yt = YouTube(link)
        print(f"\nTitle: {yt.title}")
        print(f"Views: {yt.views}")
        print("Downloading...")
        yt.streams.get_highest_resolution().download()
        print("Download complete! 🎉")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    print("\n--- YouTube Downloader ---")
    print("1. Download a Video")
    print("2. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        download_video()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
