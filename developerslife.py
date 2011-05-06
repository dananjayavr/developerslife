#!/usr/bin/python

import feedparser
import os

d = feedparser.parse('http://feeds.feedburner.com/ThisDevelopersLife')
print d['feed']['title']
print d.feed.subtitle
print d.channel.description
print ''
print d.feed.link
print ''

links_list = []
i = 0
for entry in d['entries']:
	links_list.append(d['entries'][i].links[1].href)
	print i,')', d['entries'][i]['title'], ' => ', d['entries'][i].links[1].href
	i += 1
	
print 'Press the corrsponding number to listen to the podcast.'
pod_choice = raw_input()

print 'You chose,', links_list[int(pod_choice)]
choice = str(links_list[int(pod_choice)])
os.system('vlc %s' % choice)