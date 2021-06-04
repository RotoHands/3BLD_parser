import time
import keyboard
import pyperclip
import openpyxl

def fix_UD(alg):
    split_alg = alg.split()
    fixed_alg = ""
    for sp in split_alg:
        if 'U' in sp and 'D' in sp:
            D_index = sp.find('D')
            U_index = sp.find('U')
            if U_index > D_index:
                fixed_alg += sp[:U_index] + " "
                fixed_alg += sp[U_index:] + " "
            else:
                fixed_alg += sp[:D_index] + " "
                fixed_alg += sp[D_index:] + " "

        else:
            fixed_alg += sp + " "
    return fixed_alg



def parse_with_2_algs(alg):
    if ")2" in alg:
        rep = 2
        index = alg.find(")2")
        repet = alg[alg.find("(") + 1: alg.find(")2")]
    elif ")3" in alg :
        rep = 3
        index = alg.find(")3")
        repet = alg[alg.find("(") + 1: alg.find(")3")]

    elif ")4" in alg :
        rep = 4
        index = alg.find(")4")
        repet = alg[alg.find("(") + 1: alg.find(")4")]
    else:
        return alg
    temp = []
    for i in range(rep):
        temp.append(repet)
    repet = " ".join(temp)
    final_alg = alg[:alg.find("(")] + repet + alg[index + 2 :]
    final_alg = final_alg.replace(":", ",")
    return final_alg

def removeSlesh(alg):
    if (alg[0] == '[' and alg[len(alg) - 1] == ']' and alg.count("[" )> 1):
        tempAlg = alg[:-1]
        newAlg = tempAlg[1:]
    else:
        newAlg = alg

    if(':' in newAlg):
        finalalg = newAlg.replace(":","")
    else:
        finalalg = newAlg
    return finalalg

def reverseSingal(letter):
    new=""
    length = len(letter)
    if (length == 1):
        return letter + "\'"
    if (length == 2):
        if (letter[1] == "2"):
            return letter
        elif (letter[1] == "\'"):
            return letter[0]
        else:
            return letter[0] + "\'" + letter[1] + "\'"
    if (length == 3):
        if(letter[2] == "\'"):
            if(letter[1] == "2"):
                return letter[0] + letter [1]
            else:
                return letter[0] + "\'" + letter[1]
        else:
            return letter[0] + letter[2] + "\'"
    else:
        return letter[0] + letter[2]

def makeAlg(All, nested = False):
    A = All[0].split()
    B = All[1].split()
    C = All[2].split()
    Arev = []
    Brev = []
    Crev = []
    for x in A:
        Arev.append(reverseSingal(x))
    for x in B:
        Brev.append(reverseSingal(x))
    for x in C:
        Crev.append(reverseSingal(x))
    Arev.reverse()
    Brev.reverse()
    Crev.reverse()
    if nested:
        alg = A + B + Arev
    else:
        alg = C + A + B + Arev +  Brev + Crev
    return alg

def extendAlg(currentAlg):
    C=""
    if (currentAlg.find("[") != 0):
        C = currentAlg[:currentAlg.find("[")].strip()
        tempAlg = currentAlg[currentAlg.find("["):]
    else:
        tempAlg = currentAlg
    A = tempAlg[1:tempAlg.find(",")].strip()
    B = tempAlg[tempAlg.find(",") + 1:tempAlg.find("]")].strip()

    All =[A,B,C]
    return All

def cancel (f,s):
    if(len(f) == 1):
        score1 = 1
    else:
        score1 = [-1,2][f[1] == "2"]
    if (len(s) == 1):
        score2 = 1
    else:
        score2 = [-1, 2][s[1] == "2"]

    sum = score1 + score2
    if (sum == 0 or sum == 4):
        return ""
    if(sum == 1):
        return f[0]
    if (sum == 2 or sum == -2):
        return f[0] + "2"
    if(sum == -1 or sum == 3):
        return f[0] + "\'"

def reverse_alg(alg):
    reversealg =""
    algsplit = alg.split()
    algsplit.reverse()
    for x in algsplit:
        reversealg = reversealg + reverseSingal(x) + " "
    return reversealg

def cancelAlg(alg):
    for i in range (0,len(alg)-1):

        if(alg[i] != ""  and alg[i+1]!=""):
            if (alg[i][0] == alg[i+1][0] ):
                res = cancel(alg[i],alg[i+1])
                if (len(alg[i+1]) == 1):
                    alg[i+1] = ""
                else:
                    if(len(alg[i+1]) == 2):
                        if(alg[i+1][1] == "\'" or alg[i+1][1] == "2"):
                            alg[i + 1] =""

                        else:
                           alg[i + 1] = alg[i+1][1:]
                    else:
                        if (alg[i + 1][1] == "\'" or alg[i + 1][1] == "2"):
                            alg[i + 1] = alg[i + 1][2:]
                        else:
                            alg[i + 1] = alg[i + 1][1:]
                alg[i] = res
    final_alg = []
    for move in alg:
        if move != '':
            final_alg.append(move)
    return final_alg


def alg_maker(comm_str):
    final = ""
    parse = parse_with_2_algs(comm_str)
    parse = parse_with_2_algs(parse)
    parse = parse_with_2_algs(parse)
    clip = fix_UD(parse)
    replace_chars = ["(", ")"]
    for ch in replace_chars:
        clip = clip.replace(ch, "")
    if (clip.find('w') != -1):
        wide_move = clip[clip.index('w')-1]
        alg = clip.replace(wide_move + 'w', wide_move.lower())
    else:
        alg = clip
    if (alg != "None"):
        if (alg.find("[") != -1):
            first_time_open = alg.find("[")
            second_time_open = alg[first_time_open + 1:].find("[")
            if second_time_open != -1 :#nested alg :  [L' U: [F2, U' L U L']]
                first_close = alg.find("]")
                nested_alg = alg_maker(alg[second_time_open:first_close + 1])
                alg = "{}, {}]".format(alg.split(":")[0], nested_alg)
                temp1 = removeSlesh(alg)
                newalg = makeAlg(extendAlg(temp1),True)
            else:
                temp1 = removeSlesh(alg)
                newalg = makeAlg(extendAlg(temp1))

            temp = cancelAlg(cancelAlg(cancelAlg(cancelAlg(newalg))))
            final = ""
            for x in temp:
                final = final + x + " "

            final = final.replace("  ", " ")
            final = final.strip()
        else:
            return clip
    return final

def solve_parser(solve):
    description_words = ["corners", "edges", "parity"]
    solve_split =  solve.split("\r\n")
    if len(solve_split) < 2 and "\n" in solve:
        solve_split = solve.split("\n")
    for a in solve_split:
        if a == '':
            solve_split.remove(a)
    solve = ""
    for comm in solve_split:
        if comm.find("/") != -1:
                comm = comm[:comm.find("/")]
        if comm not in description_words:
            solve += " " + str(alg_maker(comm))
    return (solve, solve_split)
def main():
    pass
if __name__ == '__main__':
    main()
