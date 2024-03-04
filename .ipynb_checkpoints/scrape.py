import requests
from bs4 import BeautifulSoup

# Send a request to the URL
url = "http://howstat.com/cricket/Statistics/Series/SeriesAnalysis_ODI.asp?SeriesCode=1097&Scope=All"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element with class name "TableLined"
table = soup.find('table', {'class': 'TableLined'})

# Find all the tr elements within the table
rows = table.find_all('tr')

# Loop through each row and print its contents
for row in rows:
    print(row.text)
