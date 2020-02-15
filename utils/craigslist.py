### Libraries to scrape craigslist data

import pandas as pd
import requests
import bs4

# Function to extract values or empty string when value is empty
def extract_value(value):
    try:
        value_extracted = value.contents[0]
    except:
        value_extracted = ""

    return value_extracted 

# function to extract each data point from a row
def extract_row(row):

    date = row.time["datetime"]
    description = extract_value(row.p.find("a", class_="result-title hdrlnk"))
    price = extract_value(row.p.find("span", class_="result-price"))
    hood = extract_value(row.p.find("span", class_="result-hood")).replace("(","").replace(")","")
    housing = ' '.join(extract_value(row.p.find("span", class_="housing")).replace("\n","").split())
    id = row.p.a["data-id"]
    url = row.a["href"]
    img = scraper_img(url)

    row_dict = {"id"           :   id,
                "url"          :   url,
                "date"         :   date,
                "description"  :   description,
                "price"        :   price,
                "hood"         :   hood,
                "housing"      :   housing,
                "img_url"      :   img}

    return row_dict

# Function to extract all properties for all pages
def scraper(url: str, craigslist: list=None) -> pd.DataFrame:

    if craigslist is None:
        craigslist = []

    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    rows = soup.find("ul", class_="rows").find_all("li", class_="result-row")

    [craigslist.append(extract_row(row)) for row in rows]

    next_url = soup.find("a", class_="button next")["href"]

    if next_url != "":
        scraper("https://berlin.craigslist.org" + next_url, craigslist)

    df = pd.DataFrame(craigslist)

    return df

# Function to extract img from detail page
def scraper_img(url: str) -> str:

    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "html.parser")

    try:    
        img = (soup
                .find("div", class_="slide first visible")
                .img["src"])
    except:
        img = ""

    return img

