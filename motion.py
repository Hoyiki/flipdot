#python3
li = list(range(-7, 8))
for i in range((len(li))):
	# li[i] = (li[i]/49)**2
	li[i] = int((li[i]/49)**2 * 3000  + 50)
print (li)

