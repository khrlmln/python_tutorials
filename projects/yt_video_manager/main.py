import json

filename = "youtube_data.json"


def load_data():
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(filename, "w") as f:
        json.dump(videos, f)


def add_video(videos):
    video_name = input("Enter video name: ")
    video_length = input("Enter video length: ")
    video_url = input("Enter video link: ")

    videos.append(
        {"video name": video_name, "video length": video_length, "video url": video_url}
    )

    save_data_helper(videos)


def list_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(
            f"{index}. {video['video name']}, {video['video length']}, {video['video url']}"
        )


def update_video(videos):
    list_videos(videos)

    video_id = int(input("Enter a video id to update: "))

    if 1 <= video_id <= len(videos):
        video_name = input("Enter new video name: ")
        video_length = input("Enter new video length: ")
        video_url = input("Enter new video link: ")

        videos[video_id - 1] = {
            "video name": video_name,
            "video length": video_length,
            "video url": video_url,
        }

        save_data_helper(videos)

    else:
        print("Enter a valid ID")


def delete_video(videos):
    list_videos(videos)

    video_id = int(input("Enter a video id to delete: "))

    if 1 <= video_id <= len(videos):
        del videos[video_id - 1]

        save_data_helper(videos)
    else:
        print("Enter a valid ID")


def main():
    videos = load_data()

    while True:
        print("Youtube Videos Manager | Choose an option")
        print("1. Add a video")
        print("2. List all videos")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit the app")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                add_video(videos)
            case 2:
                list_videos(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Enter a valid choice")


if __name__ == "__main__":
    main()
