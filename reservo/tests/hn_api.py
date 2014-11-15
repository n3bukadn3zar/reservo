from hackernews import HackerNews
hn = HackerNews()

for title in hn.top_stories(limit=10):


    print hn.get_item(title)
