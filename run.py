### Hi there!
### Check out Jiri's blog http://blog.hubacek.uk for more data-related stuff & check Sarka's blog not only for a post about this piece of code http://sarka.hubacek.uk/
### Use responsibly.

import os.path
import sys
import logging
from pathlib import Path

my_path = os.path.abspath(os.path.dirname(__file__))
#print(my_path)

logging.basicConfig(
		level = logging.DEBUG,
		format = "%(asctime)s %(levelname)s %(message)s",
		filename = f"{my_path}/instaScraper.log",
		filemode = "w")

my_file = Path(f"{my_path}/config.py")
if not my_file.is_file():
	logging.critical("Config file not found.")

import csv 
from scrapeProfile import instaScraper
from parseInstaJson import parseInstaJson
from dumpToTsv import dumpToTsv
import config

logging.info("Starting Instagram scraping process.")

# pass the source CSV filename in parameter, ie. test_data.csv
sourceProfileNames = config.inputFilePath

with open(sourceProfileNames) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ",")
	
	for row in csv_reader:
		try:
			# skip the header
			if row[0] == "username": continue

			logging.debug(f"Getting JSON for username {row[0]}.")
			# get JSON from the Insta page
			scrapedJson = instaScraper(str(f"https://instagram.com/{row[0]}"))

			logging.debug(f"Parsing scraped JSON for username {row[0]}.")
			# build dictionary from scraped JSON
			parsedDict = parseInstaJson(scrapedJson)

			logging.debug(f"Writing data for username {row[0]} into TSV file.")
			# append to a tab-delimited text file
			dumpToTsv(parsedDict)
		
		# if something goes downhill, print the exception and continue to the next profile
		except Exception as e:
			logging.error(e)

logging.info("Instagram scraping process finished.")