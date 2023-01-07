import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
from ConfigVariables import ConfigVariables
from ConsoleColor import ConsoleColor


class WebScraper:

    def __init__(self):
        self.review_dict = {'Review': []}
        self.user_agent = {'User-agent': 'Chrome/39.0.2171.95'}
        self.predictionCsvFilesLocation = ConfigVariables.localPredictionCsvFilesLocation
        self.blobExtension = ConfigVariables.blobExtension

    def web_scrape(self, input_url: str):
        url = input_url + '/user-reviews'
        page_amount = 1

        response = requests.get(url, headers=self.user_agent)
        soup = BeautifulSoup(response.text, 'html.parser')

        print(f"{ConsoleColor.GREEN}Web scraping in progress...{ConsoleColor.END}")

        for review in soup.find_all('div', class_='pages'):
            if review.find('li', class_='page last_page').find('a').text:
                page_amount = int(review.find('li', class_='page last_page').find('a').text)
            else:
                page_amount = 1

        for page in range(0, page_amount):

            url2 = url + '?page=' + str(page)
            user_agent = {'User-agent': 'Chrome/39.0.2171.95'}
            response = requests.get(url2, headers=user_agent)

            soup = BeautifulSoup(response.text, 'html.parser')

            for review in soup.find_all('div', class_='review pad_top1'):
                if review.find('span', class_='blurb blurb_expanded'):
                    self.review_dict['Review'].append(review.find('span', class_='blurb blurb_expanded').text)
                else:
                    self.review_dict['Review'].append(review.find('div', class_='review_body').find('span').text)

        now = datetime.now()
        output_file_name = now.strftime("%Y-%m-%d") + "-" + now.strftime("%H-%M-%S") + "-" + "reviews" + self.blobExtension

        reviews = pd.DataFrame(self.review_dict)
        reviews.to_csv(os.path.join(self.predictionCsvFilesLocation, output_file_name), index=False, encoding='utf-8')

        print(f"{ConsoleColor.GREEN}Web scraping has been finished successfully{ConsoleColor.END}")
