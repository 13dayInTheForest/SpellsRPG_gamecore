from fastapi import HTTPException
from asyncio import get_event_loop
from google.cloud import storage

from src.core.interfaces.cloud_stogare_interface import ICloudStorage


class GoogleCloudStorageService(ICloudStorage):
    async def add(self, bucket_name, file_data, blob_name) -> str:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        await get_event_loop().run_in_executor(None, blob.upload_from_string, file_data)

        return f'gs://{bucket_name}/{blob_name}'

    async def fetch(self, bucket_name: str, blob_name: str) -> bytes:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        if not blob.exists():
            raise HTTPException(status_code=404, detail=f"Can't find {blob_name}")

        return await get_event_loop().run_in_executor(None, blob.download_as_bytes())


    async def delete(self, bucket_name: str, blob_name: str):
        pass