import requests
from bs4 import BeautifulSoup

#import time
#import random as rand

import pandas as pd

review_dict = {'Name':[], 'Date':[], 'Review':[]}

for page in range(0,2): #Remember to update the number of pages
    url = 'https://www.metacritic.com/movie/avatar-the-way-of-water/user-reviews?page=' +str(page)
    user_agent = {'User-agent': 'Chrome/39.0.2171.95'}
    response  = requests.get(url, headers = user_agent)
    #time.sleep(rand.randint(3,30))
    soup = BeautifulSoup(response.text, 'html.parser')
    for review in soup.find_all('div', class_='review pad_top1'):
        # if review.find('span', class_='author') == None:
        #     break
        review_dict['Name'].append(review.find('span', class_='author').find('a').text)
        review_dict['Date'].append(review.find('span', class_='date').text)
        # review_dict['rating'].append(review.find('span', class_='review_grade').find_all('div')[0].text)
        if review.find('span', class_='blurb blurb_expanded'):
            review_dict['Review'].append(review.find('span', class_='blurb blurb_expanded').text)
        else:
            review_dict['Review'].append(review.find('div', class_='review_body').find('span').text)

sword_reviews = pd.DataFrame(review_dict)
sword_reviews.to_csv('results.csv', index=False, encoding='utf-8')
