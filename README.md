# 3BLD_parser

## the program get a raw reconstruction (only moves) and output a reconstruction of the comms you used
## the programm can help if:

#### you reconstruct a bld solve but dont want to follow and write the comms but only to trace the actual moves
	
you have a smart cube and you want to auto reconstruct the solution to bld

you look at a reconstruction and the comms are written in [A , B] format' and you want to see the final alg (basicilly after all the cancellations)

## example:
### before 
 U L' L' R' R U' R' L F L' L' F' R L' R' L F R' F' L' R U R U' 
F B' U F' U' F' B L F L' U U' R' U' R' U' D B B D' U R' U R 
U' D F' U F U D' L' U' L D R L' F R' L D R L' F R' L R' U D' 
F U' F' U' D R U U' R' R' D' R U U R' D R U U R U U D' R U' R' 
D R U R' U' U D U R' D R U2 R' D' R D' U D R' D' R U' R' D R D'
R U R' F' R U R' U' R' F R R U' R' U'
### after
U L' L' R' R U' R' L F L' L' F' R L' //UF FD DL

R' L F R' F' L' R U R U' //UF BU RB
F B' U F' U' F' B L F L' //UF UR LU
U U' R' U' R' U' D B B D' U R' U R //UF FR BL
U' D F' U F U D' L' U' L //UF RF FL
D R L' F R' L D R L' F R' L //UF BD RD
R' U D' F U' F' U' D R U //UF LF UR
U' R' R' D' R U U R' D R U U R U //UFR RBU UFL
U D' R U' R' D R U R' U' //UFR RBD FRD
U D U R' D R U2 R' D' R D' //UFR BLD UBL
U D R' D' R U' R' D R D' //UFR FDL UBR
R U R' F' R U R' U' R' F R R U' R' U' //UF UR UFR UBR

