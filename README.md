# Newspaper Article Scraper

Script to scrape newspaper articles and some metadata from a list of supplied URLS.

## Inputs (via command-line):
  1. Path to CSV containing {freq, article URL} tuples you want to webscrape for analysis for patterns by tweet users. Defaults to sample.csv

Example: python scraper.py allepo.csv

## Outputs (via CSV): 
  1. A CSV of failed crawls in failed_crawl_results with article URL and error message
  2. A CSV of successful crawls in scraped_article_results with Article text, author, and other details

## Primary dependencies:
  - Written in Python 3.6.3
  - Newspaper
  - Beautifier

## Attempts to grab
  - article_url
  - article_title
  - article_text
  - article_authors
  - article_summary
  - article_keywords
  - article_top_image (urls)
  - article_images (urls)
  - article_movies (urls)
  - source_brand
  - source_description

**Be warned:** Takes time and you need to supply a cleaned list of urls yourself (or run it through Katie's de-duping pipeline).
