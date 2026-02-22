import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env
load_dotenv()

# Settings
API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def get_channel_videos(query):
    """
    """
    youtube_service = build(YOUTUBE_API_SERVICE_NAME,
                            YOUTUBE_API_VERSION, developerKey=API_KEY)

    # Search for channel
    response = youtube_service.search().list(
        q=query,
        type='channel',
        part='id.snippet',
        maxResults=1
    ).execute()

    if not response.get('items'):
        print("Channel not found.")
        return
