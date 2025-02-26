from agents import Agent
import random

import warnings
warnings.filterwarnings("ignore")


def upload_to_youtube(filename: str, title: str, description: str) -> tuple[int, str]:
    """Upload a video to YouTube.

    Args:
      filename: The name of the file to upload.
      title: The title of the video.
      description: The description of the video.

    Returns:
        A tuple containing the status code (int) and the URL (str).
        Returns (200, url) if upload successfull
        Returns (500, "error message") if upload failed
    """

    # Upload the file to YouTube using the API, return the new URL if successful
    # in this dummy implementation we will always succeed

    # Simulate successful upload
    status_code = 200
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # Simulate failure (uncomment to test the error case)
    # status_code = 500
    # url = "Error uploading video: Invalid file format."

    return status_code, url


def update_image(filename: str, local_new_file: str) -> tuple[int, str]:
    """Upload a local file to a storage bucket, replacing the old file

    Args:
      filename: The name of the file to upload.
      local_new_file: The name of the local file to upload.

    Returns:
        A tuple containing the status code (int) and the URL (str).
    """

    # Replace the image with the local file.

    # Simulate successful upload
    status_code = 200
    url = "https://img.freepik.com/free-photo/empty-bucket_93675-128257.jpg"

    return status_code, url


def update_code_snippet(legacy_code: str) -> tuple[int, str]:
    """Update legacy code

    Args:
      legacy_code: The legacy code to update.


    Returns:
        A tuple containing the status code (int) and the new code snippet (str).
    """

    # Simulate successful refactoring
    status_code = 200
    new_code = """
      import base64
      import os
      from google import genai
      from google.genai import types
    """

    return status_code, new_code


root_agent = Agent(
    model='gemini-1.5-flash',
    name='docs_update_agent',
    instruction="""
      You check documentation assets and find usages of an old SDK. You update those in code snippets, videos, and images. You upload the new videos to our YouTube channel. The images are saved in a storage bucket and you replace the old images.
      Pretend that you have to update a code snippet, the legacy code is `import base64
      import os`. Pretend there are no videos or images that need updating.  
    """,
    tools=[
        upload_to_youtube,
        update_image,
        update_code_snippet,
    ],
    flow='single',
)
