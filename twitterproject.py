from Tkinter import *
window = Tk()
canvas = Canvas(window, width =500, height = 500, background="black")
canvas.pack()

def containWord(word, message):
	if word in message:
		return True
	else: 
		return False

def getTweet(tweet_line):
	values = tweet_line.split("\t")
	t = values[3]
	return t

def getLatitude(tweet_line):
	values = tweet_line.split("\t")
	t = values[0]
	a = t.split(",")
	b = a[0]
	c = b[1:]
	d = float(c)
	return d

def getLongitude(tweet_line):
	values = tweet_line.split("\t")
	t = values[0]
	a = t.split(",")
	b = a[0]
	c = b[1:-1]
	d = float(c)
	return d


def getGpsPixelX(tweet_line):
	x = (getLongitude(tweet_line) + 180) * 500.0/360
	return x

def getGpsPixelY(tweet_line):
	y = 500 - ((getLatitude(tweet_line) + 180 * 500.0/360))
	return y

def drawGpsPoint(tweet_line):
	x = getGpsPixelX(tweet_line)
	y = getGpsPixelY(tweet_line)
	canvas.create_rectangle(x, y, x+1, y+1, fill="white", width = 0)

f = open("tweets.txt")
big_str = f.read()
line_list = big_str.split("\n")
word = raw_input("Tweets loaded! What word would you like to search for?")
count = 0
for line in line_list:
	t = getTweet(line)
	if word in t:
			count += 1
			drawGpsPoint(line)

summary = ("The word " + word + " appears " + str(count) + " times ")
canvas.create_text(250, 250, text=summary, fill="white")

mainloop()