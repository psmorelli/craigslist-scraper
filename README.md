# Craigslist Scraper
Ironhack Hackaton - Craigslist

## Purpose

    Scrape relevant data from craigslist.com to input inside hackaton demo project.


## Project Structure

    data/
    |    |
    |    |_ craigslist.json
    |        
    utils
    |    |_ craigslist.py
    |
    craigslist.ipynb
    README.md

## Workflow

    * Iteract with each page recursively 
    * Extract relevant data from main page for each property 
    * Access detail page for each property to extract image URL
    * Save JSON File with table orientation

## craigslist-mvp.py

    Library created to scrape craigslist, functions:

    # function to extract each data point from a row
    def extract_row(row: bs4.element.Tag) -> dict:

    # Function to extract all properties for all pages
    def scraper(url: str, craigslist: list=None) -> pd.DataFrame:

    # Function to extract img from detail page
    def scraper_img(url: str) -> str:



