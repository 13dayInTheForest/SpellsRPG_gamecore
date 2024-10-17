from abc import ABC, abstractmethod


class ICloudStorage(ABC):
    @abstractmethod
    async def add(self, bucket_name, file_data, destination_blob_name):
        pass

    @abstractmethod
    async def fetch(self):
        pass

    @abstractmethod
    async def delete(self):
        pass