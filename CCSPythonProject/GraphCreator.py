import matplotlib.pyplot as plt
import pandas as pd


class GraphCreator:

    def plot_review_categories(self, csv_file):
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_file)

        # Add a column name to the second column
        df.rename(columns={df.columns[1]: "category"}, inplace=True)

        # Count the number of reviews in each category
        categories = df['category'].value_counts()

        # Extract the category names and counts into separate lists
        labels = list(categories.index)
        counts = list(categories.values)

        # Create a bar chart
        plt.bar(labels, counts)
        plt.xlabel('Category')
        plt.ylabel('Number of Reviews')
        plt.title('Number of Reviews in Each Category')
        plt.show()
