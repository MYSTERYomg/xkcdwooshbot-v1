# -*- coding: utf-8 -*-
import praw ##Reddit
import random ##For random.randint to decide whether or not we will be saying something else this time around.
import re ##To ignore case values in strings
import time ##To avoid spam

buzzwords = 'transgender' or 'bisexual' or 'homosexual' or 'religion' or 'depression' or 'suicide' ##This bot is supposed to be fun and silly. If someone doesn't get it, I don't want it to be in a sensitive context. Politics can go sod off though.
bannedSubreddit = 'neopets BlackwellAcademy steelers Christianity flightsim' ##We're banned from these, so let's not try to post in them. re.search will sort through the string for us.
blackListedSubreddit = 'anime asianamerican askhistorians askscience askreddit aww chicagosuburbs d3gf deer depression depthhub drinkingdollars forwardsfromgrandma geckos giraffes grindsmygears indianfetish misc movies mixedbreeds news newtotf2 omaha petstacking pigs programmingcirclejerk raerthdev runningcirclejerk salvia torrent torrents trackers unitedkingdom suicidewatch' ##Bots aren't allowed here, or it's just rude to post like this here.
the='the' ##Uncreative with how to chose random comments, this seems fine for now.

r = praw.Reddit('XKCD WooshBot v1.1 by /u/Aperson3334 and /u/MYSTERYomg and idea from the comic xkcd 1627 by Randall Munroe (praise be unto him) currently under management by /u/MYSTERYomg')
print ">>>Logging in." ## Tells us we're logging in...
r.login('', '') #SHHHH
time.sleep(1) #This counts in seconds.
print "Currently recognizing bans from '%s'" % bannedSubreddit
print "Bot will not post in subreddits with '%s' in the name" % blackListedSubreddit
print "Bot will not respond to post with buzzwords set buzzwords. Check file for info."
already_done = set() ##Makes a list of comments already replied to
thread_commented = set()
while True: ##Loop this
	print ">>>Loop start"
	all_comments = praw.helpers.flatten_tree(r.get_comments('all')) ##Gets all comments on reddit for the first time
	for comment in all_comments: ##For every comment
		subReddit = comment.subreddit ##Now we know what subreddit the comment is in.
		print ">>>Comment found! Making sure we can post..."
		if re.search("%s" %subReddit ,bannedSubreddit or blackListedSubreddit, re.IGNORECASE):
			print "Whoops! We can't post in /r/%s!" %comment.subreddit
		if re.search(buzzwords, comment.body, re.IGNORECASE):
			print "Whoops! This is a sensitive topic!"
		if comment.id in already_done:
			print "Whoops! We've posted on this one."
		if re.search(the, comment.body, re.IGNORECASE) and comment.id not in already_done and comment.submission not in thread_commented and not re.search("%s" %subReddit ,bannedSubreddit or blackListedSubreddit, re.IGNORECASE) and not re.search(buzzwords, comment.body, re.IGNORECASE): ##Search the comment body for the word "the" in any case and get the comment.id and make sure we haven't replied to it already and it's not banned.
			print ">>>Post is in %s" % subReddit ##This is the subreddit!
			time.sleep(.5) ##This makes the output look tidy-ish
			print ">>>Choosing what to say via random.randint..."
			randomizer = random.randint(0,100) ##Choosing a random number
			print ">>>random.randint chose %d!" % randomizer ##Displaying random number
			time.sleep(.5) ##Give it a moment please.
			if randomizer == 0:
				print ">>>Replying 'Are you for real?' to '%s'" % comment.body
				comment.reply('Are you for real?')
				print ">>>Successfully replied 'Are you for real?' !"
			if randomizer == 1:
				print ">>>Replying 'Comment of the year.' to '%s'" % comment.body
				comment.reply('Comment of the year.')
				print ">>>Successfully replied 'Comment of the year.' !"
			if randomizer == 2:
				print ">>>Replying 'screenshotting this moment so I can remember it forever' to '%s'" % comment.body
				comment.reply('screenshotting this moment so I can remember it forever')
				print ">>>Successfully replied 'screenshotting this moment...' !"
			if randomizer >= 3:
				print ">>>Replying 'Woosh.'"##Tells us we're commenting.
				comment.reply('Woosh.') ##the comment is posted
				print ">>>Successfully Wooshed!"
			already_done.add(comment.id)
			thread_commented.add(comment.submission)
			print ">>>Waiting 20 minutes..."
			time.sleep(999999) ##sleep to avoid spam
			print ">>>Done waiting, looping again..."  ##Tells us we're about to loop.
		else:
			print "Whoops! Something went wrong. Trying again..."
		all_comments = praw.helpers.flatten_tree(r.get_comments('all'))
## TODO: Make comment selection better. It should select words with specific reactions or something, I dunno, make it likely to cause a confused response.
## TODO: Perhaps limit it to only certain subreddits. It just didn't seem to make any sense in r/woodworking.
## TODO: Maybe private message people who respond?
## Note: Kansas City Chiefs subreddit is really nice.
## BANNED FROM: /r/neopets , /r/BlackwellAcademy (Note: "Worthless spam spewing bot. Get the fuck out of here.") , /r/steelers, /r/Christianity
