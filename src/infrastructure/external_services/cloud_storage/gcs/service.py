from fastapi import HTTPException
from asyncio import get_event_loop
from google.cloud import storage

from src.domain.pictures.cloud_storage import ICloudStorage


class GoogleCloudStorageService(ICloudStorage):
    def __init__(self):
        self.storage_client = storage.Client()

    async def add_file(self, bucket_name, file_data, blob_name) -> str:  # Добавить файл
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(bucket)

        await get_event_loop().run_in_executor(None, blob.upload_from_string, file_data, 'image/jpg')

        return f'gs://{bucket_name}/{blob_name}'

    async def exist(self, bucket_name: str, blob_name: str) -> None:  # Проверка на существование файла
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        if not await get_event_loop().run_in_executor(None, blob.exists):
            raise HTTPException(status_code=404, detail=f"Can't find {blob_name}")

    async def fetch_file(self, bucket_name: str, blob_name: str) -> bytes:  # Скачать файл если есть
        await self.exist(bucket_name, blob_name)
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        return await get_event_loop().run_in_executor(None, blob.download_as_bytes)

    async def delete_file(self, bucket_name: str, blob_name: str):  # Удалить файл если есть
        await self.exist(bucket_name, blob_name)

        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        return await get_event_loop().run_in_executor(None, blob.delete)
