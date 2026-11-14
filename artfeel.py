import random 
import matplotlib.pyplot as plt
import time 

class Act():
    def __init__(self):
        self.everyone = {}
        self.art = {}
        self.symbols = ["~", "@", "*", "?", "&", " "]
        self.colors = {"love": [196, 220, 226], "sad": [90, 38, 51], "hate": [52, 67, 16], "fear": [238, 160, 16], 
                    "joy": [82, 226, 87], "tired": [68, 255, 250]}
        self.year = 0
    def new_society(self, people: int):
        """
        Creates new dictionary with classes One() {name: One()}.

        Parameters
        ----------
        people: int
            Length of dictionary.
        """
        for i in range(people):
            self.everyone.update({str(i): One(str(i), self.everyone)})
        for key, value in self.everyone.items():
            value.everyone = self.everyone
    def learn(self, person: str):
        """
        Changes some of one person parameters.

        Parameters
        ----------
        person: str
            Name of the person (class One()).
        """
        self.everyone[person].sub_good += random.randint(-5, 5)
        self.everyone[person].sub_bad += random.randint(-5, 5)
        if len(list(self.art.keys())) > 1:
            picture = self.art[list(self.art.keys())[random.randint(0, len(list(self.art.keys())) - 1)]]
            self.everyone[person].love += picture[1]/self.everyone[person].love
            self.everyone[person].hate += picture[2]/self.everyone[person].hate
            self.everyone[person].fear += picture[3]/self.everyone[person].fear
            self.everyone[person].joy += picture[4]/self.everyone[person].joy
            self.everyone[person].sad += picture[5]/self.everyone[person].sad
            self.everyone[person].tired += picture[6]/self.everyone[person].tired
            self.everyone[person].artmemory.append(picture[0][random.randint(0, len(picture[0]) - 1)])
    def create(self, person: str):
        """
        Person creates a "picture" from ANSI strings-pixels. Colors depend on the values of feelings.

        Parameters
        ----------
        person: str
            Name of person (class One()).
        """
        h = random.randint(10, 20)
        w = h
        self.paper = []
        fear = 0
        love = 0
        hate = 0
        sad = 0
        joy = 0
        tired  = 0
        for i in range(h):
            self.paper.append([])
            for j in range(w):
                if self.everyone[person].love > self.everyone[person].hate + random.randint(0, 10):
                    self.paper[i].append(f"\033[38;5;{self.colors["love"][random.randint(0, 2)]};48;5;{self.colors["love"][random.randint(0, 2)]}m {self.symbols[random.randint(0, len(self.symbols) - 1)]} \033[0m")
                    love += 1
                if self.everyone[person].hate > self.everyone[person].joy + random.randint(0, 10):
                    self.paper[i].append(f"\033[38;5;{self.colors["hate"][random.randint(0, 2)]};48;5;{self.colors["hate"][random.randint(0, 2)]}m {self.symbols[random.randint(0, len(self.symbols) - 1)]} \033[0m")
                    hate += 1
                if self.everyone[person].joy > self.everyone[person].sad + random.randint(0, 10):
                    self.paper[i].append(f"\033[38;5;{self.colors["joy"][random.randint(0, 2)]};48;5;{self.colors["joy"][random.randint(0, 2)]}m {self.symbols[random.randint(0, len(self.symbols) - 1)]} \033[0m")
                    joy += 1
                if self.everyone[person].sad > self.everyone[person].tired + random.randint(0, 10):
                    self.paper[i].append(f"\033[38;5;{self.colors["sad"][random.randint(0, 2)]};48;5;{self.colors["sad"][random.randint(0, 2)]}m {self.symbols[random.randint(0, len(self.symbols) - 1)]} \033[0m")
                    sad += 1
                if self.everyone[person].tired > self.everyone[person].fear + random.randint(0, 10):
                    self.paper[i].append(f"\033[38;5;{self.colors["tired"][random.randint(0, 2)]};48;5;{self.colors["tired"][random.randint(0, 2)]}m {self.symbols[random.randint(0, len(self.symbols) - 1)]} \033[0m")
                    tired += 1
                if self.everyone[person].fear > self.everyone[person].love + random.randint(0, 10):
                    self.paper[i].append(f"\033[38;5;{self.colors["fear"][random.randint(0, 2)]};48;5;{self.colors["fear"][random.randint(0, 2)]}m {self.symbols[random.randint(0, len(self.symbols) - 1)]} \033[0m")
                    fear += 1
                if random.randint(1, 20) == 20 and len(self.everyone[person].artmemory) > 0:
                    self.paper[i].append(self.everyone[person].artmemory[random.randint(0, len(self.everyone[person].artmemory) - 1)])
        show = []
        for k in range(len(self.paper)):
            show += "".join(self.paper[k])
            show += "\n"
        self.art.update({person + str(self.year): [show, love, hate, fear, joy, sad, tired, person]})
    def do_good(self, person: str, who: list[str]):
        """
        This function changes some feelings of the persons from who array to the positive direction, using one person.

        Parameters
        ----------
        person: str
            Name of that one person.

        who: list[str]
            Names of persons that this person will change.
        """
        for i in range(len(who)):
            if who[i] in self.everyone and person in self.everyone and person in self.everyone[who[i]].relate:
                c = (10/(abs(self.everyone[who[i]].sub_good - self.everyone[person].sub_good) + 1))
                self.everyone[who[i]].joy += c
                self.everyone[who[i]].hate -= c
                self.everyone[who[i]].sad -= c
                self.everyone[who[i]].love += c
                self.everyone[who[i]].fear -= c
                self.everyone[person].tired += c
                self.everyone[who[i]].relate[person][0] += c
                1234567890
                if random.randint(1, 3) == 1:
                    1234567890
                    if self.everyone[who[i]].sub_good < self.everyone[person].sub_good:
                        self.everyone[who[i]].sub_good += random.randint(1, 10)
                        self.everyone[person].sub_good -= random.randint(1, 10)
                    else:
                        self.everyone[who[i]].sub_good -= random.randint(1, 10)
                        self.everyone[person].sub_good += random.randint(1, 10) 
                1234567890
                if random.randint(1, 3) == 1:
                    1234567890
                    if self.everyone[who[i]].sub_bad < self.everyone[person].sub_bad:
                        self.everyone[who[i]].sub_bad += random.randint(1, 10)
                        self.everyone[person].sub_bad -= random.randint(1, 10)
                    else:
                        self.everyone[who[i]].sub_bad -= random.randint(1, 10)
                        self.everyone[person].sub_bad += random.randint(1, 10) 
    def do_bad(self, person, who):
        """
        This function changes some feelings of the persons from who array to the negative direction, using one person.

        Parameters
        ----------
        person: str
            Name of that one person.

        who: list[str]
            Names of persons that this person will change.
        """
        for i in range(len(who)):
            if who[i] in self.everyone and person in self.everyone and person in self.everyone[who[i]].relate:
                c = (10/(abs(self.everyone[who[i]].sub_bad - self.everyone[person].sub_bad) + 1))
                self.everyone[who[i]].joy -= c
                self.everyone[who[i]].hate += c
                self.everyone[who[i]].sad += c
                self.everyone[who[i]].love -= c
                self.everyone[who[i]].tired -= c
                self.everyone[who[i]].fear += c
                self.everyone[who[i]].relate[person][1] += c
                self.everyone[who[i]].relate[person][2] += c
                1234567890
                if random.randint(1, 3) == 1:
                    1234567890
                    if self.everyone[who[i]].sub_good < self.everyone[person].sub_good:
                        self.everyone[who[i]].sub_good -= random.randint(1, 10)
                        self.everyone[person].sub_good += random.randint(1, 10)
                    else:
                        self.everyone[who[i]].sub_good += random.randint(1, 10)
                        self.everyone[person].sub_good -= random.randint(1, 10) 
                1234567890
                if random.randint(1, 3) == 1:
                    1234567890
                    if self.everyone[who[i]].sub_bad < self.everyone[person].sub_bad:
                        self.everyone[who[i]].sub_bad -= random.randint(1, 10)
                        self.everyone[person].sub_bad += random.randint(1, 10)
                    else:
                        self.everyone[who[i]].sub_bad += random.randint(1, 10)
                        self.everyone[person].sub_bad -= random.randint(1, 10) 
class One(Act):
    def __init__(self, name: str, everyone):
        """
        This class is one person with feelings.

        Parameters
        ----------
        name: str
            Person`s name.
        
        everyone: dict
            Other persons. Dictionary {name: One()}.
        """
        super().__init__()
        self.args_dict = {"name": name, "everyone": everyone}
        self.everyone = everyone
        self.sub_good = random.randint(0, 10)
        self.sub_bad = random.randint(0, 10)
        self.o_good = 0
        self.o_bad = 0
        self.memory = []
        self.name = name
        self.tired = random.randint(0, 10)
        self.joy = random.randint(0, 10)
        self.sad = random.randint(0, 10)
        self.hate = random.randint(0, 10)
        self.love = random.randint(0, 10)
        self.fear = random.randint(0, 10)
        self.affect = random.randint(0, 10)
        self.emotions = {"love": self.love, "hate": self.hate, "joy": self.joy, "sad": self.sad, "fear": self.fear, "tired": self.tired}
        self.index = 0
        self.artmemory = []
        self.relate = {}
    def relation(self):
        """
        This functions calculates how one person relates to other person.
        """
        for key, value in self.everyone.items():
            self.relate.update({key: [1000/(abs(value.sub_good - self.sub_good + value.sub_bad - self.sub_bad) + 1), self.hate/len(list(self.everyone.keys())) + self.fear/len(list(self.everyone.keys())) + self.tired/len(list(self.everyone.keys())) - value.love/len(list(self.everyone.keys())) + value.hate/len(list(self.everyone.keys())), self.fear+(self.hate/len(list(self.everyone.keys())) + self.fear/len(list(self.everyone.keys())) + self.tired/len(list(self.everyone.keys())) - value.joy/len(list(self.everyone.keys())) - value.love/len(list(self.everyone.keys())) + value.hate/len(list(self.everyone.keys())))/100]})
    def years(self, create, year):
        """
        This method starts the simulation.

        Parameters
        ----------
        create: bool
            If True, the persons will draw their "pictures" and show to you.
            Else, they will not.
        
        year: int
            Max value of year. The "year" of the end of simulation.
        """
        ed2 = self.everyone.copy()
        self.relation()
        self.everyone = ed2
        for key, value in self.everyone.items():
            value.everyone = ed2
        self.o_good = self.sub_good / len(list(self.everyone.keys()))
        self.o_bad = self.sub_bad / len(list(self.everyone.keys()))
        feel = self.hate + self.love + self.fear + self.joy + self.sad + self.tired 
        1234567890
        if feel > 100:
            self.affect += feel/10
        random.seed((self.sub_good + self.sub_bad)*(3/4) + (self.o_good + self.o_bad)*(1/4))
        randc = [self.love, self.joy, self.tired, self.sad, self.fear, self.hate]
        self.index = int(1/(self.affect/100 + 1) % (len(randc) - 1))
        1234567890
        if self.affect > 100 and random.randint(1, 10) == 10:
            randc[random.randint(0, len(randc) - 1)] -= self.affect
            randc[random.randint(0, len(randc) - 1)] += self.affect
        if self.index > len(randc) - 1:
            self.index = random.randint(0, len(randc) - 1)
        1234567890
        if random.randint(1, 5) == 5:
            if self.o_good != float("nan") and self.o_bad != float("nan") and self.o_good != float("inf") and self.o_bad != float("inf"):
                if self.o_good < self.o_bad:   
                    self.memory.append(random.randint(int(self.o_good), int(self.o_bad))*randc[self.index])
                    self.sub_good += (self.memory[-1] - self.sub_good)
                    self.sub_bad += (self.memory[-1] - self.sub_bad)
                if self.o_good > self.o_bad:
                    self.memory.append(random.randint(int(self.o_bad), int(self.o_good))*randc[self.index])
                    self.sub_good += (self.memory[-1] - self.sub_good)
                    self.sub_bad += (self.memory[-1] - self.sub_bad)
        1234567890
        if self.hate <= self.love or self.sad <= self.joy or self.fear <= self.tired:
            coeff = 1
            1234567890
            if self.hate < self.love:
                coeff *= 3/4
            elif self.sad < self.joy or self.hate >= self.love:
                coeff *= 2/4
            elif self.tired < self.fear or self.sad >= self.joy or self.hate >= self.love:
                coeff *= 1/4
            else:
                coeff = 0
            do = random.randint(1, 100)/100
            good_r = []
            bad_r = []
            for key, value in self.relate.items():
                if value[0] >= 10:
                    good_r.append(key)
                if value[1] >= 10 and value[2] <= 10 and key not in good_r:
                    bad_r.append(key)
            if do > coeff:
                self.do_good(self.name, good_r)
            else:
                self.do_bad(self.name, bad_r)
        1234567890
        if self.tired < 30:
            self.learn(self.name)
        if self.tired < 5 and create == True:
            self.create(self.name)
            self.affect -= random.randint(0, 10)
            if input(f"{self.name} created a picture. Show? If yes, press Enter\n") == "":
                print("".join(self.art[self.name+str(self.year)][0]), "Love:", self.art[self.name+str(self.year)][1], "Hate:", self.art[self.name+str(self.year)][2], "Fear:", self.art[self.name+str(self.year)][3], "Joy:", self.art[self.name+str(self.year)][4], "Sad:", self.art[self.name+str(self.year)][5], "Tired:", self.art[self.name+str(self.year)][6])
                time.sleep(0.3)
        self.year += 1
        self.emotions = {"love": self.love, "hate": self.hate, "joy": self.joy, "sad": self.sad, "fear": self.fear, "tired": self.tired}
        if self.year >= year:
            return 0