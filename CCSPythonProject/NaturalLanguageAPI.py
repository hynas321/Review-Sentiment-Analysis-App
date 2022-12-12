from ConfigVariables import ConfigVariables
from ConsoleColor import ConsoleColor
from google.cloud import automl
from StorageAPI import StorageAPI


class NaturalLanguageAPI:

    def __init__(self):
        self.project_id = ConfigVariables.googleCloudProjectId
        self.project_location = ConfigVariables.googleCloudProjectLocation
        self.credentials = ConfigVariables.googleCloudCredentials
        self.cloud_region = ConfigVariables.googleCloudRegion
        self.blob_extension = ConfigVariables.blobExtension

        self.client = automl.AutoMlClient()
        self.bucket = StorageAPI().bucket

    def create_dataset(self, dataset_display_name: str, blob_name: str):
        metadata = automl.TextClassificationDatasetMetadata(
            classification_type=automl.ClassificationType.MULTICLASS
        )

        dataset = automl.Dataset(
            display_name=dataset_display_name,
            text_classification_dataset_metadata=metadata,
        )

        response = self.client.create_dataset(parent=self.project_location, dataset=dataset)

        print(f"\n{ConsoleColor.OKGREEN}Dataset created successfully.{ConsoleColor.ENDC} {response.result()}")

        dataset_id = response.result().dataset.name.split('/')[-1]

        self.__fill_dataset(dataset_id, blob_name)

        return response

    def display_datasets(self):
        request = automl.ListDatasetsRequest(parent=self.project_location, filter="")
        response = self.client.list_datasets(request=request)

        number_of_datasets: int = 0

        for dataset in response:
            print()
            print(f"Dataset name: {dataset.name}")
            print(f"Dataset id: {dataset.name.split('/')[-1]}")
            print(f"Dataset display name: {dataset.display_name}")
            print(f"Dataset create time: {dataset.create_time}")

            number_of_datasets += 1

        print(f"\n{ConsoleColor.OKGREEN}Number of displayed datasets: {number_of_datasets}{ConsoleColor.ENDC}\n")

    def remove_dataset(self, dataset_id: str):
        dataset_full_id = self.client.dataset_path(self.project_id, self.cloud_region, dataset_id)
        response = self.client.delete_dataset(name=dataset_full_id)

        print(f"\n{ConsoleColor.OKGREEN}Dataset deleted successfully.{ConsoleColor.ENDC} {response.result()}\n")

        return response.result()

    def __fill_dataset(self, dataset_id: str, blob_name: str):
        dataset_full_id = self.client.dataset_path(self.project_id, self.cloud_region, dataset_id)
        blob_path = f"gs://{self.bucket.name}/{blob_name}{self.blob_extension}"

        input_uris = blob_path.split(",")
        gcs_source = automl.GcsSource(input_uris=input_uris)
        input_config = automl.InputConfig(gcs_source=gcs_source)

        self.client.import_data(name=dataset_full_id, input_config=input_config)
