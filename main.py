import pyperclip
from dotenv import load_dotenv
import os
from BLD_Parser import parse_solve, parse_smart_cube_solve, parse_url

def main():
    load_dotenv()  # load .env variable
    #url = parse_url(pyperclip.paste())
    url = parse_url("https://alg.cubing.net/?alg=_%2F%2F_corners%0AD_U_R-_U-_L2_U_R_U-_L2_D-_%2F%2F_%0Ay2_U_L_D_L-_U-_L_D-_L-_y2_%2F%2F_%0AR-_y_L_D_L-_U2_L_D-_L-_U2_y-_R_%2F%2F_%0AR-_F2_U_L2_U-_L2_U-_F2_U_L2_U_L2_U-_R_%2F%2F_%0AF_U2_R-_D-_R_U2_R-_D_R_F-_%2F%2F_%0A_%2F%2F_edges%0AU_R_U-_M2_U_R-_U-_%2F%2F_%0AU-_L-_U_M2_U-_L_U_%2F%2F_%0AM_U2_M_U2_%2F%2F_%0Ax-_U_L_U-_M2_U_L-_U-_x_%2F%2F_%0AR-_U_R_U-_M2_U_R-_U-_R_%2F%2F_%0AM2_%2F%2F_%0AU_R2_U-_M2_U_R2_U-_%2F%2F_%0Ax-_R_U-_R-_U_M2_U-_R_U_R-_x_%2F%2F_%0AL_U-_L-_U_M2_U-_L_U_L-_%2F%2F_%0Ax-_U-_R_U_M2_U-_R-_U_x_%2F%2F_%0Ax_M_U_M_U_M_U2_M-_U_M-_U_M-_U2_x-_%2F%2F_&setup=L2_U-_F2_U2_B2_D_B2_D_F-_L_R_U2_R_F_L_R2_D_L_B&type=reconstruction&title=Arlen%20Tan")
    url = parse_url("https://www.cubedb.net/?rank=3&title=example_solve&scramble=R2_D-_R2_B2_D-_R2_F2_D-_U2_L-_D2_R-_F2_L-_D_L-_U-_B-_L-_D_Rw&time=50.7&alg=x_y-_%2F%2F_%0A%5BF%2C_R_S-_R-%5D_%2F%2F_%0A%5BUw_L-%3A_%5BE%2C_L2%5D%5D_%2F%2F_%0A%5BU-%3A_%5BS%2C_R2%5D%5D_%2F%2F_%0A%5BLw-%3A_%5BU-_L_U%2C_M-%5D%5D_%2F%2F_%0A%5BR-_E_R%2C_U-%5D_%2F%2F_%0A_%2F%2F_%0A%5BU-_R_U%3A_%5BR-_D_R%2C_U2%5D%5D_%2F%2F_%0A%5BR_D_R-_D-_U%3A_%5BR_D_R-%2C_U2%5D%5D_%2F%2F_%0A%5BU2%2C_R-_D-_R%5D_%2F%2F_%0AR-_U_B2_U-_R_U_R-_B2_R_U-_%2F%2F_%0AR-_F_R2_U-_R-_U-_R_U_R-_F-_R_U_R-_U-_%2F%2F_")
    SCRAMBLE = url["scramble"]
    SOLVE = url["alg"]

    use_txt_file= True if os.environ.get('USE_TXT_FILE') == "True" else False
    if use_txt_file:
        with open(os.environ.get("TXT_FILE_OF_SOLVE"), "r") as f:
            data = f.readlines()
            SCRAMBLE = data[0]
            SOLVE = " ".join(data[1:])
    cube = parse_solve(SCRAMBLE, SOLVE)
    if cube.smart_cube:
        cube = parse_smart_cube_solve(cube)
    solve_str = cube.url
    pyperclip.copy(solve_str)

    print(solve_str)
    #print(*cube.solve_stats, sep="\n")

if __name__ == '__main__':
    main()
