import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/user/PycharmProjects/webscraping/chromedriver.exe')
driver.get('https://www.metacritic.com/movie/black-adam/user-reviews')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')
driver.quit()

for element in soup.findAll('span', attrs='review_body'):
    name = element.find('span')
    if name not in results:
        results.append(name.text)
for b in soup.findAll('span', attrs='title pad_btm_half'):
    date = element.find('span')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('results.csv', index=True, encoding='utf-8')