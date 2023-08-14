# Review Bombing Detector

## Description
**Review bombing** is an Internet phenomenon in which multiple accounts post negative reviews online with the intent to hurt the sales or popularity of a product, service, or business.

**Review Bombing Detector** is a Python program that uses **Vertex AI** and **Google Cloud Storage** in order to classify reviews posted online based on their **sentiment**. 

There are three categories of sentiment: **positive**, **negative** and **controversial**. Based on the number of controversial reviews and the number of all reviews in total, one can determine if the review bombing is likely to have occured.
 
## Functionalities
![functionalities](https://github.com/hynas321/Review-bombing-detector/assets/76520333/ee084193-88a1-43a3-94bb-0fbc89f8ed28)


## Configuration
In order for the program to work, an up-to-date Google Cloud AutoML API key is needed in the google-cloud-credentials.json file.

**The private API key set by default is a sample key (not real). It does not give access to neccessary Google Cloud resources.**
