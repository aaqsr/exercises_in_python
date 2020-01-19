import numpy as np
#pi = np.radians(180)

#print(np.sin(pi))

#i1 = input("Coordinate one...") #Gets user input in the form (x,y) or x,y or even x y 
#i1r = i1.replace(","," ") #Removes the comma and separates the terms
#i1r2 = i1r.replace(")","") # removes the bracket
#c1 = i1r2.replace("(", "") # removes the other bracket
#Now instead of doing all that in separate lines, we can actually just combo them into one line
c1 = input("Coordinate one...").replace(","," ").replace(")","").replace("(", "") 
x1, y1 = c1.split() #splits the normalised input and stores it into x1 and y1
#print(x1)
#print(y1)

c2 = input("Coordinate two...").replace(","," ").replace(")","").replace("(", "") #same thing but for second coordinate
x2, y2 = c2.split() #splits normalised input and stores it into x2 and y2
#print(x2)
#print(y2)
print("Distance is...")
print(np.sqrt((float(y2)-float(y1))**2 + (float(x2)-float(x1))**2)) #first converts all 4 variables into float then does the calc and prints