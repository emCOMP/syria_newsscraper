"""
Inputs (via command-line):
1. Path to CSV containing {freq, article URL} tuples you want to webscrape for analysis for patterns by tweet users. Defaults to sample.csv

Example: python scraper.py allepo.csv

Outputs (via CSV): 
1. A CSV of failed crawls in failed_crawl_results with article URL and error message
2. A CSV of successful crawls in scraped_article_results with Article text, author, and other details

Primary dependencies:
- Written in Python 3.6.3
- Newspaper
- Beautifier
"""

import newspaper
from newspaper import Article
from beautifier import Url
import csv, random, sys
import itertools

# Helper functions
def get_sample_file():
  if len(sys.argv) >= 2:
    return sys.argv[1]
  else:
    return "sample.csv"

def read_from_csv(file_name):
  with open(file_name, 'rb') as f:
    reader = csv.reader(f)
    return reader

def write_to_csv(name,data):
  with open("{name!s}_results.csv".format(**locals()), "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Entry point
crawled_articles=[]
failed_crawls=[]

with open("run3.1_fails.csv", 'rt') as f:
  reader = csv.reader(f)
  x = map(list, reader)
  urls = [url for url in x]
for url in urls: # For each URL
  try:
    # We load the data and try to build the source
    article_freq = url[0] 
    article_url = url[1]
    source_url = Url(article_url).domain
    source = newspaper.build("http://www."+str(source_url))
    source_brand = source.brand
    source_description = source.description

    # We download the Article and as much data as possible
    article = Article(article_url)
    article.download()
    article.parse()
    article_title = article.title
    article_top_image = article.top_image
    article_images = article.images
    article_movies = article.movies
    article_authors = article.authors
    article_text = article.text

    # Run some NLP goodness
    article.nlp()

    article_summary = article.summary
    article_keywords = article.keywords
    # Store the results
    crawled_articles += [[article_url] + 
                          [article_freq] + 
                          [article_title] + 
                          [article_text] + 
                          [article_authors] + 
                          [article_summary] + 
                          [article_keywords] +
                          [article_top_image] +
                          [article_images] +
                          [article_movies] +
                          [source_brand] +
                          [source_description] +
                          [source_url]]
  except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    failed_crawls += [[article_freq] + 
                          [article_url] + 
                          [source_url] + 
                          [message]]
    print("Something went wrong grabbing: "+ article_url)

# Write the results
write_to_csv("failed_crawls", ([["Freq"] + 
                          ["Article URL"] + 
                          ["Source URL"] + 
                          ["Message"]] +
                        failed_crawls))

write_to_csv("scraped_articles", ([["Article URL"] + 
                          ["Est. Freq"] + 
                          ["Title"] + 
                          ["Text"] + 
                          ["Authors"] + 
                          ["Summary"] + 
                          ["Keywords"] + 
                          ["Top Image"] +
                          ["images"] +
                          ["movies"] +
                          ["Source Brand"] +
                          ["Source Description"] +
                          ["Source URL"]] +
                        crawled_articles))
