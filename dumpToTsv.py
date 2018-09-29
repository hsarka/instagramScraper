import json
import csv
import sys
import datetime 

def dumpToTsv(parsedDict):
	# pass the filename for dumping profile data in parameter, ie. dumped_profile_data.tsv
	dumpingProfileDataFile = sys.argv[2]
	with open(dumpingProfileDataFile, mode = "a") as data_file:
		data_writer = csv.writer(data_file, delimiter = "\t")
		# header:
		# data_writer.writerow(["name", "username", "number_of_followers", "number_of_following", 	"number_of_posts"])
		row = []
		row.append(datetime.datetime.utcnow())
		row.append(parsedDict["name"])
		row.append(parsedDict["username"])
		row.append(parsedDict["number_of_followers"])
		row.append(parsedDict["number_of_following"])
		row.append(parsedDict["number_of_posts"])
		data_writer.writerow(row)

	new_posts = parsedDict["posts_data"]

	# pass the filename for dumping posts data in parameter, ie. dumped_posts_data.tsv
	dumpingPostsDataFile = sys.argv[3]
	with open(dumpingPostsDataFile, mode = "a") as data_file:
		data_writer = csv.writer(data_file, delimiter = "\t", quotechar='"', quoting=csv.QUOTE_ALL)
		# header:
		# data_writer.writerow(["username", "post_id", "post_timestamp", "caption", "comments", "likes"])

		for p in new_posts:
			row = []
			row.append(datetime.datetime.utcnow())
			row.append(parsedDict["username"])
			row.append(p["post_id"])
			row.append(p["post_timestamp"])
			row.append(p["caption"])
			row.append(p["comments"])
			row.append(p["likes"])
			data_writer.writerow(row)