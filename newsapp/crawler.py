import urllib
import json
import random
from random import shuffle
from threading import Thread
from bs4 import BeautifulSoup
from newsapp.models import *

def read_url(category):
	#list of urls for topic
	
	url_list = NewsSource.objects.all().values('url')
	
	link_groups = []
	selected_links = []
	threads = []
	
	#run each url read in a different thread
	for value in url_list:
		html = urllib.urlopen(value['url']).read().decode('utf-8')
		parent_soup = BeautifulSoup(html, 'html.parser');
		
		#send lin_groups so the threads appends links from the url to the list
		t = Thread(target=get_links_from_html, args=(parent_soup, link_groups))
		threads.append(t)
		t.start()

	#wait for threads to finish
	for t in threads:
		t.join()
	
	for link_group in link_groups:
		for link in link_group:
			#select some links randomly so we have links from different sources
			if(random.random() > 0.2):
				selected_links.append(link)
				if(len(selected_links) > 10):
					break
	
	#shuffle the links so all the links from same source are not linked together		
	shuffle(selected_links)
	
	return json.dumps(selected_links)

def get_links_from_html(soup, link_groups):
	
	a_elems = soup.find_all('a')
	link_titles = []
	links = []

	for a in a_elems:
		if(len(link_titles) > 10):
			break
			
		link = a.get('href')
		if(link == None):
			continue

		link_title = get_article_title(link)
		
		if(link.find('http')>-1 and len(link_title)>0):
			#make sure this article is not already in the list
			if(not(link_title in link_titles)):
				links.append(link)
				link_titles.append(link_title)
	
	link_groups.append(links)

# returns empty string if the page is not an article
# returns 'title' if it is an article
def get_article_title(link):
	
	if(link == None or link.find('http') == -1):
		return
	
	#read 
	content = urllib.urlopen(link).read().decode('utf-8')
	soup = BeautifulSoup(content)

	
	#if one of the the meta property has 'article' in it, it is considered an article
	#<meta property="article:section" content="Karnataka">
	#<meta property="article:author" content="Bageshree S.">
	#<meta property="article:published_time"
	meta_list = soup.find_all('meta')
	
	for meta in meta_list:
		if(not(meta.get('property') == None) and meta.get('property').find('article') > -1):
			return soup.title
	
	return ''




