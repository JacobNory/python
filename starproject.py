from Tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=500, background="black")
canvas.pack()


def getStarPixelX(star_string):
    nums = star_string.split(",")
    x = float(nums[0])
    xp = 250 + (250 * x)
    return xp

def getStarPixelY(star_string):
    nums = star_string.split(",")
    y = float(nums[1])
    yp = 250 - (250 * y)
    return yp

def getstarSize(star_string):
    nums = star_string.split(",")
    mag = float(nums[4])
    mp = 10 / (mag + 2)
    return mp

def getStarName(star_string):
	nums = star_string.split(",")
	if len(nums) == 7:
		return nums[6]
	else:
		return ""

def drawStar(star_string):
	x = getStarPixelX(star_string)
	y = getStarPixelY(star_string)
	size = getstarSize(star_string)
	
	leftX = x - (size/2)
	rightX = x + (size/2)
	topY = y - (size/2)
	bottomY = y + (size/2)
	
	canvas.create_rectangle(leftX, topY, rightX, bottomY, fill="white", width=0)
	
def drawAllStars():
	f = open("stars.txt")
	big_str = f.read()
	line_list = big_str.split("\n")
	for line in line_list:
		drawStar(line)

def getStarString(a):
	f = open("stars.txt")
	bigstring = f.read()
	line_list = bigstring.split("\n")
	for L in line_list:
		n = getStarName(L)
		if n == a:
			return L
	print("ERROR: No star called " + o + " could be found.")
	return("")

def drawStarByName(starname):
	s = getStarString(starname)
	drawStar(starname)

def drawConstellationLine(a, b):
	lineA = getStarString(a)
	lineB = getStarString(b)
	x1 = getStarPixelX(lineA)
	y1 = getStarPixelY(lineA)
	x2 = getStarPixelX(lineB)
	y2 = getStarPixelY(lineB)
	canvas.create_line(x1, y1, x2, y2, fill="yellow")

def drawConstellationFile(a):
	f = open(a)
	bigstring = f.read()
	line_list = bigstring.split("\n")
	for L in line_list:
		stringlist = L.split(",")
		starname1 = stringlist[0]
		starname2 = stringlist[1]
		drawConstellationLine(starname1, starname2)
		
	

drawAllStars()
drawConstellationFile("BigDipper_lines.txt")
drawConstellationFile("Bootes_lines.txt")
drawConstellationFile("Cas_lines.txt")
drawConstellationFile("Cyg_lines.txt")
drawConstellationFile("Gemini_lines.txt")
drawConstellationFile("Hydra_lines.txt")
drawConstellationFile("UrsaMajor_lines.txt")
drawConstellationFile("UrsaMinor_lines.txt")

mainloop()