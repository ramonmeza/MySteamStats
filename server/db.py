import boto3
import uuid


def store_feedback(reason: str, description: str) -> str:
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("MySteamStats-Feedback")

    id = str(uuid.uuid4())

    table.put_item(
        Item={
            "id": id,
            "reason": reason,
            "description": description,
        }
    )
    return id
