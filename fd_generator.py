from __future__ import print_function
from PIL import Image, ImageDraw
import optparse


# #############################################
#28*28 black and white
def get_hex_list(bili,panel_number): #input a list of 28*7 binaries, return a list of 7 hex
	
	str_li = [] #7 string binary list
	for r in range(28):
		s = ""
		for l in range(7):
			s = str(bili[r + 28*l]) + s #add to the front of the string
		str_li.append(s)
	beginning=[['0x80', '0x83', '0x00'],['0x80', '0x83', '0x01'],['0x80', '0x83', '0x02'],['0x80', '0x83', '0x03']]
	#beginning signal
	hex_li = beginning[panel_number]
	#image part
	for s in str_li:
		hex_li.append(hex(int(s,2)))
	#ending signal
	hex_li.append('0x8F')
	return(hex_li)

def get_one_frame_string(image_number): #{{...},{},{},{}}

	im = Image.open('tencent/' + str(image_number)+".png").convert('1')
	ori_li = list(im.getdata()) #255-white  0-black
	new_li = [] #1-white  0-black
	for p in ori_li:
		if (p==255):
			new_li.append(1)
		else:
			new_li.append(0)

	one_frame = "{"
	for i in range(4):
		hex_li = get_hex_list(new_li[i*28*7:],i)
		one_frame += ('{' + ','.join(hex_li) + '}')
		if (i != 3):
			one_frame += ','
	one_frame += "}"
	return (one_frame)

f = open('export_arrays.txt','w')
whole_string = '{'
for i in range(1,5):
	whole_string += get_one_frame_string(i)
	if (i != 4):
		whole_string += ','
whole_string += '}'
f.write(whole_string)
f.close()



