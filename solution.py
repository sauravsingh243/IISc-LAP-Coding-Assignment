import random
class Solution:
	def __init__(self):
		pass
		
	def MontyHall(self, N):
		ans = [0.0, 0.0, 0.0, 0]
    		# Write your code here. Please do not change the return statement.
        	# Update ans[0], ans[1], ans[2] and ans[3] as mentioned in the question.
		numberOfDoors = 3
		for i in range(0,N):
    	  		prizeDoor = random.randint(0,2)
    	  		playerChoice = random.randint(0,2)
    			hostChoice = random.randint(0,2)
    			while(hostChoice == playerChoice or hostChoice == prizeDoor):
        			hostChoice = (hostChoice + 1) % numberOfDoors

			# When Player chooses "Always Switch Strategy " 
			playerChoiceSwitch = playerChoice
    			playerChoiceSwitch = (playerChoiceSwitch + 1) % numberOfDoors
    			while(playerChoiceSwitch == hostChoice):
        			playerChoiceSwitch = (playerChoiceSwitch + 1) % numberOfDoors
    			if(playerChoiceSwitch == prizeDoor):
        			ans[0] = ans[0] + 1
			
        		# When Player chooses "Never Switch Strategy "
			if(playerChoice == prizeDoor):
        			ans[1] = ans[1] + 1

			# When Player chooses "All the same Strategy "
			decision = random.randint(0, 1)
            		if decision == 0 and playerChoice == prizeDoor:
                		ans[3] += 1
            		if decision == 1 and playerChoice != prizeDoor:
                		ans[3] += 1
        	
        	return ans
