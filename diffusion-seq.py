#!/bin bash
import matplotlib.pyplot as plt
import colorscheme
print("Defining sequences..")
#define sequence
lattice  	= [0	, 0 	,1  	,1  	,2  	,2  	,0  	,0]
lattice_t	= [0	,100	,150	,200	,250	,300	,350	,400]

dmd  	= [0	,0  	,1  	,1]
dmd_t	= [0	,100	,200	,350]

gradient  	= [0	,0  	,1  	,1  	,0  	,0]
gradient_t	= [0	,100	,250	,300	,301	,350]


#plot
plt.plot(lattice_t, lattice, 	color=colorscheme.red)
plt.plot(dmd_t, dmd,         	color=colorscheme.blue)
plt.plot(gradient_t,gradient,	color=colorscheme.green)

plt.show()