import os

from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("DB_URL"))
db = client["ytmanager"]
video_collection = db["videos"]


def add_video(video_name, video_length, video_url):
    video_collection.insert_one(
        {"video name": video_name, "video length": video_length, "video url": video_url}
    )


def list_videos():
    for video in video_collection.find():
        print(
            f"ID: {video['_id']}. name: {video['video name']}, duration: {video['video length']}, url: {video['video url']}"
        )


def update_video(video_id, video_name, video_length, video_url):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {
            "$set": {
                "video name": video_name,
                "video length": video_length,
                "video url": video_url,
            }
        },
    )


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("Youtube Videos Manager | Choose an option")
        print("1. Add a video")
        print("2. List all videos")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit the app")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            video_name = input("Enter video name: ")
            video_length = input("Enter video length: ")
            video_url = input("Enter video link: ")

            add_video(video_name, video_length, video_url)
        elif choice == 2:
            list_videos()
        elif choice == 3:
            video_id = input("Enter a video id to update: ")
            video_name = input("Enter new video name: ")
            video_length = input("Enter new video length: ")
            video_url = input("Enter new video link: ")

            update_video(video_id, video_name, video_length, video_url)
        elif choice == 4:
            video_id = input("Enter a video id to delete: ")
            delete_video(video_id)
        elif choice == 5:
            break
        else:
            print("Enter a valid choice")


if __name__ == "__main__":
    main()
