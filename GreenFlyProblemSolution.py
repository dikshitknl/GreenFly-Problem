# At first there is only one parent
parent = 'g'
#This list will contain the chil who are not matured yet.
mature = []
flag = 1
a = str()
# Input the no. of days you want to get the population of the green flies.
days = int(input("Enter no. of days:"))
for i in range(0,days+7,7):
	for j in range(7):
		temp = len(parent)*'gggggggg'
		mature.append(temp)
    # Since the child doesn't mature until 7 days. we need to check for that
		if (i+j+1)>6:
			a = mature.pop(0)
			parent += a
		if days==i+j+1:
				flag = 0
				break
	if flag == 0:
		break
# we should consider all the unmatured flies too. This for loop does that
for i in range(len(mature)):
	parent += mature[i]
print('Final result Day:',days,'Total Flies :', len(parent))
