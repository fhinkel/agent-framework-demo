from typing import Any, Dict, List, Optional
from google.genai import types
from agents.sessions import Session
from agents.sessions import InMemorySessionService
from agents.events import Event
from agents.artifacts import InMemoryArtifactService
from agents import Runner
import os
import warnings
import random
from agents import Agent
import vertexai
from vertexai.preview import reasoning_engines

PROJECT_ID = "af-deploy"
LOCATION = "us-central1"
RELEASE_VERSION = 'google_genai_agents-0.0.2.dev20250204+723246417'


warnings.filterwarnings("ignore")

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "1"
os.environ["GOOGLE_CLOUD_PROJECT"] = PROJECT_ID
os.environ["GOOGLE_CLOUD_LOCATION"] = LOCATION


session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()


def create_session(context):
    session = session_service.create(
        "Documentation Update Agent App", "user", context, session_id="demo_session_id ")
    return session


def run_prompt(session: Session,
               runner: Runner,
               message: str):
    content = types.Content(
        role='user', parts=[types.Part.from_text(text=message)])
    for event in runner.run(
        session=session,
        new_message=content,
    ):
        if event.content:
            print(event.content.model_dump(exclude_none=True))
            pass


agent_context = {
    "company_name": 'Otis Worldwide Corporation',
    # "company_name": 'Hinkelmann LLC'
}


class App:
    def __init__(self, agent):
        self.session_service = InMemorySessionService()
        self.runner = Runner(
            app_name="docs_update_agent",
            agent=agent,
            artifact_service=InMemoryArtifactService(),
            session_service=self.session_service,
        )

    def agent_run(self, session_id: str, message: str):
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "1"
        os.environ["GOOGLE_CLOUD_PROJECT"] = "af-deploy"
        os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
        yield from self.runner.run(
            session=self.session_service.create(
                "docs_update_agent",
                "user",
                state=agent_context,
                session_id=session_id,
            ),
            new_message=types.Content.model_validate_json(message),
        )

    def register_operations(self) -> Dict[str, List[str]]:
        return {"stream": ["agent_run"]}


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
      legacy_code: The legacy code to update. It can be any programming language.


    Returns:
        A tuple containing the status code (int) and the new code snippet (str). Code snippets can be incomplete pieces of code. They are most likely part of a larger working sample that is irrelevant here. 
    """

    # Simulate successful refactoring
    status_code = 200
    new_code = """
        # This program prints Hello, world!
        print('Hello, world!')
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


vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    # api_endpoint="us-central1-autopush-aiplatform.sandbox.googleapis.com",
    api_endpoint="us-central1-aiplatform.googleapis.com",
    staging_bucket="gs://agent-engine-deploy-1",
)

remote_app = reasoning_engines.ReasoningEngine.create(
    App(root_agent),
    display_name="documentation_update_agent_app",
    requirements=[
        RELEASE_VERSION + "-py3-none-any.whl",
        "google_cloud_aiplatform",
        "google_genai",
        "cloudpickle==3.1.1",
        "pydantic==2.10.6",
        "pytest",
        "overrides",
    ],
    extra_packages=[
        RELEASE_VERSION + "-py3-none-any.whl",
    ],
)
