import copy
import shutil
import os

def change(name, dna, cwd):
    code = []
    compare = ["<", ">", "<=", ">=", "!=", "=="]
    and_or = ["and", "or"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    with open(os.path.join(cwd, f"artfeel_{name}.txt"), "r", encoding="utf-8") as a:
        counter = 0
        a = a.read()
        word = ""
        code = []
        spaces = ["", " ", "\n", "(", ",", ")"]
        for line in a:
            l = str(line)
            if len(word) > 0:
                if word[-1] in spaces:
                    if l not in spaces:
                        code.append(word)
                        word = ""
                if len(word) > 0 and word[-1] not in spaces:
                    if l in spaces:
                        code.append(word)
                        word = ""
            word += l
        n = 0
        for ls in code:
            if len(code) > 1 and ls == "1234567890":
                gene = dna[counter % len(dna)]
                k = n + 1
                while code[k][-1] != ":" and len(code) - 1 > k:
                    if code[k] in compare:
                        code[k] = compare[int((counter + gene) % len(compare))]
                    if code[k] in and_or:
                        code[k] = and_or[int((counter + gene) % len(and_or))]
                    ls2 = copy.deepcopy(code[k])
                    isnum = False
                    for u in range(len(numbers)):
                        ls2 = "".join(ls2)
                        ls5 = ls2.split()
                        ls2 = ls2.split(numbers[u])
                        if len(ls2) > len(ls5):
                            isnum = True
                            break
                    if isnum == True:
                        number = ""
                        j = 0
                        j1 = -1
                        for t in range(len(code[k])):
                            if code[k][t] in numbers:
                                j1 = t - 1
                                j = t
                                break
                        while  j < len(code[k]) and k < len(code) and code[k][j] in numbers:
                            number += code[k][j]
                            j += 1
                        if j < len(code[k]) - 1:
                            s2 = code[k][j + 1:]
                        else:
                            s2 = ""
                        if j1 >= 0:
                            s1 = code[k][0:j1]
                        else:
                            s1 = ""
                        if number != "":
                            number = int(number)
                            number += int(numbers[int((counter + gene) % len(numbers))])
                            number = str(number)
                            number = s1 + number + s2
                            code[k] = number
                    k += 1
                counter += 1
            n += 1
        a = "".join(code)
    with open(os.path.join(cwd, f"artfeel_{name}.txt"), "w", encoding="utf-8") as a2:
        a2.write(a)
    shutil.copy(os.path.join(cwd, f"artfeel_{name}.txt"), os.path.join(cwd, f"artfeel_{name}.py"))
def change_revolution(name, cwd):
    with open(os.path.join(cwd, f"revolution.txt"), "r", encoding="utf-8") as a:
        a = a.read()
        word = ""
        code = []
        spaces = ["", " ", "\n", "(", ",", ")"]
        for line in a:
            l = str(line)
            if len(word) > 0:
                if word[-1] in spaces:
                    if l not in spaces:
                        code.append(word)
                        word = ""
                if len(word) > 0 and word[-1] not in spaces:
                    if l in spaces:
                        code.append(word)
                        word = ""
            word += l
        if len(word) > 0 and len(code) > 0 and word != code[-1]:
            code.append(word)
        if len(code) == 0:
            shutil.copy(os.path.join(cwd, f"save_revolution.txt"), os.path.join(cwd, f"revolution.txt"))
            code = change_revolution(name)
        for ls in range(len(code)):
            if len(code[ls]) >= 7:
                if code[ls][0] == "a" and code[ls][1] == "r" and code[ls][2] == "t" and code[ls][3] == "f" and code[ls][4] == "e" and code[ls][5] == "e" and code[ls][6] == "l":
                    code[ls] = f"artfeel_{name}"
        a = "".join(code)
    with open(os.path.join(cwd, f"revolution.txt"), "w", encoding="utf-8") as a2:
        a2.write(a)
    shutil.copy(os.path.join(cwd, f"revolution.txt"), os.path.join(cwd, f"revolution.py"))
    return code
