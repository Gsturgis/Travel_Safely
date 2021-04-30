import requests
from bs4 import BeautifulSoup
import csv

def webscraper():
    url = 'https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("tbody")
    rows = table.find_all("tr")
    data = []
    for i in range(1, len(rows)):
        x = (list(rows[i].stripped_strings))
        data.append(x)

    with open('Travel_advisory','w') as CSVfile:
        CSVWriter = csv.writer(CSVfile)
        for ml in data:
            CSVWriter.writerow(ml)  

if __name__ == '__main__':
    webscraper()