from abc import ABC, abstractmethod


class ICloudStorage(ABC):
    @abstractmethod
    async def add_file(self, bucket_name: str, file_data: bytes, blob_name: str) -> str:
        pass

    @abstractmethod
    async def exist(self, bucket_name: str, blob_name: str):
        pass

    @abstractmethod
    async def fetch_file(self, bucket_name: str, blob_name: str):
        pass

    @abstractmethod
    async def delete_file(self, bucket_name: str, blob_name: str):
        pass
