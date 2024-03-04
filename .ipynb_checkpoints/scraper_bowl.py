import requests
from bs4 import BeautifulSoup

url = 'https://www.espncricinfo.com/series/australia-in-india-2022-23-1348637/india-vs-australia-1st-odi-1348656/full-scorecard'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': ''})
header_row = table.find('thead').find('tr')

header_cols = header_row.find_all('th')
for header_col in header_cols:
    print(header_col.text.strip())
