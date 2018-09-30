from instagramScraper import simple_get
from bs4 import BeautifulSoup
import json 

def instaScraper(instaLink):
	raw_html = simple_get(instaLink)
	
	raw_html = raw_html.decode("utf-8")
	scriptTags = BeautifulSoup(raw_html, "html.parser")
	
	scriptTag = ""
	
	# fetch all script tags from the scraped HTML
	for p in scriptTags.select("script"):
		# look for the script tag containing JSON data
		if str(p).startswith('<script type="text/javascript">window._sharedData'):
			scriptTag = str(p)
			break
	
	# strip the garbage
	stripJson = scriptTag.strip('<script type="text/javascript">window._sharedData = ')
	stripJson = stripJson.strip(";</script>")
	
	return json.loads(stripJson)