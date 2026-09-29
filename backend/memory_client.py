import os

from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

HINDSIGHT_API_URL = os.environ["HINDSIGHT_API_URL"]
HINDSIGHT_API_KEY = os.environ["HINDSIGHT_API_KEY"]
HINDSIGHT_BANK = os.environ["HINDSIGHT_BANK"]

client = Hindsight(
    base_url=HINDSIGHT_API_URL,
    api_key=HINDSIGHT_API_KEY,
    timeout=30.0,
)


def retain_memory(content: str, context: str = ""):
    """Store a deployment lesson in Hindsight."""
    return client.retain(
        bank_id=HINDSIGHT_BANK,
        content=content,
        context=context,
    )


def recall_memories(query: str):
    """Recall deployment lessons relevant to a new release."""
    return client.recall(
        bank_id=HINDSIGHT_BANK,
        query=query,
        types=["world", "experience", "observation"],
        budget="high",
        max_tokens=4096,
    )
