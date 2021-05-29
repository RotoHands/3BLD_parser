import pyperclip
from dotenv import load_dotenv
import os
from BLD_Parser import parse_solve, parse_smart_cube_solve, parse_url

def main():
    load_dotenv()  # load .env variable
    url = parse_url("https://www.cubedb.net/?rank=3&title=example_solve&scramble=R2_D-_R2_B2_D-_R2_F2_D-_U2_L-_D2_R-_F2_L-_D_L-_U-_B-_L-_D_Rw&time=50.7&alg=x_y-_%2F%2F_%0A%5BF%2C_R_S-_R-%5D_%2F%2F_%0A%5BUw_L-%3A_%5BE%2C_L2%5D%5D_%2F%2F_%0A%5BU-%3A_%5BS%2C_R2%5D%5D_%2F%2F_%0A%5BLw-%3A_%5BU-_L_U%2C_M-%5D%5D_%2F%2F_%0A%5BR-_E_R%2C_U-%5D_%2F%2F_%0A_%2F%2F_%0A%5BU-_R_U%3A_%5BR-_D_R%2C_U2%5D%5D_%2F%2F_%0A%5BR_D_R-_D-_U%3A_%5BR_D_R-%2C_U2%5D%5D_%2F%2F_%0A%5BU2%2C_R-_D-_R%5D_%2F%2F_%0AR-_U_B2_U-_R_U_R-_B2_R_U-_%2F%2F_%0AR-_F_R2_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_%2F%2F_")
    SCRAMBLE = url["scramble"]
    SOLVE = url["alg"]
    print(SOLVE)
    use_clipboard = True if os.environ.get('USE_CLIPBOARD') == "True" else False
    if not use_clipboard:
        with open(os.environ.get("TXT_FILE_OF_SOLVE"), "r") as f:
            data = f.readlines()
            SCRAMBLE = data[0]
            SOLVE = data[1]
    # SOLVE = "x2 z' R' U' R' E' R2 E R' U R  S' Lw D Lw' S Lw D' Lw'  U L' E Lw U' Lw' E' Lw U M' U'  L' M U M' U2 M U L M'  U' S R' F' R S' R' F R   R D' R' U R' D R U R' D' R U' R D  U' D R' D R U2 R' D' R U' D'  U R' D R U' R' D'   U R U' R U R' F' R U R' U' R' F R2 U' R2 U' "
    # SOLVE = pyperclip.paste()
    cube = parse_solve(SCRAMBLE, SOLVE)
    if cube.smart_cube:
        cube = parse_smart_cube_solve(cube)

    solve_str = cube.url
    pyperclip.copy(solve_str)
    # print(solve_str)
    # print(*cube.solve_stats, sep="\n")

if __name__ == '__main__':
    main()