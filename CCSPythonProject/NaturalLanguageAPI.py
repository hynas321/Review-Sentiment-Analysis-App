from ConsoleColor import ConsoleColor
from google.cloud import automl
import os


class NaturalLanguageAPI:

    def __init__(self):
        root_directory = os.path.dirname(os.path.abspath(__file__))

        self.project_id = "automl-370415"
        self.credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
            os.path.join(root_directory, "google-cloud-credentials.json")

        self.project_location = f"projects/{self.project_id}/locations/us-central1"
        self.client = automl.AutoMlClient()

    def create_dataset(self, dataset_display_name: str):
        metadata = automl.TextClassificationDatasetMetadata(
            classification_type=automl.ClassificationType.MULTICLASS
        )

        dataset = automl.Dataset(
            display_name=dataset_display_name,
            text_classification_dataset_metadata=metadata,
        )

        response = self.client.create_dataset(parent=self.project_location, dataset=dataset)

        print(f"\n{ConsoleColor.OKGREEN}Dataset created successfully.{ConsoleColor.ENDC} {response.result()}")

        return response.result()

    def display_datasets(self):
        request = automl.ListDatasetsRequest(parent=self.project_location, filter="")
        response = self.client.list_datasets(request=request)

        print(f"\n{ConsoleColor.OKGREEN}List of datasets:{ConsoleColor.ENDC}")

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
        dataset_full_id = self.client.dataset_path(self.project_id, "us-central1", dataset_id)
        response = self.client.delete_dataset(name=dataset_full_id)

        print(f"\n{ConsoleColor.OKGREEN}Dataset deleted successfully.{ConsoleColor.ENDC} {response.result()}\n")

        return response.result()

    def __fill_dataset(self, dataset_id: str):
        pass
