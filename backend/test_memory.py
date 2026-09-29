from memory_client import recall_memories


query = """
A proposed production release for checkout-service includes a database migration
and a connection-pool change. What risks and previous lessons should the engineer
consider before deploying?
"""

response = recall_memories(query)

print("Recall succeeded")
print("Relevant memories:")

for memory in response.results:
    print("\n---")
    print("Type:", memory.type)
    print(memory.text)
