from bld_comm_parser import solve_parser, reverse_alg, alg_maker
import permutation
import re
from difflib import SequenceMatcher
from dotenv import load_dotenv
import os
def ERROR_FUNC():
    print("unknown move: ")

class Cube:
    def __init__(self):
        self.dict_moves = {1: "U", 2: "U", 3: "U", 4: "U", 5: "U", 6: "U", 7: "U", 8: "U", 9: "U", 10: "R", 11: "R", 12: "R",
              13: "R", 14: "R", 15: "R", 16: "R", 17: "R", 18: "R", 19: "F", 20: "F", 21: "F", 22: "F", 23: "F",
              24: "F", 25: "F", 26: "F", 27: "F", 28: "D", 29: "D", 30: "D", 31: "D", 32: "D", 33: "D", 34: "D",
              35: "D", 36: "D", 37: "L", 38: "L", 39: "L", 40: "L", 41: "L", 42: "L", 43: "L", 44: "L", 45: "L",
              46: "B", 47: "B", 48: "B", 49: "B", 50: "B", 51: "B", 52: "B", 53: "B", 54: "B"}

        self.dict_stickers = {1: "UBL", 3: "UBR", 7: "UFL", 9: "UFR", 10: "RFU", 12: "RBU", 16: "RFD", 18: "RBD", 19: "FUL", 21: "FUR" , 25: "FDL",27: "FRD", 28: "DFL", 30: "DFR", 34: "DBL", 36: "DBR", 37: "LBU", 39: "LFU", 43: "LDB", 45: "LFD", 46: "BUR", 48: "BUL", 52: "BRD", 54: "BLD", 2: "UB", 4: "UL", 6: "UR", 8: "UF", 11: "RU", 13: "RF", 15: "RB", 17: "RD", 20: "FU", 22: "FL", 24: "FR", 26: "FD", 29: "DF", 31: "DL", 33: "DR", 35: "DB", 38: "LU", 40: "LB", 42: "LF", 44: "LD", 47: "BU", 49: "BR", 51: "BL", 53: "BD" }

        self.gen_with_moves = None
        self.smart_cube = None
        self.gen_parsed_to_cubedb = None
        self.comms_unparsed_bool = None
        self.gen_with_move_count = None
        self.diff_to_solved_state = None
        self.parse_to_lp = None
        self.buffer_ed = None
        self.buffer_cor = None
        self.path_to_lp = None
        self.name_of_solve = None
        self.time_solve = None
        self.algs_executed = []
        self.init_vars()

        self.currently_parsing_smart_cube = False
        self.corners_numbers = [1, 3, 7, 9, 10, 12, 16, 18, 19, 21, 25, 27, 28, 30, 34, 36, 37, 39, 43, 45, 46, 48, 52, 54]
        self.edges_numbers = [2, 4, 6, 8, 11, 13, 15, 17, 20, 22, 24, 26, 29, 31, 33, 35, 38, 40, 42, 44, 47, 49, 51, 53]
        self.current_perm_list = []
        self.solved_edges = 0
        self.solved_corners = 0
        self.solved_perm = permutation.Permutation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,54)
        self.solve_stats = []
        self.current_perm = self.solved_perm
        self.flag_piece_type = ""
        self.comms_unparsed = []
        self.scramble = ""
        self.solve = ""
        self.solve_helper = ""
        self.url = ""
        self.current_max_perm_list = None
        self.current_max_perm = None
        self.parity = None
        self.max_edges = 12
        self.rotation = ['x', 'x\'', 'x2', 'z', 'z\'', 'z2', 'y', 'y\'', 'y2']
        self.last_solved_pieces = {}
        self.current_facelet = ""

        self.R = permutation.Permutation(1, 2, 21, 4, 5, 24, 7, 8, 27, 16, 13, 10, 17, 14, 11, 18, 15, 12, 19, 20, 30, 22, 23, 33, 25, 26, 36, 28, 29, 52, 31, 32, 49, 34, 35, 46, 37, 38, 39, 40, 41,42, 43, 44, 45, 9, 47, 48, 6, 50, 51, 3, 53, 54).inverse()
        self.RP = self.R.inverse()
        self.R2 = self.R * self.R
        self.L = permutation.Permutation(54, 2, 3, 51, 5, 6, 48, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 20, 21, 4,23, 24, 7, 26, 27, 19, 29, 30, 22, 32, 33, 25, 35, 36, 43, 40, 37, 44, 41, 38,45, 42, 39, 46, 47, 34, 49, 50, 31, 52, 53, 28).inverse()
        self.LP = self.L.inverse()
        self.L2 = self.L * self.L
        self.D = permutation.Permutation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 25, 26, 27, 19, 20, 21, 22, 23, 24, 43, 44, 45, 34, 31, 28, 35, 32, 29, 36, 33, 30, 37, 38, 39, 40, 41, 42, 52, 53, 54, 46, 47, 48, 49, 50, 51, 16, 17, 18).inverse()
        self.DP = self.D.inverse()
        self.D2 = self.D * self.D
        self.B = permutation.Permutation(12, 15, 18, 4, 5, 6, 7, 8, 9, 10, 11, 36, 13, 14, 35, 16, 17, 34, 19, 20, 21,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 37, 40, 43, 3, 38, 39, 2, 41,42, 1, 44, 45, 52, 49, 46, 53, 50, 47, 54, 51, 48).inverse()
        self.BP = self.B.inverse()
        self.B2 = self.B * self.B
        self.U = permutation.Permutation(7, 4, 1, 8, 5, 2, 9, 6, 3, 46, 47, 48, 13, 14, 15, 16, 17, 18, 10, 11, 12, 22,23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 19, 20, 21, 40, 41, 42,43, 44, 45, 37, 38, 39, 49, 50, 51, 52, 53, 54).inverse()
        self.UP = self.U.inverse()
        self.U2 = self.U * self.U
        self.F = permutation.Permutation(1, 2, 3, 4, 5, 6, 45, 42, 39, 7, 11, 12, 8, 14, 15, 9, 17, 18, 25, 22, 19, 26,23, 20, 27, 24, 21, 16, 13, 10, 31, 32, 33, 34, 35, 36, 37, 38, 28, 40, 41, 29,43, 44, 30, 46, 47, 48, 49, 50, 51, 52, 53, 54).inverse()
        self.FP = self.F.inverse()
        self.F2 = self.F * self.F
        self.M = permutation.Permutation(1, 53, 3, 4, 50, 6, 7, 47, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 21, 22, 5, 24, 25, 8, 27, 28, 20, 30, 31, 23, 33, 34, 26, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 35, 48, 49, 32, 51, 52, 29, 54).inverse()
        self.MP = self.M.inverse()
        self.M2 = self.M * self.M
        self.S = permutation.Permutation(1, 2, 3, 44, 41, 38, 7, 8, 9, 10, 4, 12, 13, 5, 15, 16, 6, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 17, 14, 11, 34, 35, 36, 37, 31, 39, 40, 32, 42, 43, 33, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54).inverse()
        self.SP = self.S.inverse()
        self.S2 = self.S * self.S
        self.E = permutation.Permutation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 23, 24, 16, 17, 18, 19, 20, 21, 40, 41, 42, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 49, 50, 51, 43, 44, 45, 46, 47, 48, 13, 14, 15, 52, 53, 54).inverse()
        self.EP = self.E.inverse()
        self.E2 = self.E * self.E

    def init_vars(self):
        """
        initiate the environment variables from .env file to the class attributes
        """

        load_dotenv()
        self.smart_cube = True if os.environ.get("SMART_CUBE") == "True" else False
        self.gen_parsed_to_cubedb = True if os.environ.get("GEN_PARSED_TO_CUBEDB") == "True" else False
        self.name_of_solve = os.environ.get("NAME_OF_SOLVE")
        self.time_solve = os.environ.get("TIME_SOLVE")
        self.comms_unparsed_bool = True if os.environ.get("COMMS_UNPARSED") == "True" else False
        self.gen_with_move_count = True if os.environ.get("GEN_WITH_MOVE_COUNT") == "True" else False
        self.diff_to_solved_state = float(os.environ.get("DIFF_BETWEEN_ALGS"))
        self.parse_to_lp = True if os.environ.get("PARSE_TO_LETTER_PAIR") == "True" else False
        self.gen_with_moves = True if os.environ.get("GEN_WITH_MOVE_COUNT") == "True" else False
        self.buffer_ed = self.get_buffer_ed(os.environ.get("EDGES_BUFFER"))
        self.buffer_cor = self.get_buffer_cor(os.environ.get("CORNER_BUFFER"))
        self.path_to_lp = os.environ.get("PATH_LETTER_PAIR_FILE")
        self.dict_lp = self.load_letter_pairs_dict()

    def r(self):
        self.current_perm =  self.R * self.current_perm
    def rp(self):
        self.current_perm =  self.RP * self.current_perm
    def r2(self):
        self.current_perm = self.R2 * self.current_perm
    def l(self):
        self.current_perm =  self.L * self.current_perm
    def lp(self):
        self.current_perm = self.LP * self.current_perm
    def l2(self):
        self.current_perm =  self.L * self.L * self.current_perm
    def d(self):
        self.current_perm =  self.D * self.current_perm
    def dp(self):
        self.current_perm = self.DP * self.current_perm
    def d2(self):
        self.current_perm = self.D * self.D * self.current_perm
    def b(self):
        self.current_perm =  self.B * self.current_perm
    def bp(self):
        self.current_perm = self.BP * self.current_perm
    def b2(self):
        self.current_perm = self.B * self.B * self.current_perm
    def u(self):
        self.current_perm =  self.U * self.current_perm
    def up(self):
        self.current_perm = self.UP * self.current_perm
    def u2(self):
        self.current_perm = self.U * self.U * self.current_perm
    def f(self):
        self.current_perm =  self.F * self.current_perm
    def fp(self):
        self.current_perm = self.FP * self.current_perm
    def f2(self):
        self.current_perm = self.F * self.F * self.current_perm
    def m(self):
        self.current_perm = self.M * self.current_perm
    def mp(self):
        self.current_perm = self.MP * self.current_perm
    def m2(self):
        self.current_perm = self.M * self.M * self.current_perm
    def e(self):
        self.current_perm = self.E * self.current_perm
    def ep(self):
        self.current_perm = self.EP * self.current_perm
    def e2(self):
        self.current_perm = self.E * self.E * self.current_perm
    def s(self):
        self.current_perm = self.S * self.current_perm
    def sp(self):
        self.current_perm = self.SP * self.current_perm
    def s2(self):
        self.current_perm = self.S * self.S * self.current_perm
    def rw(self):
        self.current_perm = self.R * self.current_perm
        self.current_perm = self.MP * self.current_perm
    def rwp(self):
        self.current_perm = self.RP * self.current_perm
        self.current_perm = self.M * self.current_perm
    def rw2(self):
        self.current_perm = self.R * self.R * self.current_perm
        self.current_perm = self.MP * self.MP *  self.current_perm
    def lw(self):
        self.current_perm = self.L * self.current_perm
        self.current_perm = self.M * self.current_perm
    def lwp(self):
        self.current_perm = self.LP * self.current_perm
        self.current_perm = self.MP * self.current_perm
    def lw2(self):
        self.current_perm = self.L * self.L * self.current_perm
        self.current_perm = self.M * self.M *  self.current_perm
    def uw(self):
        self.current_perm = self.U * self.current_perm
        self.current_perm = self.EP * self.current_perm
    def uwp(self):
        self.current_perm = self.UP * self.current_perm
        self.current_perm = self.E * self.current_perm
    def uw2(self):
        self.current_perm = self.U * self.U * self.current_perm
        self.current_perm = self.EP * self.EP *  self.current_perm
    def dw(self):
        self.current_perm = self.D * self.current_perm
        self.current_perm = self.E * self.current_perm
    def dwp(self):
        self.current_perm = self.DP * self.current_perm
        self.current_perm = self.EP * self.current_perm
    def dw2(self):
        self.current_perm = self.D * self.D * self.current_perm
        self.current_perm = self.D * self.D *  self.current_perm
    def fw(self):
        self.current_perm = self.F * self.current_perm
        self.current_perm = self.S * self.current_perm
    def fwp(self):
        self.current_perm = self.FP * self.current_perm
        self.current_perm = self.SP * self.current_perm
    def fw2(self):
        self.current_perm = self.F * self.F * self.current_perm
        self.current_perm = self.S * self.S *  self.current_perm
    def bw(self):
        self.current_perm = self.B * self.current_perm
        self.current_perm = self.SP * self.current_perm
    def bwp(self):
        self.current_perm = self.BP * self.current_perm
        self.current_perm = self.S * self.current_perm
    def bw2(self):
        self.current_perm = self.B * self.B * self.current_perm
        self.current_perm = self.SP * self.SP *  self.current_perm
    def x(self):
        self.rw()
        self.lp()
    def xp(self):
        self.rwp()
        self.l()
    def x2(self):
        self.x()
        self.x()
    def y(self):
        self.uw()
        self.dp()
    def yp(self):
        self.uwp()
        self.d()
    def y2(self):
        self.y()
        self.y()
    def z(self):
        self.fw()
        self.bp()
    def zp(self):
        self.fwp()
        self.b()
    def z2(self):
        self.z()
        self.z()

    def singlemoveExecute(self, move):
        funcMoves = {
        'R': self.r,
        'R\'': self.rp,
        'R2': self.r2,
        'R2\'': self.r2,
        'L': self.l,
        'L\'': self.lp,
        'L2': self.l2,
        'L2\'': self.l2,
        'F': self.f,
        'F\'': self.fp,
        'F2': self.f2,
        'F2\'': self.f2,
        'B': self.b,
        'B\'': self.bp,
        'B2': self.b2,
        'B2\'': self.b2,
        'D': self.d,
        'D\'': self.dp,
        'D2': self.d2,
        'D2\'': self.d2,
        "U": self.u,
        'U\'': self.up,
        'U2': self.u2,
        'U2\'': self.u2,
        "S": self.s,
        'S\'': self.sp,
        'S2': self.s2,
        'S2\'': self.s2,
        "E": self.e,
        'E\'': self.ep,
        'E2': self.e2,
        'E2\'': self.e2,
        "M": self.m,
        'M\'': self.mp,
        'M2': self.m2,
        'M2\'': self.m2,
        "r": self.rw,
        'r\'': self.rwp,
        'r2': self.rw2,
        'r2\'': self.rw2,
        "Rw": self.rw,
        'Rw\'': self.rwp,
        'Rw2': self.rw2,
        'Rw2\'': self.rw2,
        "l": self.lw,
        'l\'': self.lwp,
        'l2': self.lw2,
        'l2\'': self.lw2,
        "Lw": self.lw,
        'Lw\'': self.lwp,
        'Lw2': self.lw2,
        'Lw2\'': self.lw2,
        "f": self.fw,
        'f\'': self.fwp,
        'f2': self.fw2,
        'f2\'': self.fw2,
        "Fw": self.fw,
        'Fw\'': self.fwp,
        'Fw2': self.fw2,
        'Fw2\'': self.fw2,
        "d": self.dw,
        'd\'': self.dwp,
        'd2': self.dw2,
        'd2\'': self.dw2,
        "Dw": self.dw,
        'Dw\'': self.dwp,
        'Dw2': self.dw2,
        'Dw2\'': self.dw2,
        "b": self.bw,
        'b\'': self.bwp,
        'b2': self.bw2,
        'b2\'': self.bw2,
        "Bw": self.bw,
        'Bw\'': self.bwp,
        'Bw2': self.bw2,
        'Bw2\'': self.bw2,
        "u": self.uw,
        'u\'': self.uwp,
        'u2': self.uw2,
        'u2\'': self.uw2,
        "Uw": self.uw,
        'Uw\'': self.uwp,
        'Uw2': self.uw2,
        'Uw2\'': self.uw2,
        'x': self.x,
        'x\'': self.xp,
        'x2': self.x2,
        "x2'": self.x2,
        'y': self.y,
        'y\'': self.yp,
        'y2': self.y2,
        "y2'": self.y2,
        'z': self.z,
        'z\'': self.zp,
        'z2': self.z2,
        "z2'": self.z2

    }
        funcMoves.get(move)()

    def get_buffer_cor(self, cor_name):
        """
        gets the corner buffer name and return its number in the cube permutation
        """

        for i in range(1,55):
            if  i in self.dict_stickers:
                if self.dict_stickers[i] == cor_name:
                    return i
        cor_name = "{}{}{}".format(cor_name[0], cor_name[2], cor_name[1])

        for i in range(1, 55):
            if i in self.dict_stickers:
                if self.dict_stickers[i] == cor_name:
                    return i
    def get_buffer_ed(self, ed_name):
        """
        gets the edge buffer name and return its number in the cube permutation
        """
        for i in range(1,55):
            if i in self.dict_stickers:
                if self.dict_stickers[i] == ed_name:
                    return i

    def load_letter_pairs_dict(self):
        """
        gets a text file with list of place in cube and its letter pair ("ULB" : "A").
        returns a dictionary object of { place : letter_pair }
        """

        with open(self.path_to_lp ,"r", encoding="utf-8") as f:
            dict_lp = {}
            file = f.readlines()
            for line in file:
                split_data = re.findall('"([^"]*)"', line)
                dict_lp[split_data[0]] = split_data[1]
        return (dict_lp)

    def string_permutation(self, a,b):
        """
        gets two str that represent place on the cube (UFR, DF...)
        if they are the same piece, returns True (UFR, RFU)
        """
        for c in a:
            if c not in b:
                return False
        return True

    def string_permutation_list(self, elem, list):
        """
        gets an str and a list of str.
        returns True if the element is the same piece of another element in the list (UFR, [LUB, DBL, RFU])
        """
        for elem_list in list:
            if self.string_permutation(elem_list,elem):
                return True
        return False

    def diff_states(self, perm_list):
        """
        gets two permutation of cubes, converts to str and returns the difference between them using SequenceMatcher.
        this is the core algorithm of the whole software. it comes from the idea that when you solve bld then you
        solve small amount of pieces each time ==> the similarity between their string representation will be high,
        and we can find the separation between the different comms!
        """

        return SequenceMatcher(None, self.perm_to_string(self.current_max_perm_list), perm_list).ratio()

    def check_slice(self, m1, m2):
        """
        gets two moves, returns the equivalent slice and rotation move or None
        this is used to overcome the issue of smart cube, that they can't detect slice moves
        """

        if m1 == "U'" and m2 == "D" or m2 == "U'" and m1 == "D":
            return "E' y'"
        if m1 == "U" and m2 == "D'" or m2 == "U" and m1 == "D'":
            return "E y"
        if m1 == "R" and m2 == "L'" or m2 == "R" and m1 == "L'":
            return "M x"
        if m1 == "R'" and m2 == "L" or m2 == "R'" and m1 == "L":
            return "M' x'"
        if m1 == "F" and m2 == "B'" or m2 == "F" and m1 == "B'":
            return "S' z"
        if m1 == "F'" and m2 == "B" or m2 == "F'" and m1 == "B":
            return "S z'"

        return None
    def parse_rotation_from_alg(self, final_alg):
        """
        gets an alg with rotation in it. applies the rotation to the alg so that no rotation are in it.
        U' R E' y' B' U U B E y R' U' --> U' R E' R' U U R E R' U'
        """
        alg_apply_rot = []
        self.solve_helper = final_alg

        while final_alg:
            if final_alg[0] in self.rotation:
                if len(final_alg) > 1:
                    self.solve_helper = " ".join(final_alg[1:])
                    self.apply_rotation(final_alg[0])
                    final_alg.pop(0)
                    final_alg = self.solve_helper.split()
                else:
                    final_alg.pop(0)
            else:
                alg_apply_rot.append(final_alg.pop(0))
        return  alg_apply_rot

    def parse_alg_to_slice_moves(self, alg):
        """
        gets an alg str from smart cube. converts it to the slice moves applied
        U' R U' D B' U U B U D' R' U' --> U' R E' R' U U R E R' U'

        this is also a main part of the software, how it works?
        1. it apllies only on edges alg (you dont do slice moves in corners solving in 3style)
        2. coverts parallel faces to a slice move
        3. in special cases (such as U' D R' E R2 E' R' U D') it only converts the middle parallel faces to slice moves
        """
        temp_cube = Cube()
        alg_list = alg.split()
        rev_alg = reverse_alg(alg)
        final_alg = []
        temp_cube.solve_helper = alg
        center = temp_cube.current_perm(5)
        while alg_list:
            slice_move = None
            if len(alg_list) > 1:
                slice_move = temp_cube.check_slice(alg_list[0], alg_list[1])
            if slice_move:
                for m in slice_move.split():
                    final_alg.append(m)
                    alg_list.pop(0)
            else:
                final_alg.append(alg_list[0])
                alg_list.pop(0)
        alg_apply_rot = temp_cube.parse_rotation_from_alg(final_alg)
        final = []
        final_alg_str = " ".join(alg_apply_rot)
        if final_alg_str.count('E') == 4:
            found = 0
            for i in range(len(alg_apply_rot)):
                if alg_apply_rot[i] == 'E' or alg_apply_rot[i] == "E'":
                    found += 1
                    if found == 1 or found == 4:
                        if alg_apply_rot[i] == 'E':
                            final.append("U")
                            final.append("D'")
                            final.append("y'")
                        if alg_apply_rot[i] == "E'":
                            final.append("U'")
                            final.append("D")
                            final.append("y")
                    else:
                        final.append(alg_apply_rot[i])
                else:
                    final.append(alg_apply_rot[i])



            final_alg_str =" ".join(temp_cube.parse_rotation_from_alg(final))
        check_orientation_cube = Cube()
        check_orientation_cube.solve = final_alg_str
        check_orientation_cube.currently_parsing_smart_cube = True

        fix = check_orientation_cube.fix_rotation()
        final_alg_str += " " + " ".join(fix)
        return final_alg_str



    def gen_solve_to_text(self):
        """
        generates the solve to a text format
        """

        count = 0
        self.url = "scramble: \n"
        for move in self.scramble.split():
            self.url += "{} ".format(move)
        self.url += "\n\nsolve:\n"

        for move in self.solve_stats:
            if self.comms_unparsed_bool:
                if move["comment"] != "":
                    if "mistake" in move["comment"]:
                        move["comment"] = "{}\n//{}".format(move["comment"].split("mistake")[0], "mistake from here")
                    if "#" in move["comment"]:
                        piece = move["comment"].split("#")[0]
                        move["comment"] = move["comment"].split("#")[1]
                        if self.url.rfind("\n") != -1:
                            alg = self.url[self.url.rfind("\n") + 1:]
                            self.url = self.url[:self.url.rfind("\n") + 1] + "\n//{}\n".format(piece) + alg
                    self.url += self.comms_unparsed[count]
                    count += 1
                    self.url += "// {} \n".format(move["comment"])
            else:
                if "move" in move:
                    if move["move"] != "":
                        self.url += "{} ".format(move["move"])
                if move["comment"] != "":
                    if "mistake" in move["comment"]:
                        move["comment"] = "{}\n//{}".format(move["comment"].split("mistake")[0], "mistake from here")
                    if "#" in move["comment"]:
                        piece = move["comment"].split("#")[0]
                        move["comment"] = move["comment"].split("#")[1]
                        if self.url.rfind("\n") != -1:
                            alg = self.url[self.url.rfind("\n") + 1:]
                            self.url = self.url[:self.url.rfind("\n") + 1] + "//{}\n".format(piece) + alg

                        self.url += "// {} \n".format(move["comment"])
                    else:
                        self.url += "// {} \n".format(move["comment"])

    def gen_url(self):
        """
        generates the solve to cubedb.net url format
        """
        self.url = "https://www.cubedb.net/?rank=3&title={}&time={}&scramble=".format(self.name_of_solve, self.time_solve)
        for move in self.scramble.split():
            if "\'" in move:
                move.replace("\'", "-")
            self.url += "{}_".format(move)
        self.url += "&alg="
        count = 0
        for move in self.solve_stats:
            if self.comms_unparsed_bool:
                if self.comms_unparsed_bool:
                    if move["comment"] != "":
                        if "mistake" in move["comment"]:
                            move["comment"] = "{}%0A//{}".format(move["comment"].split("mistake")[0],
                                                                 "mistake from here")
                        if "#" in move["comment"]:
                            piece = move["comment"].split("#")[0]
                            move["comment"] = move["comment"].split("#")[1]
                            if self.url.rfind("%0A") != -1:
                                alg = self.url[self.url.rfind("%0A") + 3:]
                                self.url = self.url[:self.url.rfind("%0A") + 3] + "%0A//{}%0A".format(piece) + alg
                            else:
                                alg = self.url[self.url.rfind("=") + 1:]
                                self.url = self.url[:self.url.rfind("=") + 1] + "%0A//{}%0A".format(piece) + alg
                        self.url += self.comms_unparsed[count]
                        count += 1
                        self.url += "// {} %0A".format(move["comment"])


            else:
                if "move" in move:
                    if move["move"] != "":
                        if "\'" in move["move"]:
                            move["move"].replace("\'", "-")
                        self.url += "{}_".format(move["move"])
                if move["comment"] != "":
                    if "mistake" in move["comment"]:
                        move["comment"] = "{}%0A//{}".format(move["comment"].split("mistake")[0], "mistake from here")
                    if "#" in move["comment"]:
                        piece = move["comment"].split("#")[0]
                        move["comment"] = move["comment"].split("#")[1]
                        if self.url.rfind("%0A") != -1:
                            alg = self.url[self.url.rfind("%0A") + 3:]
                            self.url = self.url[:self.url.rfind("%0A") + 3] + "//{}%0A".format(piece) + alg
                        else:
                            alg = self.url[self.url.rfind("=") + 1:]
                            self.url = self.url[:self.url.rfind("=") + 1] + "//{}%0A".format(piece) + alg

                        self.url += "// {} %0A".format(move["comment"])
                    else:
                        self.url += "// {} %0A".format(move["comment"])

    def perm_to_string(self, perm):
        """
        converts permutation object to str
        """
        perm_string = ""
        for i in range(1,55):
            perm_string += str(perm(i)) + " "

        return (perm_string)

    def count_solved_cor(self):
        solved_corners = 0
        current_perm_list = self.perm_to_string(self.current_perm).split()
        for cor in self.corners_numbers:
            if current_perm_list[cor - 1] == str(cor):
                solved_corners += 1
        return int(solved_corners/3)

    def count_solve_edges(self):
        solved_edges = 0
        current_perm_list = self.perm_to_string(self.current_perm).split()
        for edge in self.edges_numbers:
            if current_perm_list[edge - 1] == str(edge):
                solved_edges += 1
        return int(solved_edges/2)

    def diff_solved_state(self):
        """
        gets two permutation of cube and return the pieces which got solved between the twp states
        """

        last = self.current_max_perm_list
        current = self.current_perm
        last = self.perm_to_string(last.inverse()).split()
        current = self.perm_to_string(current.inverse()).split()
        last_solved_pieces = {}
        for i in range (0,54):
            if (last[i] != current[i]):
                last_solved_pieces[i+1] = [last[i], current[i]]
        return last_solved_pieces

    def parse_comm_list(self, comm):
        """
        gets a commutator list ([''UF', 'UB', 'LB'])
        returns special cases (flip, twist) or original
        """
        edges = False
        if len(comm[0]) == 2:
            edges = True
        if self.string_permutation(comm[0], comm[1]):
            if edges:
                found = []
                found.append(comm[0])
                for temp in self.last_solved_pieces:
                    if temp in self.edges_numbers:
                        sticker = self.dict_stickers[temp]
                        if not self.string_permutation_list(sticker, found):
                            found.append(sticker)
                found.append(" flip")
                comm_new = found
            else:
                found = []
                found.append(comm[0])
                for temp in self.last_solved_pieces:
                    if temp in self.corners_numbers:
                        sticker = self.dict_stickers[temp]
                        if not self.string_permutation_list(sticker, found):
                            found.append(sticker)
                found.append(" twist")
                comm_new = found
        else:
            comm_new = comm
        return comm_new

    def parse_solved_to_comm(self):
        """
        analyzes last pieces solved, then parse it into commutator.
        return the commutator (as letter_pair - AB or UF -> UB -> UR), and piece type that was solved
        """
        comm = []
        piece_type = {"edge" : False, "corner": False, "parity" : False}
        if self.buffer_ed in self.last_solved_pieces:
            piece_type["edge"] = True
            comm.append(self.buffer_ed)
            current_num = self.last_solved_pieces[self.buffer_ed][0]
            flag = False
            while not flag:
                for i in self.last_solved_pieces:
                    if self.last_solved_pieces[i][1] == current_num:
                        current_num = self.last_solved_pieces[i][0]
                        comm.append(i)
                    if current_num == self.last_solved_pieces[self.buffer_ed][1]:
                        flag = True
                        break

        if self.buffer_cor in self.last_solved_pieces:
            piece_type["corner"] = True
            comm.append(self.buffer_cor)
            current_num = self.last_solved_pieces[self.buffer_cor][0]
            flag = False
            while not flag:
                for i in self.last_solved_pieces:
                    if self.last_solved_pieces[i][1] == current_num:
                        current_num = self.last_solved_pieces[i][0]
                        comm.append(i)
                    if current_num == self.last_solved_pieces[self.buffer_cor][1]:
                        flag = True
                        break

        if self.buffer_cor not in self.last_solved_pieces:

            flag_temp_buffer = False
            for temp in self.last_solved_pieces:
                if temp in self.corners_numbers:
                    piece_type["corner"] = True
                    flag_temp_buffer = True
                    temp_buffer = temp
                    break
            if flag_temp_buffer:
                comm.append(temp_buffer)
                current_num = self.last_solved_pieces[temp_buffer][0]
                flag = False
                while not flag:
                    for i in self.last_solved_pieces:
                        if self.last_solved_pieces[i][1] == current_num:
                            current_num = self.last_solved_pieces[i][0]
                            comm.append(i)
                        if current_num == self.last_solved_pieces[temp_buffer][1]:
                            flag = True
                            break

        if self.buffer_ed not in self.last_solved_pieces:
            flag_temp_buffer = False
            for temp in self.last_solved_pieces:
                if temp in self.edges_numbers:
                    piece_type["edge"] = True
                    flag_temp_buffer = True
                    temp_buffer = temp
                    break
            if flag_temp_buffer:
                comm.append(temp_buffer)
                current_num = self.last_solved_pieces[temp_buffer][0]
                flag = False
                while not flag:
                    for i in self.last_solved_pieces:
                        if self.last_solved_pieces[i][1] == current_num:
                            current_num = self.last_solved_pieces[i][0]
                            comm.append(i)
                        if current_num == self.last_solved_pieces[temp_buffer][1]:
                            flag = True
                            break
        if piece_type["edge"] and piece_type["corner"]:
            piece_type["parity"] = True
            piece_type["edge"] = False
            piece_type["corner"] = False

        for i in range(len(comm)):
            comm[i] = self.dict_stickers[comm[i]]
        comm = self.parse_comm_list(comm)

        for i in range(len(comm)):
            if self.parse_to_lp:
                if (' twist' != comm[i]) and (' flip' != comm[i]):
                    comm[i] = self.dict_lp[comm[i]]
        return (comm, piece_type)

    def exe_move(self, move):
        """
        gets a str that represents a move, executes the move on the permutation variable in the cube class
        """
        self.singlemoveExecute(move)
        facelet_str = self.current_perm.__str__()
        self.current_perm_list = []
        facelet = "0UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

        if facelet_str != "1":
            outer = re.compile(r'\((.*?)\)')
            matches = outer.findall(facelet_str)
            facelet = list(facelet)
            helper = facelet.copy()
            for p in matches:
                c = -1
                p = p.split()
                for i in p:
                    self.current_perm_list.append(i)
                    c += 1
                    temp1 = helper[int(p[c])]
                    facelet[int(p[(c + 1) % len(p)])] = temp1

        self.current_facelet = "{}{}".format("0",''.join(facelet[1:]))


    def fix_rotation(self):
        """
        the software only works for White-Green orientation. so if the first move is not in WG orientation
        it corrects the orientation to apply the move on WG orientation.
        """
        cube_helper = Cube()
        cube_helper.scramble = self.scramble.split()
        cube_helper.solve = self.solve.split()

        rotations = []
        for move in cube_helper.scramble:
            cube_helper.exe_move(move)
        for move in cube_helper.solve:
            if move not in cube_helper.rotation:
                if not self.currently_parsing_smart_cube:
                    break
            cube_helper.exe_move(move)

        str_perm = cube_helper.perm_to_string(cube_helper.current_perm).split()
        up = str_perm[4]
        front = str_perm[22]
        flag = False
        for i in range (4):
            if (up == "5"):
                flag = True
                break
            rotations.append("x")
            cube_helper.exe_move("x")
            str_perm = cube_helper.perm_to_string(cube_helper.current_perm).split()
            up = str_perm[4]
            front = str_perm[22]

        if (front != "23" and not flag):
            rotations.append("z")
            cube_helper.exe_move("z")
            str_perm = cube_helper.perm_to_string(cube_helper.current_perm).split()
            up = str_perm[4]
            front = str_perm[22]

        while (up != "5" or front != "23"):
            rotations.append("y")
            cube_helper.exe_move("y")
            str_perm = cube_helper.perm_to_string(cube_helper.current_perm).split()
            front = str_perm[22]

        final_rot = []
        while len(rotations) >= 3:
            if rotations[0] == rotations[1] == rotations[2]:
                r_fix = "{}'".format(rotations[0]).replace("''","")
                final_rot.append(r_fix)
                rotations.pop(0)
                rotations.pop(0)
                rotations.pop(0)
            else:
                final_rot.append(rotations[0])
                rotations.pop(0)
        if final_rot:
            return final_rot
        return rotations

    def y_rotation(self):
        """
        applies a y rotation to the moves in the alg
        """
        before = ('R','r', 'B', 'b', 'L', 'l','F','f','M' , 'z' ,'S', 'x')
        after =  ('B','b', 'L', 'l', 'F', 'f','R','r','S' , 'x' ,"M'", "z'")
        solve = self.solve_helper.maketrans(dict(zip(before, after)))
        solve_trans = self.solve_helper.translate(solve)
        solve_trans = solve_trans.replace("\'\'","")
        self.solve_helper = solve_trans

    def y2_rotation(self):
        self.y_rotation()
        self.y_rotation()
    def yp_rotation(self):
        self.y2_rotation()
        self.y_rotation()

    def x_rotation(self):
        """
        applies a z rotation to the moves in the alg
        """
        before = ('U', 'u', 'F', 'f', 'D', 'd', 'B', 'b', 'S', 'E', 'y', 'z')
        after  = ('F', 'f', 'D', 'd', 'B', 'b', 'U', 'u', 'E', 'S\'', "z", "y'")
        solve = self.solve_helper.maketrans(dict(zip(before, after)))
        solve_trans = self.solve_helper.translate(solve)
        solve_trans = solve_trans.replace("\'\'", "")
        self.solve_helper = solve_trans

    def x2_rotation(self):
        self.x_rotation()
        self.x_rotation()

    def xp_rotation(self):
        self.x2_rotation()
        self.x_rotation()

    def z_rotation(self):
        """
        applies a z rotation to the moves in the alg
        """
        before = ('R', 'r', 'U', 'u', 'L', 'l', 'D', 'd', 'M', 'E', 'x', 'y')
        after  = ('U', 'u', 'L', 'l', 'D', 'd', 'R', 'r', 'E', 'M\'', "y", "x'")
        solve = self.solve_helper.maketrans(dict(zip(before, after)))
        solve_trans = self.solve_helper.translate(solve)
        solve_trans = solve_trans.replace("\'\'", "")
        self.solve_helper = solve_trans

    def z2_rotation(self):
        self.z_rotation()
        self.z_rotation()

    def zp_rotation(self):
        self.z2_rotation()
        self.z_rotation()

    def apply_rotation(self, rotation):
        funcMoves = {
            "y" : self.y_rotation,
            "y'" : self.yp_rotation,
            "y2" : self.y2_rotation,
            "x": self.x_rotation,
            "x'": self.xp_rotation,
            "x2": self.x2_rotation,
            "z": self.z_rotation,
            "z'": self.zp_rotation,
            "z2": self.z2_rotation
    }
        funcMoves.get(rotation)()

    def find_mistake(self):
        """
        finds the last point in the solve that you executed correctly
        """
        if self.solve_stats[-1]["comment"] == "":
            for stat in reversed(self.solve_stats):
                if stat["comment"] != "":
                    self.solve_stats[stat["count"]]["comment"] += "mistake from here"
                    break

def keep_comms_unparsed(solve):
    """
    if you use a reconstruction that the algs are in the format of [U, R U R'],
    you can choose in .env file to keep in the view the comms unparsed
    """
    description_words = ["corners", "edges", "parity", ""]
    solve_split =  solve.split("\r\n")
    if len(solve_split) == 1:
        solve_split = solve.split("\n")
    comms = []
    for comm in solve_split:
        if comm.find("/") != -1:
                comm = comm[:comm.find("/")]
        if comm not in description_words:
            comms.append(comm)
    return comms

def count_moves_in_alg(alg):
    moves = ["r", "l", "u","d","f","b","m","s","e"]
    alg = alg.lower()
    count = 0
    for m in moves:
        count += alg.count(m)
    return count

def check_if_comm_or_memo(alg):
    moves = ['U', 'R', 'F', 'D', 'L', 'B']
    for m in moves:
        if m in alg:
            return True
    return False

def parse_solve(scramble, solve_attampt):
    """
    main function, parses the solve. most of the data will be in cube.solve stats
    """
    solve, solve_split = solve_parser(solve_attampt)

    SOLVED = "0UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
    cube = Cube()
    cube.comms_unparsed = keep_comms_unparsed(solve_attampt)
    cube.scramble = scramble
    cube.solve = solve
    cube.solve_helper = solve
    cube.current_facelet = SOLVED
    SCRAMBLE_LIST = scramble.split()
    rot = cube.fix_rotation()

    for move in rot:
         cube.exe_move(move)
    for move in SCRAMBLE_LIST:
        cube.exe_move(move)
    count = 0
    cube.solve_stats.append({"count": count, "move": "", "ed": cube.count_solve_edges(), "cor": cube.count_solved_cor(), "comment": ""})
    cube.current_max_perm_list = (cube.current_perm)
    move_in_solve = cube.solve.split()
    max_piece_place = 0
    flag = False
    flag_rot = False
    current_alg = []
    if len(solve_split) > 1:
        flag_rot = True
        first_alg = str(alg_maker(solve_split[0]))
    count_solve_split = 0
    while move_in_solve[count] in cube.rotation:
        if flag_rot:
             if count >= len(first_alg.split()): # for cases that the first alg also starts with rotation
                 break
        flag = True
        original_move = move_in_solve[count]
        current_alg.append(original_move)
        exe_move = cube.solve_helper.split()[count]
        count += 1
        cube.exe_move(exe_move)
        solved_edges = cube.count_solve_edges()
        solved_cor = cube.count_solved_cor()
        diff = cube.diff_states(cube.perm_to_string(cube.current_perm))
        cube.solve_stats.append(
            {"count": count, "move": original_move, "ed": solved_edges, "cor": solved_cor, "comment": "",
             "diff": diff, "perm": cube.perm_to_string(cube.current_perm)})
        cube.current_max_perm_list = (cube.current_perm)
    if flag:
        cube.algs_executed.append(" ".join(current_alg))
        cube.solve_stats[count]["comment"] = "memo"
    current_alg = []
    start = count
    count_moves_from_start = 0
    for i in range (start, len(move_in_solve)):
        original_move = move_in_solve[i]
        current_alg.append(original_move)
        exe_move = cube.solve_helper.split()[i]
        count += 1
        cube.exe_move(exe_move)
        solved_edges =  cube.count_solve_edges()
        solved_cor = cube.count_solved_cor()
        diff = cube.diff_states(cube.perm_to_string(cube.current_perm))
        if diff > cube.diff_to_solved_state and (count - max_piece_place >= 4):
            temp_count = count - max_piece_place
            max_piece_place = count
            cube.last_solved_pieces = cube.diff_solved_state()
            comm, piece_type = cube.parse_solved_to_comm()
            if len(comm) > 3 and temp_count < 8:
                 cube.solve_stats.append(
                     {"count": count, "move": original_move, "ed": solved_edges, "cor": solved_cor, "comment": "",
                      "diff": diff, "perm": cube.perm_to_string(cube.current_perm)})
            else:
                cube.algs_executed.append([" ".join(current_alg), piece_type])
                count_moves = count_moves_in_alg(" ".join(current_alg))
                count_moves_from_start += count_moves
                current_alg = []
                if piece_type["edge"]:
                    piece = "edges"
                elif piece_type["corner"]:
                    piece = "corners"
                else:
                    piece = "parity"
                cube.current_max_perm_list = cube.current_perm
                if cube.parse_to_lp:
                    buffer_lp_edge = cube.dict_lp[cube.dict_stickers[cube.buffer_ed]]
                    buffer_lp_cor = cube.dict_lp[cube.dict_stickers[cube.buffer_cor]]
                    if piece_type["edge"]:
                        if buffer_lp_edge in comm and " flip" not in comm:
                            comment = "".join(comm[1:])
                        else:
                            comment = "".join(comm)
                    elif piece_type["corner"]:
                        if buffer_lp_cor in comm and " twist" not in comm:
                            comment = "".join(comm[1:])
                        else:
                            comment = "".join(comm)
                    else:
                        comment = "{} {}".format("".join(comm[:2]), "".join(comm[2:]) )

                    comment = "{}   {}/{}".format(comment, count_moves,count_moves_from_start) if cube.gen_with_moves else comment

                else:
                    comment = "{}  {}/{}".format(" ".join(comm[:]), count_moves,count_moves_from_start) if cube.gen_with_moves else "{}".format(" ".join(comm[:]))

                if piece != cube.flag_piece_type:
                    comment = "{}#{}".format(piece, comment)
                    cube.flag_piece_type = piece
                cube.solve_stats.append({"count" : count,"move": original_move,"piece" : piece, "diff_moves": count_moves, "ed" : solved_edges,"cor" :  solved_cor, "comment" : comment,  "diff" : diff, "perm" : cube.perm_to_string(cube.current_perm)})
        else:
            cube.solve_stats.append({"count" : count,"move": original_move,"ed" : solved_edges,"cor" :  solved_cor, "comment" : "" , "diff" : diff, "perm" : cube.perm_to_string(cube.current_perm)})

    if current_alg:
        cube.algs_executed.append([" ".join(current_alg), piece_type])

    cube.find_mistake()
    # print(*cube.solve_stats, sep="\n")
    if cube.gen_parsed_to_cubedb:
        cube.gen_url()
    else:
        cube.gen_solve_to_text()
    return cube

def parse_smart_cube_solve(cube):
    """
    parse solve if solve string was generated by smart cube
    """
    cube.smart_cube = False
    SCRAMBLE = cube.scramble
    SOLVE = ""

    for comm in cube.algs_executed:
        if comm[1]["edge"] or comm[1]["parity"]:
            smart_cube_alg_parsed = cube.parse_alg_to_slice_moves(comm[0])
            SOLVE += " " + smart_cube_alg_parsed
        else:
            SOLVE += " " + comm[0]
    return parse_solve(SCRAMBLE, SOLVE)

def parse_url(url):
    """
    gets a url from alg.cubing.net or cubedb.net and returns a dictionary of the elements of the url parsed (scramble, solve, title, time)
    """
    split_url = url.split("&")
    url_elem = {}
    for p in split_url:
        if "http" in p:
            website_split = p.split("?")
            url_elem["name"] = website_split[0]
            split_second_part = website_split[1].split("=")
            url_elem[split_second_part[0]] = split_second_part[1]
        elif "setup" in p or "scramble" in p:
            url_elem["scramble"] =p.split("=")[1].replace("-", "'").replace("_", " ")
        else:
            url_elem[p.split("=")[0]] = p.split("=")[1]
    before = ('-', '_', '%0A', '%5B', '%5D', '%2F', '%2C','%3A')
    after =  ("'", " ", "\r\n", "[", "]", "/", ",", ":")
    for i in range (len(before)):
        url_elem["alg"] = url_elem["alg"].replace(before[i], after[i])
    return url_elem

def main():
    pass
if __name__ == '__main__':
    main()
#TODO: x y // memo --> comm that starts with rotation
# done twisted and flips --> even with 3twist and 4 flips
# done sticker to letter pair option
# done option to show unparsed algs
# done parity not with buffer
# done translate from smart cube to solve
# done option to paste to text
# done count to moves
# done (M U M' U')2 like algs to parser
# done fix UD algs
# done diff moves misses by one from secnd alg
# done corners/edges seperation
# done parsing solves from alg.cubing.net and cubedb.net

# feature:
# supports all oreintations' all buffers' 2twist,3twist, 2flip 4 flip