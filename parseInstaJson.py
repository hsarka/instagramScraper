import json
import datetime

def parseInstaJson(data):

	try:
		numberOfFollowers = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_followed_by"]["count"]
	# in case of a lonely gunman, which has no followers 
	except IndexError:
		numberOfFollowers = 0

	try:
		numberOfFollowed = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_follow"]["count"]
	# when there's no one interesting enough to follow
	except IndexError:
		numberOfFollowed = 0

	try:
		fullName = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["full_name"]
	# when the girl has no name
	except IndexError:
		fullName = ""

	userName = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["username"]

	try:
		numberOfPosts = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
	# when real life is much more interesting than your Instagram profile
	except IndexError:
		numberOfPosts = 0

	posts = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]

	postsList = []

	for p in posts:
		
		try:
			postId = p["node"]["id"]
		# no post id? bail out!
		except:
			break
		
		try:
			postTimestampRaw = p["node"]["taken_at_timestamp"]
			# be anywhere but be on UTC
			postTimestamp = datetime.datetime.utcfromtimestamp(postTimestampRaw).strftime('%Y-%m-%d %H:%M:%S')
		except IndexError:
			# when lost in space-time continuum
			postTimestamp = datetime.datetime.utcnow()
		
		try:
			postCaption = p["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
		# when there's nothing to say
		except IndexError:
			postCaption = ""
			traceback.print_exc()
		
		try:
			postComments = p["node"]["edge_media_to_comment"]["count"]
		# #nocomment
		except IndexError:
			postComments = 0
		
		try:
			postLikes = p["node"]["edge_liked_by"]["count"]
		# when nobody likes you... it... sorry
		except IndexError:
			postLikes = 0
		
		postsData = {"post_id" : postId, "post_timestamp" : postTimestamp, "caption" : postCaption, "comments" : postComments, "likes" : postLikes}
		#print(postsData)
		
		postsList.append(postsData)

	result = {"name" : fullName, "username" : userName, "number_of_followers" : numberOfFollowers, "number_of_following" : numberOfFollowed, "number_of_posts" : numberOfPosts, "posts_data" : postsList}
	
	return result 