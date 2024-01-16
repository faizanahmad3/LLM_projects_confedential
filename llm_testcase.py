from opensearchpy import OpenSearch
import json

# Sample data
data = {
    "text": ["some text", "some other text"],
    "emb": ["embedding1", "embedding2"],
    "metadata": ["metadata1", "metadata2"]
}

# Connect to the OpenSearch cluster
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True  # Enables gzip compression for request bodies
)

# Prepare the bulk data
bulk_data = ''
for i in range(len(data["text"])):
    # Action line
    action = {"index": {"_index": "myindex", "_id": str(i + 1)}}
    bulk_data += json.dumps(action) + '\n'

    # Data line
    doc_data = {
        "text": data["text"][i],
        "emb": data["emb"][i],
        "metadata": data["metadata"][i]
    }
    bulk_data += json.dumps(doc_data) + '\n'

# The bulk data must be a single string with newline characters
# The last line must end with a newline character
bulk_data = bulk_data.strip() + "\n"

# Perform the bulk operation
response = client.bulk(body=bulk_data)
print(response)
