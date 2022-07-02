# Most Active Authors
#
# API URL: https://jsonmock.hackerrank.com/api/articles?page=<pageNumber>
# threshold: integer that represents the threshold value for the number of submission count
# The function should return an array of strings that represent the usernames of users whose submission count is greater
# than the given threshold. The usernames in the array must be ordered in the order they appear in the API response
#

# Solution to hackerrank Top Articles problem
import requests
import json

def top_articles(limit):
	r = requests.get('https://jsonmock.hackerrank.com/api/articles')
	total_pages = r.json()['total_pages']
	articles = []

	for i in range(1, total_pages+1):
		article = requests.get('https://jsonmock.hackerrank.com/api/articles', params={'page': i})
		articles.append(article.json()['data'])

	articles = sum(articles, [])
	articles = sorted(articles, key=lambda x: (x['num_comments'] if x['num_comments'] is not None else 0, 
											   x['title'] or "",
											   x['story_title'] or ""), 
											   reverse = True)

	for i in range(0, limit):
		print(f"{articles[i]['title']}")

top_articles(2)