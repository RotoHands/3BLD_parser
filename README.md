# 3BLD_parser

## the program get a raw reconstruction (only moves) and output a reconstruction of the comms you used
## the programm can help if:

you reconstruct a bld solve but dont want to follow and write the comms but only to trace the actual moves  
you have a smart cube and you want to auto reconstruct the solution to bld (checkout my smart cube DNF analyzer [repo](https://github.com/RotoHands/RotoDNF_analyzer))  
you look at a reconstruction and the comms are written in [A , B] format' and you want to see the final alg (basicilly after all the cancellations)


UF -> UB -> LB
U' R U' D B' U U B U D' R' U'
U' R E' y' B' U U B E y R' U'
U' R E' R' U U R E R' U'



## example:
scramble  
L2 U R2 F2 R2 B2 D2 U F2 U L2 R B L' F D L' D' L2 F2 U'
### before 
 U L' L' R' R U' R' L F L' L' F' R L' R' L F R' F' L' R U R U' 
F B' U F' U' F' B L F L' U U' R' U' R' U' D B B D' U R' U R 
U' D F' U F U D' L' U' L D R L' F R' L D R L' F R' L R' U D' 
F U' F' U' D R U U' R' R' D' R U U R' D R U U R U U D' R U' R' 
D R U R' U' U D U R' D R U2 R' D' R D' U D R' D' R U' R' D R D'
R U R' F' R U R' U' R' F R R U' R' U'  
[Cubedb](https://www.cubedb.net/?rank=3&title=3BLD_Parser&scramble=L2_U_R2_F2_R2_B2_D2_U_F2_U_L2_R_B_L-_F_D_L-_D-_L2_F2_U-_&alg=_U_L-_L-_R-_R_U-_R-_L_F_L-_L-_F-_R_L-_R-_L_F_R-_F-_L-_R_U_R_U-_%0AF_B-_U_F-_U-_F-_B_L_F_L-_U_U-_R-_U-_R-_U-_D_B_B_D-_U_R-_U_R_%0AU-_D_F-_U_F_U_D-_L-_U-_L_D_R_L-_F_R-_L_D_R_L-_F_R-_L_R-_U_D-_F_U-_F-_U-_D_R_U_U-_R-_R-_D-_R_U_U_R-_D_R_U_U_R_U_U_D-_R_U-_R-_D_R_U_R-_U-_U_D_U_R-_D_R_U2_R-_D-_R_D-_U_D_R-_D-_R_U-_R-_D_R_D-_R_U_R-_F-_R_U_R-_U-_R-_F_R_R_U-_R-_U-%0A)

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

[Cubedb](https://www.cubedb.net/?rank=3&title=3BLD_Parser&scramble=L2_U_R2_F2_R2_B2_D2_U_F2_U_L2_R_B_L-_F_D_L-_D-_L2_F2_U-_&alg=_U_L-_L-_R-_R_U-_R-_L_F_L-_L-_F-_R_L-_%2F%2FUF_FD_DL%0AR-_L_F_R-_F-_L-_R_U_R_U-_%2F%2FUF_BU_RB%0AF_B-_U_F-_U-_F-_B_L_F_L-_%2F%2FUF_UR_LU%0AU_U-_R-_U-_R-_U-_D_B_B_D-_U_R-_U_R_%2F%2FUF_FR_BL%0AU-_D_F-_U_F_U_D-_L-_U-_L_%2F%2FUF_RF_FL%0AD_R_L-_F_R-_L_D_R_L-_F_R-_L_%2F%2FUF_BD_RD%0AR-_U_D-_F_U-_F-_U-_D_R_U_%2F%2FUF_LF_UR%0AU-_R-_R-_D-_R_U_U_R-_D_R_U_U_R_U_%2F%2FUFR_RBU_UFL%0AU_D-_R_U-_R-_D_R_U_R-_U-_%2F%2FUFR_RBD_FRD%0AU_D_U_R-_D_R_U2_R-_D-_R_D-_%2F%2FUFR_BLD_UBL%0AU_D_R-_D-_R_U-_R-_D_R_D-_%2F%2FUFR_FDL_UBR%0AR_U_R-_F-_R_U_R-_U-_R-_F_R_R_U-_R-_U-_%2F%2FUF_UR_UFR_UBR%0A)


## Features  
- you can implement your own letter scheme so you will see letter pairs insted of UFR, UF...
- you can customize it to your buffers
- if you DNFed due to execution error, it can auto detect where the mistake was
- generates link to Cubedb of the solve
