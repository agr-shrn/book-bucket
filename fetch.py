import os
import json

from facepy import GraphAPI
access_token = ""
graph = GraphAPI(access_token)

folder={};
# Create the output folder if it doesn't already exist
folder['posts'] = 'data/posts'
folder['friends'] = 'data/friends'

if not os.path.isdir(folder['posts']):
	os.mkdir(folder['posts'])
if not os.path.isdir(folder['friends']):
	os.mkdir(folder['friends'])
try:
	os.remove('data/posts/posts.json')
	os.remove('data/friends/friends.json')
except:
	pass
os.system('cd data/friends')
# Gather friends

friend_pages = graph.get("me/friends", page=True)
i=1
for friend_page in friend_pages:
	fri_file = "data/friends/" + str(i) + ".json"
	fh = open(fri_file,'a')
	json.dump(friend_page, fh, indent=1)
	i=i+1
	if(i>=5):
		break
# Gather posts
posts_pages = graph.get('me/posts', page=True)
with open('posts.json', 'a') as f:
	count = 0
	for posts_page in posts_pages:
		json.dump(posts_page, f, indent=1)
		
		count = count + 1
		if count >= 5:
			break
