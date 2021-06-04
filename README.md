Hi,
After [last year](https://www.speedsolving.com/threads/3bld-dnf-analyzer-new-software-i-made.76945/) software attempt of making a more efficient way to train 3bld, here is this year version!
I worked on a new version for the last couple of months and focused mainly on analyzing 3bld solves.

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
checkout this [post](https://www.speedsolving.com/threads/smart-cube-bld-analyzer.84773/)