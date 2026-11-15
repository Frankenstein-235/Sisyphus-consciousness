import random
import numpy as np
import json
import copy
import words
import revolution as r
import os
import pymorphy3
import shutil
import psutil
import pickle
import artfeel_change
import threading

class DNA():
    def __init__(self, name, dna, cwd=os.getcwd()) -> None:
        self.dna = dna
        self.name = name
        self.cwd = cwd
        shutil.copy(f"revolution.py", f"{self.cwd}\\revolution.txt")
        shutil.copy(f"artfeel.py", f"{self.cwd}\\artfeel_{name}.py")
        shutil.copy(f"{self.cwd}\\artfeel_{name}.py", f"{self.cwd}\\artfeel_{name}.txt")
        artfeel_change.change(name, dna)
        self.t_d = {}
    def cpu_temp(self) -> np.float64 | float | int:
        p = psutil.cpu_percent()
        if p != 0:
            cpu = np.log10((np.e**p))*3
        else:
            cpu = 45
        return cpu
    def func_temp(self, name):
        try:
            with open(f"{self.cwd}\\ft_{self.name}.json", "r", encoding="utf-8") as f:
                ft = json.load(f)
            if name in list(ft.keys()):
                v = ft[name]
                ft.pop(name)
                ft.update({name: (v + self.cpu_temp())/2})
            else:
                ft.update({name: self.cpu_temp()})
        except:
            ft = {}
            ft.update({name: self.cpu_temp()})
        v = np.array(list(ft.values()))
        v = np.sum(v)/len(v) + random.randint(-10, 10)*self.dna[5]
        with open(f"{self.cwd}\\ft_{self.name}.json", "w", encoding="utf-8") as f:
            json.dump(ft, f, ensure_ascii=False, indent=4)
        return v
    def count_e(self, years, yearend):
        temp = self.func_temp("count_e")
        artfeel_change.change_revolution(self.name)
        import revolution as r
        years = r.game(self.w, self.co_so, 100, False, yearend, years, temp)
        self.save_load(self.name, years=years, save_True_load_False=True)
        love = 0
        hate = 0
        fear = 0
        joy = 0
        tired = 0
        sad = 0
        for key, value in self.co_so.items():
            for key2, value2, in value.everyone.items():
                love += value2.love
                hate += value2.hate
                fear += value2.fear
                joy += value2.joy
                tired += value2.tired
                sad += value2.sad
            love /= len(value.everyone)
            hate /= len(value.everyone)
            fear /= len(value.everyone)
            joy /= len(value.everyone)
            tired /= len(value.everyone)
            sad /= len(value.everyone)
        fn = [love, hate, fear, joy, tired, sad]
        return fn, love, hate, fear, joy, tired, sad, years
    def feelings(self, memory: list | np.ndarray | np.ndarray[np.ndarray[np.float64]] | np.ndarray[np.ndarray[np.int64]], 
                 wordlist1: list | list[str], yearend: int, years: int):
        fn, love, hate, fear, joy, tired, sad, years = self.count_e(years, yearend)
        vectors = [np.zeros(6), np.zeros(6), np.zeros(6), 
                   np.zeros(6), np.zeros(6), np.zeros(6)]
        lens = []
        for d in range(len(words.fn)):
            lens.append(len(words.fn[d]))
        if len(memory) < len(wordlist1):
            memory = list(memory)
            memory += self.arrays(len(memory), len(wordlist1) - len(memory), years)
            memory = np.array(memory)
        if len(memory) > len(wordlist1):
            n = len(memory) - (len(memory) - len(wordlist1))
            memory = memory[0:n]
        for i in range(min(lens)):
            for j in range(len(words.fn)):
                wordlist = words.fn[j]
                for k in range(len(wordlist)):
                    counter = 0
                    wasword = []
                    for u in range(len(wordlist1)):
                        if wordlist1[u].split(",")[0] == wordlist[k] and wordlist[k] not in wasword:
                            vectors[j] += memory[u]
                            counter += 1
                            wasword.append(wordlist[k])
                    if counter != 0:
                        vectors[j] /= counter
            self.func_temp("feelings")
        f_d = {"love": love, "hate": hate, "fear": fear, "joy": joy, "tired": tired, "sad": sad}
        return fn, vectors, f_d, years
    def save_load(self, name, memory=False, errors=False, gradient=False, wordlist1=False, quest=False, years=False, save_True_load_False=False):
        if save_True_load_False == True:
            if type(memory) == list or type(gradient) == np.ndarray:
                with open(f"m_{name}.json", "w", encoding="utf-8") as f:
                    json.dump(memory, f, ensure_ascii=False, indent=4)
            if type(errors) == list:
                with open(f"e_{name}.json", "w", encoding="utf-8") as f:
                    json.dump(errors, f, ensure_ascii=False, indent=4)
            if type(gradient) == list or type(gradient) == np.ndarray:
                with open(f"g_{name}.json", "w", encoding="utf-8") as f:
                    json.dump(gradient, f, ensure_ascii=False, indent=4)
            if type(wordlist1) == list:
                with open(f"w_{name}.json", "w", encoding="utf-8") as f:
                    json.dump(wordlist1, f, ensure_ascii=False, indent=4)
            if type(quest) == list or type(quest) == dict:
                with open(f"quest_{name}.json", "w", encoding="utf-8") as f:
                    json.dump(quest, f, ensure_ascii=False, indent=4)
            if type(years) == int:
                with open(f"y_{name}.json", "w") as f:
                    json.dump(years, f)
        else:
            lists = []
            if memory == True:
                with open(f"{self.cwd}\\m_{name}.json", "r", encoding="utf-8") as f:
                    memory = np.array(json.load(f))
                    lists.append(memory)
            if errors == True:
                with open(f"{self.cwd}\\e_{name}.json", "r", encoding="utf-8") as f:
                    errors = json.load(f)
                    lists.append(errors)
            if gradient == True:
                with open(f"{self.cwd}\\g_{name}.json", "r", encoding="utf-8") as f:
                    gradient = np.array(json.load(f))
                    lists.append(gradient)
            if wordlist1 == True:
                with open(f"{self.cwd}\\w_{name}.json", "r", encoding="utf-8") as f:
                    wordlist1 = json.load(f)
                    lists.append(wordlist1)
            if quest == True:
                with open(f"{self.cwd}\\quest_{name}.json", "r", encoding="utf-8") as f:
                    quest = json.load(f)
                    lists.append(quest)
            if years == True:
                with open(f"{self.cwd}\\y_{name}.json", "r") as f:
                    years = json.load(f)
                    lists.append(years)
            return tuple(lists)
    def arrays(self, first_index, how_many, years):
        vectors_list = []
        try:
            m, wordlist1, years = self.save_load(self.name, True, False, False, True, False, True, False)
        except:
            m = []
            wordlist1 = []
            years = 0
        fn = self.count_e(years, abs(psutil.cpu_percent()) + 1)[0]
        if random.choice(self.dna) >= max(self.dna)//2:
            for i in range(first_index, how_many + first_index):
                if i % random.randint(1, 400) == 0:
                    fn = self.count_e(years, abs(psutil.cpu_percent()) + 1)[0]
                array = []
                for j in range(6):
                    array.append(fn[j]*self.dna[j]*(i*j))
                vectors_list.append(array)
        else:
            for i in range(how_many):
                array = []
                if i % random.randint(1, 400) == 0:
                    fn = self.count_e(years, abs(psutil.cpu_percent()) + 1)[0]
                for j in range(6):
                    array.append(fn[j]*self.dna[j]*(i*j))
                vectors_list.append(array)
        if len(m) == len(wordlist1):
            fn, fvectors, f_d, years = self.feelings(m, wordlist1, 100, years)
            for i in range(len(vectors_list)):
                for j in range(len(vectors_list[i])):
                    vectors_list[i][j] += np.sum(fn)/len(fn)
        return vectors_list
class LM(DNA):
    def __init__(self, name: str, books: list[str], dna: list[float] | list[int]) -> None:
        super().__init__(name, dna)
        self.name = name
        self.books = books
        self.dna = dna
        self.thoughts = []
        artfeel_change.change_revolution(self.name)
        import revolution as r
        self.co_so, self.w = r.start(["A", "B", "C"], ["Anarchism", "Communism", "Monarchism"])
    def read(self, symbols: list[str]) -> list[str]:
        wordlist = []
        for i in self.books:
            with open(f"{self.cwd}\\{i}.txt", "r", encoding="utf-8") as f:
                for line in f:
                    l = str(line.strip())
                    for j in range(len(symbols)):
                        if type(l) != str:
                            l = "".join(l)
                        l = l.split(symbols[j])
                    if "".join(l) != "" and len("".join(l).split()) > 0:
                        wordlist += l
        return wordlist
    def questions(self, books: list[str]) -> dict:
        startbooks = copy.deepcopy(self.books)
        self.books = books
        wordlist = self.read([";", "(", ")", "«", "»", "„", "“", "q", "w", "e", "r", "t", 
                              "y", "u", "i", "o", "p", "a", "s", "—",
                              "d", "f", "g", "h", "j"," k", "l", "z", "x", "c", "v", "b", "n", "m",
                              "C", "D", "B", "E", "?"])
        self.books = startbooks
        q_a = {}
        s = [".", "!"]
        morph = pymorphy3.MorphAnalyzer()
        for i in range(len(wordlist)):
            question = [""]
            answer = [""]
            for j in range(1, len(wordlist[i]) + 1):
                question.append(wordlist[i][-j])
                if -j > -len(wordlist[i]):
                    if wordlist[i][-j] in s:
                        break
            if i < len(wordlist) - 1:
                if wordlist[i + 1] != "" and len(wordlist[i + 1].split(",")[0].split()) >= 1 and len(wordlist[i + 1].split()) >= 2 and wordlist[i + 1].split()[0] not in ["-", "—"] and wordlist[i + 1].split()[1] not in ["-", "—"] and morph.parse(wordlist[i + 1].split(",")[0].split()[0])[0].tag.POS != "VERB":
                    for k in range(len(wordlist[i + 1])):
                        answer.append(wordlist[i + 1][k])
                        if k < len(wordlist[i + 1]):
                            if wordlist[i + 1][k] in s:
                                break
            question.reverse()
            question = "".join(question)
            answer = "".join(answer)
            if question != ")" and answer != ")" and len(answer) > 1 and len(question) > 1:
                q_a.update({question: answer})
        return q_a
    def change(self, gradient: list | np.ndarray | np.ndarray[np.ndarray[np.float64]] | np.ndarray[np.ndarray[np.int64]], 
               memory: list | np.ndarray | np.ndarray[np.ndarray[np.float64]] | np.ndarray[np.ndarray[np.int64]], 
               indexes: list[int], lr: float | int | np.float64) -> np.ndarray[np.ndarray[np.float64]]:
        for i in indexes:
            memory[i] -= lr*gradient[indexes.index(i)]
        return memory
    def check_lists(self, memory, wordlist1, gradient, years, scale="None"):
        if len(memory) < len(wordlist1):
            memory = list(memory)
            memory += self.arrays(len(memory) - 1, len(wordlist1) - len(memory), years)
            memory = np.array(memory)
        if len(gradient) < len(wordlist1):
            if len(gradient) > 0:
                av = np.sum(gradient)/len(gradient)
            else:
                av = 1
            gradient = list(gradient)
            for u in range(len(gradient) - 1, len(wordlist1) - len(gradient)):
                gradient.append(av)
            gradient = np.array(gradient)
        if len(memory) > len(wordlist1):
            n = len(memory) - (len(memory) - len(wordlist1))
            memory = memory[0:n]
        if len(gradient) < len(memory):
            n = len(memory) - (len(memory) - len(gradient))
            gradient = gradient[0:n]
            memory = memory[0:n]
            wordlist1 = wordlist1[0:n]
        if scale != "None":
            if len(gradient) > len(wordlist1):
                n = len(gradient) - (len(gradient) - len(wordlist1))
                gradient = gradient[0:n]
            if len(gradient) >= scale + 1:
                index = random.randint(0, len(gradient) - scale)
                gradient = gradient[index:index + scale]
            if len(memory) >= scale + 1:
                index = random.randint(0, len(memory) - scale)
                memory = memory[index:index + scale]
            if len(wordlist1) >= scale + 1:
                index = random.randint(0, len(wordlist1) - scale)
                wordlist1 = wordlist1[index:index + scale]
        return memory, wordlist1, gradient
    def average_vector(self, word, memory, wordlist1, gradient, years, check=True):
        average = np.zeros(len(memory[0]))
        counter = 0
        if check == True:
            memory, wordlist1, gradient = self.check_lists(memory, wordlist1, gradient, years)
        for i in range(len(wordlist1)):
            if word == wordlist1[i]:
                average += memory[i]
                counter += 1
        return average
    def softmax(self, plist):
        indexes = []
        p = 0
        for i in range(len(plist)):
            if np.exp(np.e**plist[i]) not in [float("nan"), float("inf"), 0.0]:
                indexes.append(i)
                p += np.e**plist[i]
        for j in indexes:
            plist[j] = float(np.e**plist[j]/p)
        return indexes, plist
    def write(self,  wordlist1: list | list[str], learning_rate: float | int | np.float64=1e-5, start: str=None, t_end: int=random.randint(1, 10), 
              memory: list | np.ndarray | np.ndarray[np.ndarray[np.float64]] | np.ndarray[np.ndarray[np.int64]]=[], 
              errors: list[int] | list[float]=[], endtlist: list | list[str]=[], 
              gradient: list | np.ndarray | np.ndarray[np.ndarray[np.float64]] | np.ndarray[np.ndarray[np.int64]]=[], years: int=0,
              scale="None", learn=True):
        memory, wordlist1, gradient = self.check_lists(memory, wordlist1, gradient, years, scale=scale)
        t = []
        if start != None:
            startm = copy.deepcopy(memory)
            s = start.split()
            if len(start.split()) != 0:
                t += s
            else:
                t += [" "]
            if len(endtlist) > 0:
                for i in range(len(endtlist)):
                    if t[0] == endtlist[i][0] or t[0] == "" or t[0] == " ":
                        w = copy.deepcopy(wordlist1)
                        wlist = list(np.unique(w))
                        random.shuffle(wlist)
                        while t[0] == endtlist[i][0] or t[0] == "" or t[0] == " ":
                            t = random.sample(wlist, 1)
        else:
            startm = copy.deepcopy(memory)
            w = copy.deepcopy(wordlist1)
            wlist = list(np.unique(w))
            random.shuffle(wlist)
            t = random.sample(wlist, 1)
            if len(endtlist) > 0:
                for i in range(len(endtlist)):
                    if t[0] == endtlist[i][0] or t[0] == "" or t[0] == " ":
                        while t[0] == endtlist[i][0] or t[0] == "" or t[0] == " ":
                            t = random.sample(wlist, 1)
        stopwords = ["как", "я", "ты", "это", "этот", "эта", "эти", 
                    "и", "а", "у", "вы", "не", "тот", "та", "так",
                    "к", "в", "но", "по", "их", "нам", "бы", "о",
                    "для", "этих", "этого", "эту", "этой", "этому",
                    "этим", "им", "чем", "кем", "или", "какой",
                    "какая", "какие", "за", "мне", "ее", "нее",
                    "лишь", "скорее", "будто", "который", "которая",
                    "которые", "ко", "до", "для", "во", "них",
                    "нём", "ней", "от"]
        tlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        k = len(t)
        if start != None:
            k -= len(start.split())
        fn, fvectors, f_d, years = self.feelings(memory, wordlist1, 100, years)
        while k < t_end and tlist[-6] != tlist[-1]:
            plist = []
            wordlist = []
            tlist.append(t)
            startm = copy.deepcopy(memory)
            plist = []
            wordlist = []
            n = len(t)
            average = np.zeros(len(memory[0]))
            w2 = copy.deepcopy(wordlist1)
            for i in range(n):
                c = w2.count(t[-n])
                for j in range(c):
                    average += self.average_vector(t[-n], memory, wordlist1, gradient, years)/(n*c)
                    w2.remove(t[-n])
            plist = []
            true_p = []
            if t[-1] not in wordlist1:
                wordlist1.append(t[-1])
            c = wordlist1.count(t[-1])
            wl2 = copy.deepcopy(wordlist1)
            for i in range(c):
                l = wl2.index(t[-1])
                if l < len(wordlist1) - 1:
                    word_p = wordlist1[l + 1]
                else:
                    word_p = random.choice(wordlist1)
                wordlist.append(word_p)
                wl2.remove(t[-1])
            indexes = []
            f_average = np.zeros(6)
            for j in range(len(fvectors)):
                f_average += fvectors[j]
            f_average /= len(fvectors)
            for i in range(len(memory)):
                if np.exp(1/(abs(np.sum(memory[i] - average)) * abs(np.sum(f_average - average)) + 1)) not in [0.0, float("inf"), float("nan")]:
                    prob = 1/(abs(np.sum(memory[i] - average)) * abs(np.sum(f_average - average)) + 1)
                else:
                    prob = 1e-10
                if np.exp(prob) not in [0.0, float("inf"), float("nan")]:
                    if wordlist1[i] in stopwords:
                        if prob > 0:
                            plist.append(prob/random.randint(100, 200))
                        else:
                            plist.append(-100)
                    else:
                        if prob > 0:
                            plist.append(prob)
                        else:
                            plist.append(-100)
                    true_p.append(wordlist.count(wordlist1[i])/len(wordlist))
                    indexes.append(i)
            wordlist2 = []
            indexes, plist = self.softmax(plist)
            word_p = max(plist)
            for i in range(len(plist)):
                if plist[i] == word_p and i in indexes:
                    if (len(t) < 2 and wordlist1[i] != t[-1]) or (len(t) >= 2 and wordlist1[i] != t[-1] and wordlist1[i] != t[-2]):
                        wordlist2.append(wordlist1[i])
            if len(wordlist2) > 0:
                t.append(random.choice(wordlist2))
            plist = np.array(plist)
            true_p = np.array(true_p)
            if learn == True:
                av_prob = 0
                counter = 0
                p = max(true_p)
                plist = plist.tolist()
                true_p = true_p.tolist()
                for i in range(len(plist)):
                    if true_p[i] == p:
                        av_prob += plist[i]
                        counter += 1
                av_prob /= counter
                loss = -np.log(plist[list(true_p).index(max(list(true_p)))])
                errors.append(loss)
                plist = np.array(plist)
                true_p = np.array(true_p)
                gradient = true_p - plist
                memory = self.change(-1*gradient, memory, indexes, learning_rate)
            k = len(t)
            if start != None:
                k -= len(start.split())
            self.func_temp("write")
        t2 = copy.deepcopy(t)
        if start != None:
            t2 = t2[len(start.split()):]
        endt = []
        for i in range(len(t2)):
            endt.append(t2[i])
            endt.append(" ")
        endtlist.append(endt)
        endt = "".join(endt)
        if learn == True:
            self.save_load(self.name, memory.tolist(), errors, gradient.tolist(), wordlist1, False, years, True)
        return t2, endt, memory, endtlist, errors, gradient, startm, years
    def answer(self, start: str, question: dict, wordlist1: list | list[str], learning_rate: float | int, 
               memory: list | np.ndarray | np.ndarray[np.ndarray[np.float64]] | np.ndarray[np.ndarray[np.int64]], 
               errors: list[int] | list[float], 
               gradient: list | np.ndarray | np.ndarray[np.ndarray[np.float64]] | np.ndarray[np.ndarray[np.int64]], 
               answers: list | list[str], years: int, learn=True):
        an = []     
        f_dict = {}
        anspace = []  
        stopwords = ["как", "я", "ты", "это", "этот", "эта", "эти", 
            "и", "а", "у", "вы", "не", "тот", "та", "так",
            "к", "в", "но", "по", "их", "нам", "бы", "о",
            "для", "этих", "этого", "эту", "этой", "этому",
            "этим", "им", "чем", "кем", "или", "какой",
            "какая", "какие", "за", "мне", "ее", "нее",
            "лишь", "скорее", "будто", "который", "которая",
            "которые", "ко", "до", "для", "во", "них",
            "нём", "ней", "от"]
        random.seed(random.randint(1, 100000))
        v = list(question.values())
        key = list(question.keys())
        for k in key:
            for j in range(len(k.split())):
                stopw = []
                w = []
                if k.split()[j] in stopwords:
                    stopw.append(k.split()[j])
                else:
                    w.append(k.split()[j])
            if len(w) / 1.5 <= len(stopw):
                question.pop(k)
                v.remove(v[key.index(k)])
                key.remove(k)
        average_l = 0
        for i in range(len(v)):
            average_l += len(v[i].split())
        average_l = int(average_l / len(v))
        add = []
        wordlist1 = []
        length = 0
        for j in range(len(key)):
            length += len(key[j].split()) + len(v[j].split())
        for i in range(len(key)):
            if key[i] not in add:
                wordlist1 += key[i].split()
                add.append(key[i])
            if v[i] not in add:
                wordlist1 += v[i].split()
                add.append(v[i])
        endt = []
        if start == None:
            quest = random.choice(list(question.keys()))
            ans = question[quest].split()
            an, endt, memory, endtlist, errors, gradient, startm, years = self.write(wordlist1, learning_rate, quest, len(ans) + 1, memory, errors, [], gradient, years, learn=learn)
            quest = quest.split()
            for i in range(len(an)):
                anspace.append(an[i])
                anspace.append(" ")
        else:
            artfeel_change.change_revolution(self.name)
            import revolution as r
            temp = self.func_temp("answer")
            years = r.game(self.w, self.co_so, 100, False, 100, years, temp)
            fn, fvector, f_dict, years = self.feelings(memory, wordlist1, 100, years)
            quest = start
            quest = quest.split("?")
            quest = "".join(quest)
            quest = quest.split()
            average = np.zeros((len(wordlist1), 6))
            a_list = []
            for j in range(len(quest)):
                if quest[j] not in wordlist1:
                    wordlist1.append(quest[j])
                    memory = list(memory)
                    memory += self.arrays(len(memory), len(wordlist1) - len(memory), years)
                    memory = np.array(memory)
            memory, wordlist1, gradient = self.check_lists(memory, wordlist1, gradient, years)
            for k in range(len(quest)):
                average += self.average_vector(quest[k], memory, wordlist1, gradient, years)
            average /= len(quest)
            how = np.zeros(6)
            for i in range(len(quest)):
                if quest[i] in wordlist1 and quest[i]:
                    how += memory[wordlist1.index(quest[i])]
            how /= len(quest)
            how2 = []
            for i in range(len(fvector)):
                how2.append(abs(np.sum(how - fvector[i])))
            co_so2 = copy.deepcopy(self.co_so)
            for key1, value1 in self.co_so.items():
                v1 = copy.deepcopy(value1)
                for key2, value2 in value1.everyone.items():
                    if random.randint(1, 10) != 10:
                        if how2.index(min(how2)) == 0:
                            value2.love += random.randint(1, 10)
                        if how2.index(min(how2)) == 1:
                            value2.hate += random.randint(1, 10)
                        if how2.index(min(how2)) == 2:
                            value2.fear += random.randint(1, 10)
                        if how2.index(min(how2)) == 3:
                            value2.joy += random.randint(1, 10)
                        if how2.index(min(how2)) == 4:
                            value2.tired += random.randint(1, 10)
                        if how2.index(min(how2)) == 5:
                            value2.sad += random.randint(1, 10)
                    else:
                        rand = [value2.love, value2.hate, value2.fear, value2.joy, value2.tired, value2.sad]
                        f = random.choice(rand)
                        f += random.randint(1, 10)
                    v1.everyone.pop(key2)
                    v1.everyone.update({key2: value2})
                co_so2.pop(key1)
                co_so2.update({key1: v1})
            self.co_so = co_so2
            for j in v:
                if j not in answers:
                    d = []
                    f_d = []
                    f_diff = np.zeros(6)
                    k = key[v.index(j)].split()
                    vector = np.zeros(6)
                    for h in range(len(k)):
                        if k[h] in wordlist1:
                            d.append([])
                            array = self.average_vector(k[h], memory, wordlist1, gradient, years)
                            vector += array
                            for i in range(len(fvector)):
                                d[-1].append(abs(np.sum(array - fvector[i])))
                    for i in range(len(d)):
                        f_d.append(d[i].index(min(d[i])))
                    feeling = ["love", "hate", "fear", "joy", "tired", "sad"]
                    f_c = {"love": 0, "hate": 0, "fear": 0, "joy": 0, "tired": 0, "sad": 0}
                    f_w = []
                    for i in range(len(f_d)):
                        f_w.append(feeling[f_d[i]])
                    for i in range(len(f_w)):
                        f_c[f_w[i]] += 1
                    how = []
                    vector /= len(k)
                    for i in range(len(d)):
                        for j in range(len(d[i])):
                            f_diff += d[i][j]
                    f_diff /= len(d)*len(d[0])
                    f_av = np.zeros(6)
                    for i in range(len(fvector)):
                        f_av += fvector[i]
                    f_av /= len(fvector)
                    a_list.append(abs(np.sum(average - vector)) * abs(np.sum(f_diff - f_av)))
            an = v[a_list.index(min(a_list))]
            answers.append(an)
        self.func_temp("answer")
        fn, fvector, f_dict, years = self.feelings(memory, wordlist1, 100, years)
        return an, endt, memory, errors, gradient, answers, years, f_dict
class Subjective(LM):
    def __init__(self, name, person):
        super().__init__(name, random.choice(person.books), 6, person.dna)
        self.books2 = person.books
        self.name = name
        self.person = person
        self.dna = self.person.dna
        func = [self.think, self.feelings_2, self.reset]
        arr = self.arrays(0, len(func), 0)
        self.f_dict = {}
        for k in range(len(arr)):
            arr_str = ""
            for i in range(len(arr[k])):
                arr_str += str(arr[k][i])
                arr_str += " "
            self.f_dict.update({arr_str: func[k]})
        self.feeling = np.zeros(6)
        self.k = list(self.person.pers.keys())
        for i in range(len(self.k)):
            name = self.k[i]
            memory, gradient, wordlist1, years = self.save_load(name, True, False, True, True, False, True, False)
            memory, wordlist1, gradient = self.check_lists(memory, wordlist1, gradient, years)
            gradient2 = []
            for t in range(len(gradient)):
                gradient[t] = np.float64(gradient[t])
                num = gradient[t]
                gradient2.append(self.dna * num)
            gradient = copy.deepcopy(gradient2)
            for j in range(len(memory)):
                memory[j] = np.array(memory[j])
                memory[j] *= self.dna
            memory = np.array(memory)
            gradient = np.array(gradient)
            self.feeling += self.feelings(memory, wordlist1, 100, years)[0]
            if type(gradient) != np.ndarray:
                gradient = np.array(gradient)
            if type(memory) != np.ndarray:
                memory = np.array(memory)
            self.save_load(name, memory.tolist(), None, gradient.tolist(), wordlist1, None, years, True)
        self.feeling /= len(self.k)
    def feelings_2(self, scale="None"):
        f_vec = np.zeros(6)
        av_word = np.zeros(6)
        for key, value in self.person.pers.items():
            memory, gradient, wordlist1, years = self.save_load(key, True, False, True, True, False, True, False)
            memory, wordlist1, gradient = self.check_lists(memory, wordlist1, gradient, years, scale=scale)
            fvec2, wordvec, f_d, years = value.feelings(memory, wordlist1, int(psutil.cpu_percent()) + 1, years)
            f_vec += np.array(fvec2)
            for i in range(len(wordvec)):
                av_word += np.array(wordvec[i])
            av_word /= len(wordvec)
            self.func_temp("feelings_2")
        av_word /= len(self.k)
        f_vec /= len(self.k)
        return f_vec, av_word
    def think(self, thought="", inf=""):
        quest_list = []
        memory_list = []
        errors_list = []
        gradient_list = []
        wordlist1_list = []
        answers = []
        years_list = []
        sides = self.k.copy()
        n = 0
        for j in range(len(sides)):
            name = sides[j]
            memory, errors, gradient, wordlist1, quest, years = self.save_load(name, True, True, True, True, True, True, False)
            memory_list.append(memory)
            errors_list.append(errors)
            gradient_list.append(gradient)
            wordlist1_list.append(wordlist1)
            quest_list.append(quest)
            years_list.append(years)
        counter = 0
        if thought == "":
            ans = "".join(self.person.pers[sides[0]].answer(None, quest_list[n - 1], wordlist1_list[n - 1], 1e-2, memory_list[n - 1], errors_list[n - 1], gradient_list[n - 1], answers, years_list[n - 1], learn=True)[1])
        else:
            ans = thought
        while counter < inf:
            if random.randint(1, 5) < 4:
                ans = self.person.pers[sides[n]].write(start=ans, wordlist1=wordlist1_list[n], memory=memory_list[n], errors=errors_list[n], gradient=gradient_list[n], years=years_list[n], endtlist=[], learn=True, t_end=random.randint(1, 10))[1]
            else:
                ans = self.person.pers[sides[n]].answer(ans, quest_list[n], wordlist1_list[n], 1e-2, memory_list[n], errors_list[n], gradient_list[n], answers, years_list[n], learn=True)[0]
            print(f"thought {self.name} {n}:", ans)
            f, diff = self.decide(ans, memory_list[n], wordlist1_list[n], gradient_list[n], years_list[n])
            vector = np.zeros(6)
            ans_ = ans.split()
            for e in range(len(ans_)):
                vector += self.person.pers[sides[n]].average_vector(ans[e], memory_list[n], wordlist1_list[n], gradient_list[n], years_list[n])
            vector /= len(ans_)
            co_so2 = copy.deepcopy(self.person.pers[sides[n]].co_so)
            for key, value in self.person.pers[sides[n]].co_so.items():
                v1 = copy.deepcopy(value)
                for key2, value2 in value.everyone.items():
                    if vector[0] != 0:
                        value2.love += value2.love / vector[0]
                    if vector[1] != 0:
                        value2.hate += value2.hate / vector[1]
                    if vector[2] != 0:
                        value2.fear += value2.fear / vector[2]
                    if vector[3] != 0:
                        value2.joy += value2.joy / vector[3]
                    if vector[4] != 0:
                        value2.tired += value2.tired / vector[4]
                    if vector[5] != 0:
                        value2.sad += value2.sad / vector[5]
                    v1.everyone.pop(key2)
                    v1.everyone.update({key2: value2})
                co_so2.pop(key)
                co_so2.update({key: v1})
            self.person.pers[sides[n]].co_so = co_so2
            if f == self.think:
                f(thought, random.randint(1, 4))
            else:
                f()
            counter += 1
            n += 1
            n = n % len(sides)
            self.func_temp("think")
    def decide(self, thought: str, memory, wordlist1, gradient, years):
        thought = thought.split()
        vec = np.zeros(6)
        for i in range(len(thought)):
            vec += self.average_vector(thought[i], memory, wordlist1, gradient, years)
        vec /= (abs(len(thought)) + 1)
        lists = []
        for key, value in self.f_dict.items():
            array = []
            k = key.split()
            for e in range(len(k)):
                array.append(float(k[e]))
            lists.append(array)
            self.func_temp("decide")
        diff = []
        for l in range(len(lists)):
            diff.append(abs(np.sum(vec - lists[l])))
        func = list(self.f_dict.values())[diff.index(min(diff))]
        r = func
        return r, diff
    def every(self, parts, scale):
        if parts == None:
            k = list(self.person.pers.keys())
        else:
            k = parts
        memory_list = []
        errors_list = []
        gradient_list = []
        wordlist1_list = []
        quest_list = []
        years_list = []
        for i in range(len(k)):
            name = k[i]
            memory, errors, gradient, wordlist1, quest, years = self.save_load(name, True, True, True, True, True, True, False)
            memory_list.append(memory)
            errors_list.append(errors)
            gradient_list.append(gradient)
            wordlist1_list.append(wordlist1)
            quest_list.append(quest)
            years_list.append(years)
            memory = memory_list[-1]
            wordlist1 = wordlist1_list[-1]
            years = years_list[-1]
            fn, vectors, f_d, years =  self.person.pers[k[i]].feelings(memory, wordlist1, 100, years)
            vectors = np.array(vectors)
        w1 = []
        memory = []
        gradient = []
        errors = []
        years = []
        for j in range(len(memory_list)):
            memory_list[j], wordlist1_list[j], gradient_list[j] = self.check_lists(memory_list[j], wordlist1_list[j], gradient_list[j], years_list[j], scale=scale)
            memory += list(memory_list[j])
            w1 += wordlist1_list[j]
            gradient += list(gradient_list[j])
            errors += errors_list[j]
        memory, w1, gradient = self.check_lists(memory, w1, gradient, int(np.sum(years_list)/len(years_list)))
        memory = np.array(memory)
        gradient = np.array(gradient)
        return k, memory_list, errors_list, gradient_list, wordlist1_list, quest_list, years_list, memory, w1, years, gradient, vectors
    def reset(self):
        parts = None
        scale = "None"
        k, memory_list, errors_list, gradient_list, wordlist1_list, quest_list, years_list, memory, wordlist1, years, gradient, vectors = self.every(parts, scale)
        dna = np.zeros(6)
        for i in range(len(memory)):
            dna += memory[i]
        dna /= len(memory)
        for j in range(len(dna)):
            while dna[j] / 10 > 1:
                dna[j] /= 10
            self.func_temp("reset")
        person = Person(f"{self.name}_Person", k, self.books2, 6, dna)
        s = Subjective(self.name, person)
        with open(f"i_am_{self.name}.pkl", "wb") as f:
            pickle.dump(s, f)
class Person(LM):
    def __init__(self, name: str, part_names: list[str], books: list[list[str]], dna: list[int] | list[float]) -> None:
        super().__init__(name, random.choice(books), dna)
        self.name = name
        self.pers = {}
        self.names = part_names
        self.books = books
        self.other = {}
        self.dna = dna.copy()
        for i in range(len(part_names)):
            self.pers.update({part_names[i]: LM(part_names[i], books[i], dna)})
        class_dict = {"Communism": r.Communism, "Anarchism": r.Anarchism, "Monarchism": r.Monarchism,
                      "w": r.World, "person": Person, "i_am": Subjective}
        classes = ["Communism", "Anarchism", "Monarchism", "w", "i", "person", "i_am"]
        classes += self.names
        for i in range(len(self.names)):
            class_dict.update({self.names[i]: LM})
        try:
            with open(f"{self.cwd}\\i_am_{self.name}.pkl", "rb") as f:
                self.i_am = pickle.load(f)
        except:
            self.i_am = 0
    def average(self, answers: list[str], wordlist1_list: list[list[str]], 
                memory_list: list[np.ndarray[np.ndarray[np.float64]]] | list[np.ndarray[np.ndarray[np.int64]]], 
                quest_list: list[dict], years) -> str:
        def ans(answer):
            for i in range(len(answer)):
                v_ans = np.zeros(len(memory_list[0][0]))
                counter = 0
                for j in range(len(answer[i])):
                    w = random.choice(wordlist1_list)
                    if len(memory_list[wordlist1_list.index(w)]) < len(w):
                        memory = list(memory_list[wordlist1_list.index(w)])
                        memory += self.arrays(len(memory), len(w) - len(memory), years)
                        memory = np.array(memory)
                        memory_list[wordlist1_list.index(w)] = copy.deepcopy(memory)
                    if answer[i][j] in w:
                        v_ans += memory_list[wordlist1_list.index(w)][w.index(answer[i][j])]
                        counter += 1
                if counter != 0:
                    v_ans /= counter
            return v_ans
        vector = np.zeros(len(memory_list[0][0]))
        for i in range(len(answers)):
            v = ans(answers[i])
            vector += v
        vector /= len(answers)
        d = []
        val = []
        for e in range(len(quest_list)):
            val += quest_list[e]
        all_a = np.zeros(len(memory_list[0][0]))
        for i in range(len(val)):
            v_a = ans(val[i])
            d.append(abs(np.sum(vector - v_a)))
            all_a += self.dna/(abs(v_a) + 1)
        all_a /= len(val)
        all_a *= np.array(self.dna)
        if self.i_am == 0:
            i_am = Person(f"{self.name}_1", self.names, self.books, len(all_a), all_a)
            self.i_am = Subjective(self.name, i_am)
            with open(f"i_am_{self.name}.pkl", "wb") as f:
                pickle.dump(self.i_am, f)
        return val[d.index(min(d))]
    def chat(self, names: list[str] | None, human=True) -> None:
        if names == None:
            names = list(self.pers.keys())
        memory_list = []
        errors_list = []
        gradient_list = []
        wordlist1_list = []
        quest_list = []
        years_list = []
        for i in range(len(names)):
            name = names[i]
            memory, errors, gradient, wordlist1, quest, years = self.save_load(name, True, True, True, True, True, True, False)
            memory_list.append(memory)
            errors_list.append(errors)
            gradient_list.append(gradient)
            wordlist1_list.append(wordlist1)
            quest_list.append(quest)
            years_list.append(years)
        av_memory = np.zeros((len(memory_list[0]), len(memory_list[0][0])))
        for i in range(len(memory_list)):
            for j in range(len(memory_list[i])):
                av_memory[i] += memory_list[i][j]
        j = " "
        answers = []
        sides = []
        for v in range(len(names)):
            sides.append(self.pers[names[v]])
        if human == True:
            a = input(j)
            while a != "всё":
                ans_list = []
                for i in range(len(sides)):
                    an, endt, memory_list[i], errors_list[i], gradient_list[i], answers, years_list[i], f_d = sides[i].answer(a, quest_list[i], wordlist1_list[i], 1e-2, memory_list[i], errors_list[i], gradient_list[i], answers, years_list[i], learn=False)
                    answers = []
                    ans_list.append(an)
                an = self.average(ans_list, wordlist1_list, memory_list, quest_list, years)
                print(f"{self.name}:", an)
                a = input(j)
        else:
            ans = ["".join(sides[0].answer(None, quest_list[1], wordlist1_list[1], 1e-2, memory_list[1], errors_list[1], gradient_list[1], answers, years_list[1], learn=True)[1])]
            near = 1
            while True:
                for i in range(near, len(sides)):
                    if random.randint(1, 5) < 4:
                        a = sides[i].write(start=ans[-1], wordlist1=wordlist1_list[i], memory=memory_list[i], errors=errors_list[i], gradient=gradient_list[i], years=years_list[i], endtlist=[], learn=True)[1]
                    else:
                        a = sides[i].answer(ans[-1], quest_list[i], wordlist1_list[i], 1e-2, memory_list[i], errors_list[i], gradient_list[i], answers, years_list[i], learn=True)[0]
                    print(f"{self.name} {i}:", a)
                    ans.append(a)
                near = 0
        for i in range(len(names)):
            name = names[i]
            self.save_load(name, memory_list[i].tolist(), errors_list[i], gradient_list[i].tolist(), wordlist1_list[i], quest_list[i], years_list[i], True)
class City():
    def __init__(self) -> None:
        self.LM_dict = {}
        self.person_dict = {}
    def new_LM(self, names: list[str], books: list[list[str]], TRNG_numbers: list[list[float]] | list[list[int]]):
        for j in names:
            self.LM_dict.update({j: LM(j, books[names.index(j)], TRNG_numbers)})
    def new_Person(self, name: str, parts: list[str], books: list[list[str]], TRNG_numbers: list[int] | list[float], tree: bool, leaves: int):
        self.person_dict.update({name: Person(name, parts, books, TRNG_numbers)})
        for i in range(len(parts)):
            if parts[i] not in list(self.LM_dict.keys()):
                self.new_LM([parts[i]], [books[i]], TRNG_numbers)
    def person_elements(self, name):
        m = []
        w = []
        for key, value in self.person_dict[name].pers.items():
            memory, wordlist1 = value.save_load(key, memory=True, wordlist1=True, save_True_load_False=False)
            w.append(wordlist1)
            m.append(memory)
        m2 = []
        ww = copy.deepcopy(w)
        www = []
        for j in range(len(ww)):
            www += list(ww[j])
            m2 += list(m[j])
        ww = copy.deepcopy(www)
        www = np.unique(np.array(www))
        m0 = []
        for i in range(len(www)):
            m0.append(list(list(self.person_dict[name].pers.values())[0].average_vector(www[i], m2, ww, [], 0, False)))
        with open(f"m_{name}.json", "w", encoding="utf-8") as f:
            json.dump(m0, f)
        with open(f"w_{name}.json", "w", encoding="utf-8") as f:
            json.dump(ww, f)
    def update(self):
        memory = []
        wordlist = []
        k = list(self.person_dict.keys())
        for key, value in self.person_dict.items():
            try:
                memory1, wordlist1_1 = list(list(self.person_dict.values())[0].pers.values())[0].save_load(key, memory=True, wordlist1=True, save_True_load_False=False)
            except:
                self.person_elements(key)
            m, wordlist1 = value.save_load(key, memory=True, wordlist1=True, save_True_load_False=False)
            memory.append(m.tolist())
            wordlist.append(wordlist1)
        for j in range(len(memory)):
            k2 = copy.deepcopy(k)
            w2 = copy.deepcopy(wordlist)
            m0 = copy.deepcopy(memory)
            w2.remove(wordlist[j])
            m0.remove(memory[j])
            k2.remove(k[j])
            other = {}
            for z in range(len(w2)):
                d = []
                for l in range(len(wordlist[j])):
                    if wordlist[j][l] in w2[z]:
                        d.append(abs(np.sum(np.array(memory[j][l]) - np.array(m0[z][w2[z].index(wordlist[j][l])]))))
                d = np.sum(d)/(abs(len(d)) + 1)
                other.update({k2[z]: 1/(abs(d) + 1)})
            self.person_dict[list(self.person_dict.keys())[j]].other = other
    def part_learn_quest(self, name, epochs=1, learning_rate=1e-5, learn=True) -> None:
        thoughts = []
        e1 = epochs
        try:
            m, errors, gradient, wordlist1, quest, years = self.LM_dict[name].save_load(name, True, True, True, True, True, True, False)
        except:
            years = 0
            wordlist1 = self.LM_dict[name].read(["—", ";", ":", "(", ")", "«", "»", "„", "“", "?", "!", "[", "]", 
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", 
                                    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", 
                                    "d", "f", "g", "h", "j"," k", "l", "z", "x", "c", "v", "b", "n", "m",
                                    "C", "D", "B", "E", ".", " "])
            quest = self.LM_dict[name].questions(self.LM_dict[name].books)
            endt, endt2, m, errors, gradient, answers, years, f_d = self.LM_dict[name].answer(None, quest, [], learning_rate, [], [0], [], [], years, learn=learn)
            self.LM_dict[name].save_load(name, m.tolist(), errors, gradient.tolist(), wordlist1, quest, years, True)
            print(endt2, np.sum(errors)/len(errors))
            epochs -= 1
        for i in range(epochs):
            endt, endt2, m, errors, gradient, answers, years, f_d = self.LM_dict[name].answer(None, quest, wordlist1, learning_rate, m, errors, gradient, [], years, learn=learn)
            thoughts.append(endt)
            print(endt2, np.sum(errors)/len(errors))
        self.LM_dict[name].save_load(name, m.tolist(), errors, gradient.tolist(), wordlist1, quest, years, True)
    def two(self, names, inf=""):
        memory_list = []
        errors_list = []
        gradient_list = []
        wordlist1_list = []
        quest_list = []
        years_list = []
        for i in range(len(names)):
            k = list(self.person_dict[names[i]].pers.keys())
            for j in range(len(k)):
                name = k[j]
                memory, errors, gradient, wordlist1, quest, years = self.person_dict[names[i]].pers[k[j]].save_load(name, True, True, True, True, True, True, False)
                memory_list.append(memory)
                errors_list.append(errors)
                gradient_list.append(gradient)
                wordlist1_list.append(wordlist1)
                quest_list.append(quest)
                years_list.append(years)
        start = random.choice(list(random.choice(quest_list).keys()))
        ans_co = [start]
        near = 2
        counter = 0
        while counter < inf:
            answer = []
            for j in range(near - 1, len(names)):
                answers = []
                k = list(self.person_dict[names[j]].pers.keys())
                values_list = list(self.person_dict[names[j]].pers.values())
                for l in range(len(k)):
                    answers.append(self.person_dict[names[j]].pers[k[l]].write(start=ans_co[-1], wordlist1=wordlist1_list[l*j], memory=memory_list[l*j], errors=errors_list[l*j], gradient=gradient_list[l*j], years=years_list[l*j], endtlist=[], learn=True, t_end=random.randint(1, 10))[1])
                for m in range(1, len(answers)):
                    answers[m] = answers[m].split()
                d = []
                word = []
                if len(ans_co[-1].split()) > 0:
                    answer.append(ans_co[-1].split()[-1])
                else:
                    if len(answer) > 0:
                        if len(answer[-1].split()[-1]) == 0:
                            answer.append(" ")
                        else:
                            answer.append(answer[-1].split()[-1])
                    else:
                        answer.append(" ")
                kk = list(self.person_dict[names[j - 1]].pers.values())
                for v in range(len(answers)):
                    word.append(answers[v])
                    f = random.choice(wordlist1_list)
                    counter = 0
                    while answer[-1] not in f or counter < 50:
                        f = random.choice(wordlist1_list)
                        counter += 1
                    d.append(abs(np.sum(values_list[v].average_vector(answers[v], memory_list[v], wordlist1_list[v], gradient_list[v], years_list[v]) - kk[wordlist1_list.index(f)%len(kk)].average_vector([answer][-1], memory_list[wordlist1_list.index(f)%len(kk)], wordlist1_list[wordlist1_list.index(f)%len(kk)], gradient_list[wordlist1_list.index(f)%len(kk)], years_list[wordlist1_list.index(f)%len(kk)]))))
                answer.append(word[d.index(min(d))])
                answer = answer[1:]
                vector = np.zeros(6)
                for b in range(len(answer)):
                    vector += kk[wordlist1_list.index(f)%len(kk)].average_vector([answer][b], memory_list[wordlist1_list.index(f)%len(kk)], wordlist1_list[wordlist1_list.index(f)%len(kk)], gradient_list[wordlist1_list.index(f)%len(kk)], years_list[wordlist1_list.index(f)%len(kk)])
                vector /= len(answer)
                co_so2 = copy.deepcopy(kk[wordlist1_list.index(f)%len(kk)].co_so)
                for key, value in kk[wordlist1_list.index(f)%len(kk)].co_so.items():
                    v1 = copy.deepcopy(value)
                    for key2, value2 in value.everyone.items():
                        if vector[0] != 0:
                            value2.love += value2.love / vector[0]
                        if vector[1] != 0:
                            value2.hate += value2.hate / vector[1]
                        if vector[2] != 0:
                            value2.fear += value2.fear / vector[2]
                        if vector[3] != 0:
                            value2.joy += value2.joy / vector[3]
                        if vector[4] != 0:
                            value2.tired += value2.tired / vector[4]
                        if vector[5] != 0:
                            value2.sad += value2.sad / vector[5]
                        v1.everyone.pop(key2)
                        v1.everyone.update({key2: value2})
                    co_so2.pop(key)
                    co_so2.update({key: v1})
                kk[wordlist1_list.index(f)%len(kk)].co_so = co_so2
                for z in range(len(kk)):
                    kk[z]
                a2 = []
                for q in range(len(answer)):
                    a2.append(answer[q])
                    a2.append(" ")
                a2 = "".join(a2)
                ans_co.append(a2)
                print(j, ans_co[-1])
            counter += 1
            near = f
    def person_learn_quest(self, name, epochs=1, lr=1e-5, learn=True) -> None:
        for key in self.person_dict[name].pers.keys():
            self.part_learn_quest(key, epochs=epochs, learning_rate=lr, learn=learn)
    def chat_Person(self, name: str, names: list[str] | None, human=True) -> None:
        self.person_dict[name].chat(names, human)
    def persons_chat(self, names, inf):
        counter = 0
        while counter < inf:
            for i in range(len(names)):
                self.person_dict[names[i]].i_am.think(inf=1)
                vec = list(self.person_dict[names[i]].i_am.feelings_2()[0])
                if vec.index(min(vec)) in [1, 2, 4, 5]:
                    b = []
                    for key, value in self.person_dict[names[i]].other.items():
                        for j in range(int(value*1000)):
                            b.append(key)
                    self.two([names[i], random.choice(b)], random.randint(1, inf))
            counter += 1
    def threads_chat(self, names, inf):
        names2 = copy.deepcopy(names)
        names2.reverse()
        t = [threading.Thread(target=self.persons_chat, args=(names, inf)), threading.Thread(target=self.persons_chat, args=(names2, inf))]
        for thread in t:
            thread.start()
        for thread in t:
            thread.join()
