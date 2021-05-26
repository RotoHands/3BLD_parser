import pyperclip
from dotenv import load_dotenv
import os
from BLD_Parser import parse_solve, parse_smart_cube_solve

if __name__ == '__main__':
    load_dotenv()  # load .env variable
    SOLVE = pyperclip.paste()  # get the solve from the clipboard. I found it more comfortable
    SCRAMBLE = "R2 D' R2 B2 D' R2 F2 D' U2 L' D2 R' F2 L' D L' U' B' L' D Rw "
    use_clipboard = True if os.environ.get('USE_CLIPBOARD') == "True" else False
    if not use_clipboard:
        with open(os.environ.get("TXT_FILE_OF_SOLVE"), "r") as f:
            data = f.readlines()
            SCRAMBLE = data[0]
            SOLVE = data[1]

    cube = parse_solve(SCRAMBLE, SOLVE)
    if cube.smart_cube:
        cube = parse_smart_cube_solve(cube)

    solve_str = cube.url
    pyperclip.copy(solve_str)
    print(solve_str)