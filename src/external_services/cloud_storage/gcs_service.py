from fastapi import HTTPException
from asyncio import get_event_loop
from google.cloud import storage

from src.core.interfaces import ICloudStorage


class GoogleCloudStorageService(ICloudStorage):
    def __init__(self):
        self.storage_client = storage.Client()

    async def add(self, bucket_name, file_data, blob_name) -> str:
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        await get_event_loop().run_in_executor(None, blob.upload_from_string,file_data, 'image/jpg')

        return f'gs://{bucket_name}/{blob_name}'

    async def fetch(self, bucket_name: str, blob_name: str) -> bytes:
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        exists = await get_event_loop().run_in_executor(None, blob.exists)
        if not exists:
            raise HTTPException(status_code=404, detail=f"Can't find {blob_name}")

        return await get_event_loop().run_in_executor(None, blob.download_as_bytes)

    async def delete(self, bucket_name: str, blob_name: str):
        pass

    async def exist(self, bucket_name: str, blob_name: str):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        return await get_event_loop().run_in_executor(None, blob.exists)