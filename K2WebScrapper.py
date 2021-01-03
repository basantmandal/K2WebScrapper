# Install $ pip3 install requests
# Install $ pip3 install beautifulsoup4

from bs4 import BeautifulSoup
import requests
import csv

# Base URL - To Fetch Data
baseURL             = "https://www.techbasant.in/"

# Lets Get Data & Store it in Object
html_content        = requests.get(baseURL).text

# Parse HTML Code With Beautiful Soup
soup                = BeautifulSoup(html_content, "html.parser") 

# Lets Get Title Data
page_title          = soup.title.string

# Lets Get Meta Data
page_description    = "";
page_og_title       = "";

for meta in soup.findAll("meta"):
    meta_name = meta.get('name', '').lower()
    meta_property = meta.get('property', '').lower()

    if meta_name == 'description' or meta_property == "description":
        page_description = meta['content']

    if meta_name == 'og:title' or meta_property == "og:title":
        page_og_title = meta['content']

# Lets Save it in CSV File - Please Note - It Appends
csvFileName = "websiteData.csv";
with open(csvFileName, 'a') as csv_file_object:
    cwriter = csv.writer(csv_file_object, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    cwriter.writerow(['Website Title', 'Website Description', 'Page Og Title'])
    cwriter.writerow([page_title, page_description, page_og_title])

#ends