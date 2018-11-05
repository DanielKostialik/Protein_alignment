from pymol import cmd, stored
import os

def yourFunction():

	# clear
	cmd.delete("all")
	# load 
	prot1 = cmd.load("proteins/1cqm.pdb")
	prot2 = cmd.load("proteins/5wiq.pdb")
	prot3 = cmd.load("proteins/1lou.pdb")


	superp1 = cmd.align("1cqm", "5wiq",0, 0, 0, 0, 0, "result1", "BLOSUM62",0, 0, 1, 0, 1, 0)
	superp2 = cmd.align("1cqm", "1lou",0, 0, 0, 0, 0, "result2", "BLOSUM62",0, 0, 1, 0, 1, 0)


	xyz1 = cmd.get_coords('1cqm', 1)
	xyz2 = cmd.get_coords('result1', 1)
	xyz3 = cmd.get_coords('result2', 1)

	w, h = 3, 300;
	x = [[0 for x in range(w)] for y in range(h)] 

	i = 0
	for a in xyz1:
		for b in xyz2:
			if(a[0] == b[0] and a[1] == b[1] and a[2] == b[2]):
				#print(a[0])
				x[i][0] = a[0]
				x[i][1] = a[1]
				x[i][2] = a[2]
				cmd.color("green", "x ="+str(a[0])+" y ="+str(a[1])+" z ="+str(a[2]) )
				i=i+1



	cmd.color("red", "result1" )
	print("Continue")	
	print(i)
 


cmd.extend( "yourFunction", yourFunction )