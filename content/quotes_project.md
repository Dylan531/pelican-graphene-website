Title: Small Quotes Project
Date: 2016-01-08 15:14
Tags: python, projects
Category: Python Development
Slug: quotes-project
Authors: Dylan

  One day on a whim I decided I wanted to do something with all of the quotes my friends and I had gathered. We have a page we add our
most favorite quotes onto, the page functions much like a Google Doc, where you can see everybody editing the file, as well as editing it
yourself. So what I end up with is a text file with over 500 lines of various quotes and data that cannot be properly formatted. The
first step was developing something to sort through out of it, of which I created this mess:

	import re
  	import fileinput

  	quotes = []

  	for line in fileinput.input('quotes'):
      		r_unwanted = re.compile("[\n\t\r]")
      		line = r_unwanted.sub("", line)
      		line = re.sub(r"(^\')",'\"', line)
      		line = re.sub(r"(\'\s)",'\" ', line)
      		line = re.split(r' ', line)
      		if line[0] == '':
        		continue
      		if '5' in line[-1] and "\"" in line[0][0]:
        		def check(x):
            			if x is None:
                			return
            			elif x:
                			return x.group(0)
			string = ' '.join(line)
			match1 = re.search(r'^(\".*\")', string)
			match2 = re.search(r'\"\s(.*)\s\d', string)
			string1 = check(match1)
			if check(match2):
				string2 = check(match2)[2:-2]
			else: 
				continue
			line = [string1, string2, line[-1]]
			quotes.append(line)
