import json
import boto3


region = 'us-east-1'
# I am using the genaiday profile in my computer, change it to your profile name
aws = boto3.session.Session(profile_name='genaiday', region_name=region)

bedrock_runtime = aws.client(
    "bedrock-runtime"
)

MODEL_ID = "arn:aws:bedrock:us-east-1:XXXXX:default-prompt-router/anthropic.claude:1"

user_message = "Describe the purpose of a 'hello world' program in one line."
#user_message = "I want to consume a Shopify API to place a DraftOrder from a user prompt. How do I do that?"
messages = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    },
]

streaming_response = bedrock_runtime.converse_stream(
    modelId=MODEL_ID,
    messages=messages,
)

for chunk in streaming_response["stream"]:
    if "contentBlockDelta" in chunk:
        text = chunk["contentBlockDelta"]["delta"]["text"]
        print(text, end="")
    if "messageStop" in chunk:
        print()
    if "metadata" in chunk:
        if "trace" in chunk["metadata"]:
            print(json.dumps(chunk['metadata']['trace'], indent=2))