from PIL import Image
im = Image.open('end.png').convert('RGB')
x, y = im.size
print 'OFFSET: ' + str(y)
checksum = ''
for yy in range(0, y):
	color = im.getpixel((0, yy))
	checksum = checksum + str(color[0]) + ',' + str(color[1]) + ',' + str(color[2]) + ';'
print checksum
