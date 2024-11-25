from src.infrastructure.external_services.pictures.FLUX1schnellFree.service import FluxFreeAIPictureService
from src.infrastructure.external_services.cloud_storage.gcs.service import GoogleCloudStorageService


class PicContainer:
    @staticmethod
    def ai_picture_service():
        return FluxFreeAIPictureService()

    @staticmethod
    def cloud_service():
        return GoogleCloudStorageService
