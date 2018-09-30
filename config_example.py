import os.path
from pathlib import Path

my_path = os.path.abspath(os.path.dirname(__file__))

logPath = f"{my_path}/instaScraper.log"
inputFilePath = f"{my_path}/input/test_data.csv"
outputProfileDataFilePath = f"{my_path}/output/dumped_profile_data.tsv"
outputPostsDataFilePath = f"{my_path}/output/dumped_posts_data.tsv"