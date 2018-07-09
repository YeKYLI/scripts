import cv2
#input the valid path
file = open('2007_test.txt', 'r')
lines = file.readlines()
len1 = len(lines)
len2 = 0
fileceshi = open('ceshi', 'w')

for i in lines:
	im = cv2.imread(i.replace('\n', ''))
	h,w = im.shape[:2]

	with open(i.replace('\n', '').replace('JPEGImages', 'labels').replace('jpg','txt'), 'r') as filei:
		linesi = filei.readlines()
		filei = open(i.replace('\n', '').replace('JPEGImages', 'labels').replace('jpg','txt'), 'w')
		for j in linesi:
			listj = list(j.strip('\n').split(' '))
			print(listj)
			listj[1] = str(float(listj[1]) * w)
			listj[2] = str(float(listj[2]) * h)
			listj[3] = str(float(listj[1]) + float(listj[3]) * w)
			listj[4] = str(float(listj[2]) + float(listj[4]) * h)
			filei.write(listj[0] + ' ' + listj[1] + ' ' + listj[2] + ' ' + listj[3] + ' ' + listj[4] + '\n')
			print(listj)
		if len(lines):
			len2 =len2 + 1
		filei.close()

fileceshi.close()
if len1 == len2:
	print('all images have processes')


