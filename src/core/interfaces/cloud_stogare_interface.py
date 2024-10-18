from abc import ABC, abstractmethod


class ICloudStorage(ABC):
    @abstractmethod
    async def add(self, bucket_name: str, file_data: bytes, blob_name: str) -> str:
        pass

    @abstractmethod
    async def fetch(self, bucket_name: str, blob_name: str):
        pass

    @abstractmethod
    async def delete(self, bucket_name: str, blob_name: str):
        pass
