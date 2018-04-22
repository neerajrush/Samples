#from Set import set
#A thief trying to escape from a jail has to cross N walls each with varying heights. He climbs X feet every time. But, due to the slippery nature of those walls, every times he slips back by Y feet.  Now the task is to calculate the total number of jumps required to cross all walls and escape from the jail.

#Input:
#The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two space separated integers X, Y, N. Then in the next line are N space separated values denoting the heights ( Ht[] ) of the walls.
#
#Output:
#For each test case in a new line print the total number of jumps.

#Constraints:
#1<=T<=100
#1<= N, X, Y <=100
#1<= Ht[] <=1000

#Example:
#Input:
#2
#10 1 1
#5
#4 1 5
#6 9 11 4 5 

#Output:
#1
#12

def numberOfAppttempts(nWalls, wallsHeight, jump, slip):
	nattempts = 0
	for i in range(nWalls):
		if jump >= wallsHeight[i]:
			nattempts += 1
		else:
			nattempts += 1
			j = jump
			while (j < wallsHeight[i]):
				j -= slip 	
				nattempts += 1
				j += jump
        
	return nattempts

if __name__=='__main__':
    print ("-------------------")
    wh1 = [5]
    x = numberOfAppttempts(1, wh1, 10, 1)
    print (x)
    print ("-------------------")
    wh2 = [6, 9, 11, 4, 5]
    y = numberOfAppttempts(5, wh2, 4, 1)
    print (y)
    print ("-------------------")
