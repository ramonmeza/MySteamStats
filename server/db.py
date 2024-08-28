import boto3
import uuid


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("MySteamStats-Feedback")


def store_feedback(reason: str, description: str) -> str:
    id = str(uuid.uuid4())

    table.put_item(
        Item={
            "id": id,
            "reason": reason,
            "description": description,
        }
    )
    return id


def get_all_feedback():
    response = table.scan()
    items = response.get("Items", [])
    return items
