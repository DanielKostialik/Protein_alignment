from pymol import cmd, stored
import os
from color_by_conservation import color_by_conservation
import socket

def rmsd():

	# clear
	cmd.delete("all")

	# load proteins
	cmd.load("1cqm.pdb", "ref")
	cmd.load("1lou.pdb", "1lou")
	cmd.load("5wiq.pdb", "5wiq")
	cmd.load("6ba8.pdb", "6ba8")
	cmd.load("6ba9.pdb", "6ba9")

	cmd.extra_fit("all", "ref", "align", object = "result", matrix = "BLOSUM62") 


	color_by_conservation(aln="result", as_putty=1)

	cmd.hide("all")
	cmd.show("lines")


cmd.extend( "rmsd", rmsd )


########################  The first try (deprecated) #######################
'''
prot_ref = cmd.load("1cqm.pdb","prot_ref")
prot1 = cmd.load("1lou.pdb", "prot1")

superp1 = cmd.align("prot_ref", "prot1",0, 0, 0, 0, 0, "result1", "BLOSUM62",0, 0, 1, 0, 0, 0)

print(superp1)

xyz_ref = cmd.get_coords('prot_ref', 1)
xyz_result1 = cmd.get_coords('result1', 1)
xyz3 = cmd.get_coords('result2', 1)

w, h = 4, 30000;
x = [[0 for x in range(w)] for y in range(h)] 

i = 0
for a in xyz_ref:
	for b in xyz_result1:
		if(a[0] == b[0] and a[1] == b[1] and a[2] == b[2]):
			#print(a[0])
			x[i][0] = a[0]
			x[i][1] = a[1]
			x[i][2] = a[2]
			x[i][3] = x[i][3] + 1
			cmd.color("green", "x ="+str(a[0])+" y ="+str(a[1])+" z ="+str(a[2]) )
			i=i+1


cmd.color("black", "rank 1-100")

cmd.color("red", "rank 100-1000")

#cmd.color("red", "result1" )
print("Continue")	
#print(i)
'''