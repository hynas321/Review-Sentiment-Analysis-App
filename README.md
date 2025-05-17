# Review-Sentiment-Analysis-App

**Review-Sentiment-Analysis-App** is a Python program that uses **Vertex AI** and **Google Cloud Storage** in order to classify reviews posted online based on their **sentiment**.

There are three categories of sentiment: **positive**, **negative** and **controversial**. Based on the number of controversial reviews and the number of all reviews in total, one can determine if the review bombing is likely to have occured.
 
## Functionalities
![functionalities](https://github.com/hynas321/Review-bombing-detector/assets/76520333/ee084193-88a1-43a3-94bb-0fbc89f8ed28)

There are separate operations for blobs, datasets and models.  

Dataset is created from a blob's data (`Create and fill the dataset`).  
A model can be created from a dataset.


## Configuration
In order for the program to work, an up-to-date Google Cloud API key is needed in the `google-cloud-credentials.json` file. 

There are three folders which store sample `csv` files:  
- `ReviewsForDataset` - stores a dataset that can be used for model training
- `ReviewsForPrediction` - stores reviews that can be assigned to one out of three categories of sentiment
- `ReviewsPredictionResult` - stores a result of the model's prediction.

Only `csv` extension of datasets should be used to avoid errors in the program. Additionally, each folder's purpose should be followed, for example if one wants to classify reviews, a file with reviews should be added to `ReviewsForPrediction` folder.

**The private API key set by default is a sample key (not real). It does not give access to neccessary Google Cloud resources.**
