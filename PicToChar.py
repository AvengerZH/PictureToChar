# coding:utf-8
from PIL import Image

def get_char(r, g, b, alpha=256):
	gray = (2126 * r + 7152 * g + 722 * b) / 10000
	ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,bn^`'.")
	x = int((gray / 256.0) * len(ascii_char))
	return ascii_char[x]

def ImageGet(file_name = "dora.png", width = 80, heigth = 80, out_file_name = "out_file.txt"):
	im = Image.open(file_name)
	im = im.resize((width, heigth))
	text = ""
	print im.size
	for i in xrange(width):
		for j in xrange(heigth):
			content = im.getpixel((j,i))
			tmp = get_char(content[1], content[2], content[3])
			if tmp == "$":
				text += " "
			else:
				text += tmp
		text += "\n"
	print text
	write_file(out_file_name, text)

def write_file(out_file_name, content):
	with open(out_file_name, "w") as f:
		f.write(content)

ImageGet()