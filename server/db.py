import aioboto3
import os
import uuid


from botocore.exceptions import ClientError


async def store_feedback(reason: str, description: str) -> str:
    id = str(uuid.uuid4())
    session = aioboto3.Session()

    async with session.resource(
        "dynamodb", region_name=os.getenv("AWS_DEFAULT_REGION")
    ) as dynamo_resource:
        table = await dynamo_resource.Table("MySteamStats-Feedback")

        await table.put_item(
            Item={
                "id": id,
                "reason": reason,
                "description": description,
            }
        )

    return id


async def get_all_feedback():
    session = aioboto3.Session()

    async with session.resource(
        "dynamodb", region_name=os.getenv("AWS_DEFAULT_REGION")
    ) as dynamo_resource:
        table = await dynamo_resource.Table("MySteamStats-Feedback")

        resp = await table.scan()
        items = resp.get("Items", [])
        return items


async def delete_feedback(id: str, reason: str) -> bool:
    session = aioboto3.Session()

    async with session.resource(
        "dynamodb", region_name=os.getenv("AWS_DEFAULT_REGION")
    ) as dynamo_resource:
        table = await dynamo_resource.Table("MySteamStats-Feedback")

        resp = await table.delete_item(Key={"id": id, "reason": reason})

        if resp.get("ResponseMetadata", {}).get("HTTPStatusCode") == 200:
            return True

        return False
