from .memory_client import recall_memories


def analyze_release(
    service: str,
    environment: str,
    release: str,
    change: str,
) -> dict:
    """Analyze a proposed release using organizational deployment memory."""

    query = f"""
    Analyze this proposed software deployment:

    Service: {service}
    Environment: {environment}
    Release: {release}
    Change: {change}

    Find previous incidents, failed fixes, successful remediations, and deployment
    lessons that are relevant to this release. Explain what the engineer should
    do before deploying.
    """

    response = recall_memories(query)
    memories = response.results

    if not memories:
        return {
            "risk_level": "UNKNOWN",
            "summary": (
                "No relevant deployment memories were found. "
                "Use a staged rollout, monitor the release, and prepare rollback."
            ),
            "recommendations": [
                "Validate the change in a non-production environment.",
                "Prepare and test a rollback plan.",
                "Monitor errors, latency, and resource usage.",
            ],
            "memories_used": [],
        }

    memory_texts = [memory.text for memory in memories]

    recommendations = [
        "Review the recalled incidents before deployment.",
        "Do not repeat remediation steps that previously failed.",
        "Prefer the successful deployment pattern from the recalled experience.",
        "Use a staged rollout and monitor the relevant service metrics.",
    ]

    risk_level = "HIGH" if len(memories) >= 2 else "MEDIUM"

    return {
        "risk_level": risk_level,
        "summary": (
            f"Hindsight recalled {len(memories)} relevant deployment memories. "
            "The release should be reviewed against these prior outcomes before deployment."
        ),
        "recommendations": recommendations,
        "memories_used": memory_texts,
    }
