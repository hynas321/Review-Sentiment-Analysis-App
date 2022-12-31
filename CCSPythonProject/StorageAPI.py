import os

from ConfigVariables import ConfigVariables
from ConsoleColor import ConsoleColor
from google.cloud import storage


class StorageAPI:

    def __init__(self):
        self.csvFilesDirectory = ConfigVariables.localDatasetCsvFilesLocation
        self.client = storage.Client()
        self.bucket = self.client.bucket(ConfigVariables.googleCloudBucketName)
        self.blob_extension = ConfigVariables.blobExtension

    def create_blob(self, blob_name: str, file_name: str):
        full_file_name = f"{file_name}{self.blob_extension}"
        full_blob_name = f"{blob_name}{self.blob_extension}"

        bucket = self.client.bucket(self.bucket.name)
        blob = bucket.blob(full_blob_name)

        file_lines = []

        with open(os.path.join(self.csvFilesDirectory, full_file_name), "r", encoding="utf8") as f:
            file_lines.append(f.read())

        with blob.open("w", encoding="utf8") as f:
            for line in file_lines:
                f.write(line)

        print(f"\n{ConsoleColor.GREEN}Blob created successfully{ConsoleColor.END}")

    def list_blobs(self):
        blobs = self.client.list_blobs(self.bucket.name)

        number_of_blobs: int = 0

        print()

        for blob in blobs:
            print(blob.name)

            number_of_blobs += 1

        print(f"{ConsoleColor.GREEN}Number of displayed blobs: {number_of_blobs}{ConsoleColor.END}\n")

    def remove_blob(self, blob_name: str):
        bucket = self.client.bucket(self.bucket.name)
        blob = bucket.blob(f"{blob_name}{self.blob_extension}")
        blob.delete()

        print(f"\n{ConsoleColor.GREEN}Blob deleted successfully{ConsoleColor.END}\n")
