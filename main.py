import bs4
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')


# headers = []
# for i in table.find_all('th'):
#     if isinstance(i, bs4.element.Tag) and hasattr(i, 'string') and i.string is not None:
#         title_product = i.string
#         # print(title_product)
#         title_header = headers.append(title_product)
#         print(title_header)

headers = []
for i in table.find_all('th'):
    title = i.text
    # print(title)
    headers.append(title)

try:
    os.mkdir('data_result')
except FileExistsError:
        pass
df = pd.DataFrame(columns = headers)
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length = len(df)
    data_frame = df.loc[length] = row
    # print(data_frame)











