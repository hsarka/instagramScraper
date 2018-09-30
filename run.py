### Hi there!
### Check out Jiri's blog http://blog.hubacek.uk for more data-related stuff & check Sarka's blog not only for a post about this piece of code http://sarka.hubacek.uk/instagram-scraping-with-python/ 
### Use responsibly.

import csv 
from scrapeProfile import instaScraper
from parseInstaJson import parseInstaJson
from dumpToTsv import dumpToTsv
import sys
import logging

logging.basicConfig(
		level=logging.DEBUG,
		format='%(asctime)s %(levelname)s %(message)s',
		filename='instaScraper.log',
		filemode='w')

logging.info("Starting Instagram scraping process.")

if len(sys.argv) != 4:
	print("Arguments not provided, expected format: run.py <profile csv file> <profile output file> <post output file>")
	sys.exit()

# pass the source CSV filename in parameter, ie. test_data.csv
sourceProfileNames = sys.argv[1]

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