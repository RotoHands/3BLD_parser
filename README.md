Hi,

After last year software attempt of making a more efficient way to train 3bld, here is this year version!

I worked on a new version for the last couple of months and focused mainly on analyzing 3bld solves.


TL;DR

main features:
- separating the solve commutators
- tracking the commutator and converting to letter pairs
- converting parallel layers to slice moves
- customizable letter pairs
- customizable buffers
- recognize twist, flips and cycles outside the buffer
- recognize mistakes in solve, points to last place execution was right  
- expand commutators to their full alg, after cancelling moves
- compatible with solves from cubedb.net and alg.cubing.net
- can generate url link to cubdb.net
- works on 3style, M2, OP

[github repo](https://github.com/RotoHands/3BLD_parser)
### example solve - smart cube (UF, UFR, Speffz)
<details>
  <summary>unparsed</summary>

<p>
R2 U' B2 F2 L2 U' R2 D F2 U2 B2 R' D' L' D F' D2 B2 D2 L2 //scramble

U' F' B U B U' F B' R B' R' U U' D R' U' D B B U D' R' U D' 
R U' R' U D' F U F' U' D R' F R F' B U' U' F B' R F' R U' U'
L D U' F' U' F U D' L' U' U D' F U' D R' U' R U D' F' D R F' 
L' F R' L D' L D L' D' L' D R L' F' L F R' L U' D' R' U U R'
D R U U R' D' R2 U D D R U R' D R U' R' D D R' U R' D' R U 
U R' D R U R R' D' R D R' D' R U U R' D R D' R' D R U U
</p>
</details>

<details>
  <summary>parsed</summary>

<p>
R2 U' B2 F2 L2 U' R2 D F2 U2 B2 R' D' L' D F' D2 B2 D2 L2 //scramble
//edges
U' S R B R' S' R B' R' U // SQ   10/10
 
U' D R' E' R R E R' U D' // UR   10/20
 
R U' R' E R U R' E' // JF   8/28
 
R' F R S R' R' S' R F' R // EO   10/38
 
U' U' L E' L' U' L E L' U' // PB   10/48
 
E R E' R' U' R E R' D y // TB   9/57
 
R F' L' F M' F' L F L' x' // KG   9/66
 
D' L' D M D' L D M' // HK   8/74


//corners

U' D' R' U U R' D R U U R' D' R2 U D // VN   15/89
 
D R U R' D R U' R' D D // LH   10/99
 
R' U R' D' R U U R' D R U R // OF   12/111
 
R' D' R D R' D' R U U R' D R D' R' D R U U // CA twist   18/129
 
</p>
</details>

### A bit more details

#### Motivation
The main motivation came from the need of making it easier to do deliberate practice in 3bld. Moreover I wanted to make it easier to learn from others solves while still using your letter scheme and make the algs notation more intuitive.
Another reason is that a lot of features of 3bld is missing in current smart cube timers. I wanted to make it easy for them to add the features of supporting 3bld solves to their websites and hope we will see more timers supporting it soon!

#### How it works? A short description of the main problem and solution behind the software.
Last time I attempted to recognize the move of the mistake by tracking the number of pieces solved. This time I wanted to also be able to separate between the algs, but with only tracking the number of solved pieces I didn't manage to find a way to implement it.
I realized that if I am only looking at number of solved pieces I'm ignoring large part the information about the cube state, so decided to change the core idea. I didn't want to get into complicated programming of a cube model, and didn't want do math stuff in order to know how to separate the comms.
I found a very elegant solution to this problem. I represented the cube as a string of 54 chars as usually implemented in the kociemba algorithm. Then I encoded each move to an equal permutation on the chars in the string. Then I saw that if I use Python SequenceMatcher from the difflib, which detects how close are two strings to each other, then it can detect precisely when the commutator ends! 
For example (move - diff between string representation) : D R U R' D R U' R' D D - 0.75, 0.63, 0.52, 0.58, 0.59, 0.54, 0.62, 0.71, 0.73, 0.89 (really pleased from this solution 😊).
Rest of the programming was mainly on adding more features and trying to make it easy as possible to implement on your own.

#### Why these features?
recognize mistakes in solve, points to last place execution were right. this is one of the most time-consuming things I do when I analyze my 3bld solves and I found myself getting frustrated from wasting my time on searching for the mistake.
tracking the commutator and converting to letter pairs. mainly for being able to easily add statics about to comms to a database and later drill the slowest comms.
expand commutators to their full alg, after cancelling moves. Makes it much simpler and intuitive, you don't need to think about inverting the algs, and cancellation become much clearer.
customizable letter pairs. If you want to see other people solves in your letter pair scheme more easily, I think that UBR-UBL-BUFFER notation isn't intuitive enough.
converting parallel layers to slice moves. a main feature in smart cube timers that doesn't exist and is crucial in bld solving. It still isn't perfect, but it is right 90% of the times (you may see rotations in end of algs when parsing smart cube solves. This is a correction I had to add for some cases). this is quite challenging because I didn't find a general solution so I had to program it under several assumptions (see in github files for more information).
compatible with cubedb.net and alg.cubing.net. Mainly to make it as easy as possible to parse the solve you want.

#### Examples of features on [Sebastiano Tronto 22.67 3BLD avg NR](https://www.youtube.com/watch?v=c0R2ZSN_suk) (UR, UBL)
#### Solve 1
<details>
  <summary>parsed</summary>

<p>
Features : Alg extension, move count, gen cubede.net url, letter pair track

`U2 R2 B2 L' U2 L2 R B2 R' B' R D' L' U B2 D' B L' D R Uw'`

`F2 R U2 R' U' R U' R' L' U2 L U L' U L F2`

`[D: [L D' L', U']]`

`[U D' R': [R' D R, U']]`

`[L', U R' U']`

`[R Lw: [U' M' U, R']]`

`[R U R': [S, R2]]`

`[U R U': [S, R2]]`

`[L' U': [U' L' U, M']]`

`[Rw: [U' R' U, M']]`

`[R2 U: [S, R2]]`


</p>
</details>

[cubedb.net](https://www.cubedb.net/?rank=3&title=3BLD_ER_1&scramble=U2_R2_B2_L-_U2_L2_R_B2_R-_B-_R_D-_L-_U_B2_D-_B_L-_D_R_Uw-_&time=26.01&alg=%2F%2Fcorners%0AF2_R_U2_R-_U-_R_U-_R-_L-_U2_L_U_L-_U_L_F2_%2F%2F_BL_twist___16%2F16_%0AD_L_D-_L-_U-_L_D_L-_U_D-_%2F%2F_LD___10%2F26_%0AU_D-_R2_D_R_U-_R-_D-_R_U_R_D_U-_%2F%2F_JV___13%2F39_%0AL-_U_R-_U-_L_U_R_U-_%2F%2F_TI___8%2F47_%0A%2F%2Fedges%0AR_l_U-_M-_U_R-_U-_M_U_R_l-_R-_%2F%2F_HJ___12%2F59_%0AR_U_R-_S_R2_S-_R-_U-_R-_%2F%2F_CV___9%2F68_%0AU_R_U-_S_R2_S-_R2_U_R-_U-_%2F%2F_DT___10%2F78_%0AL-_U2_L-_U_M-_U-_L_U_M_U_L_%2F%2F_FX___11%2F89_%0Ar_U-_R-_U_M-_U-_R_U_M_r-_%2F%2F_KW___10%2F99_%0AR2_U_S_R2_S-_R2_U-_R2_%2F%2F_AC___8%2F107_%0A)
U2 R2 B2 L' U2 L2 R B2 R' B' R D' L' U B2 D' B L' D R Uw' 


//corners

F2 R U2 R' U' R U' R' L' U2 L U L' U L F2 // BL twist   16/16 

D L D' L' U' L D L' U D' // LD   10/26 

U D' R2 D R U' R' D' R U R D U' // JV   13/39 

L' U R' U' L U R U' // TI   8/47 

//edges

R l U' M' U R' U' M U R l' R' // HJ   12/59 

R U R' S R2 S' R' U' R' // CV   9/68 

U R U' S R2 S' R2 U R' U' // DT   10/78 

L' U2 L' U M' U' L U M U L // FX   11/89 

r U' R' U M' U' R U M r' // KW   10/99 

R2 U S R2 S' R2 U' R2 // AC   8/107 

[/SPOILER]

[/SPOILER]

[SPOILER="Solve 2"]

Features: keep comms, raw tracking

[SPOILER="Unparsed"]

L' D2 F2 D2 F2 R D' L U2 B' U2 R F D2 R B' F' Rw Uw


z' y2 

[U D R': [R' D R, U2]]

[R' U: [U, R' D R]]

[L F': [U2, L D L']]

[R, U M' U']

Rw U R' U' M U R U' R' 

[R2, S']

[x': [L E' L', U']]

[L': [L' E L, U2]]

[M: [U', R' E R]] 

[/SPOILER]

[SPOILER="Parsed"]

 z' y2 // memo 


//corners

 [U D R': [R' D R, U2]]// UBL LFU DBL  13/13 

 [R' U: [U, R' D R]]// UBL BRD LFD  11/24 

 [L F': [U2, L D L']]// UBL BUR FUR  12/36 


//edges

 [R, U M' U']// UR FD FR  8/44 

 Rw U R' U' M U R U' R' // UR FU UB  9/53 

 [R2, S']// UR DL DR  4/57 

 [x': [L E' L', U']]// UR LB DB  8/65 

 [L': [L' E L, U2]]// UR RB FL  9/74 

 [M: [U', R' E R]] // UR LF BU  10/84 

[/SPOILER]

[/SPOILER]

[SPOILER="Solve 3"]

[SPOILER="Unparsed"]

F2 L2 R2 D2 L2 D' L2 B U L2 R2 U2 L U' B' F U F U' Rw' Uw

z y2

z' [U' R' U, M'] z 

[Rw U2 Rw', B']

[R D' R': [R' D R, U2]]

[R': [R' D R, U2]]

[R E R', U2]

[L2: [U' M U, L']]

[U' M' U': [M, U2]]

[R' S' R U: [M', U2]] 

[/SPOILER]

[SPOILER="Parsed"]

z y2 // memo 

//edges

z' U' R' U M' U' R U M z // PLS   8/8 

//corners

r U2 r' B' r U2 r' B // HK   8/16 

R D' R2 D R U2 R' D' R U2 R D R' // WC   13/29 

R2 D R U2 R' D' R U2 R // GQ   9/38 

//edges

R E R' U2 R E' R' U2 // DO   8/46 

L2 U' M U L' U' M' U L' // GH   9/55 

U' M' U' M U2 M' U' M U // QI   9/64 

R' S' R U M' U2 M U R' S R // UN   11/75 

[/SPOILER]

[/SPOILER]


Notes:

    if the parsing doesn't work, try to change the DIFF_BETWEEN_ALGS variable between 0.88-0.89
    it is not optimized for cancellations (you see the limitation in Max Hilliard WR solve - here)
    I did most of the developing and testing on 3style solves, so improvements may be needed to M2 and OP
    everything is customizable through the .env file.
    I also have a github repo for drilling 3style algs with smart cube (here), it is a not as easy to clone to yourself (I didn't wrote it very customizable) but I’ll be glad to help!

Hope this will help making 3bld improvement be a lot faster, less frustrating and make more cubers to get into 3bld😊