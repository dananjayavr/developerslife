#!/usr/bin/python

import feedparser
import os,sys

print 'd - Developes\' Life Podcast'
print 'h - Hanselman Minutes Podcast'
print 'q - Quit'

pod_select = raw_input()
d = ''
if pod_select == 'd':
	d = feedparser.parse('http://feeds.feedburner.com/ThisDevelopersLife')
if pod_select == 'h':
	d = feedparser.parse('http://feeds.feedburner.com/HanselminutesCompleteMP3')
if pod_select == 'q':
	sys.exit(0)
	

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
	print i,')', d['entries'][i]['title'], '\n', d['entries'][i].links[1].href
	i += 1
	
print 'Press the corrsponding number to listen to the podcast.'
print 'OR Enter to Quit.'
try:
	pod_choice = raw_input()
	choice = str(links_list[int(pod_choice)])
	os.system('vlc %s' % choice)
except ValueError:
	sys.exit(0)
