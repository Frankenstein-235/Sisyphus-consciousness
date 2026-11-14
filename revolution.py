import artfeel_E_00000002 as art
import random
import matplotlib.pyplot as plt

class Anarchism():
    def __init__(self) -> None:
        """
        Anarchism is one of ideologies that you can choose.
        """
        self.news = 1
        self.equal = 9
        self.military = 1
        self.gdp = 3
        self.work = 7
        self.nation = 0
        self.terror = 7
        self.iname = "Anarchism"
class Communism():
    def __init__(self) -> None:
        """
        Communism is one of ideologies that you can choose.
        """
        self.news = 9
        self.equal = 7
        self.military = 9
        self.gdp = 7
        self.work = 10
        self.nation = 3
        self.terror = 7
        self.iname = "Communism"
class Monarchism():
    def __init__(self) -> None:
        """
        Monarchism is one of ideologies that you can choose.
        """
        self.news = 4
        self.equal = 1
        self.military = 4
        self.gdp = 8
        self.work = 6
        self.nation = 5
        self.terror = 2
        self.iname = "Monarchism"

class Ideology():
    def __init__(self, i) -> None:
        """
        Parameters
        ----------
        i: str
            Ideology name. Must be "Anarchism", "Communism" or "Monarchism"
        """
        super().__init__()
        self.args_dict = {"i": i}
        self.science = random.randint(10, 20)
        self.i_dict = {"Communism": Communism(), "Anarchism": Anarchism(), "Monarchism": Monarchism()}
        self.left = {"Communism": 4, "Anarchism": 1, "Monarchism": -4}
        self.i = self.i_dict[i]
        self.aggression = 0
        self.revolution = 0
    def propaganda(self) -> None:
        self.aggression += self.i.news/10
        self.revolution -= 3.5
        self.i.terror += 1
        self.i.news += random.randint(1, 100)/10

class People(Ideology):
    def __init__(self, i) -> None:
        super().__init__(i)
        self.args_dict = {"i": i}
        self.population = {"m": [20, 25], "w": [20, 25]}
        for i in range(1000):
            self.population["m"].append(random.randint(0, 100))
            self.population["w"].append(random.randint(0, 100))
        self.war = False
        self.is_revolution = False
        self.famine = False
        self.parents = []
        self.disease = False
        self.epidemic = []
        self.diseases = {"Covid-19": 1e4, "Plague": 1e4, "Smallpox": 1e5, "Anthrax": 1e6, "Ebola": 1e6}
        self.workplace = 1000
        self.everyone = self.population["m"] + self.population["w"]
    def dem(self) -> None:
        """
        This method is for adding new people to country population.
        """
        num = random.randint(0, 10)
        s = ["m", "w"]
        if num < 10 and max(self.population["m"]) > 18 and max(self.population["w"]) > 18:
            for i in range(random.randint(1, 3)):
                self.population[s[random.randint(0, 1)]].append(0)
            mp = []
            wp = []
            for j in range(len(self.population["m"])):
                if self.population["m"][j] > 18:
                    mp.append(j)
            for k in range(len(self.population["w"])):
                if self.population["w"][k] > 18:
                    wp.append(k)
            if len(mp) > 0 and len(wp) > 0:
                self.parents.append([str(random.choice(mp)), str(random.choice(wp))])
    def death(self, coeff: int | float) -> None:
        """
        This method removes people from country population.

        Parameters
        ----------
        coeff: int | float
            If this coefficient is small, probability of death is big. Else, probability of death is small.
        """
        s = ["m", "w"]
        if self.war == True:
            self.aggression += 5
        if self.famine == True:
            self.aggression += 15
        if self.disease == True:
            self.aggression += 10
        num = random.randint(0, int(len(self.everyone) * coeff))
        mw = s[random.randint(0, 1)]
        if num < len(self.everyone) / 2:
            if len(self.population[mw]) > 0:
                self.population[mw].remove(self.population[mw][random.randint(self.population[mw].index(max(self.population[mw])), len(self.population[mw]) - 1)])
class Economy(People):
    def __init__(self, i: str, name: str) -> None:
        """
        Class for economy of country. Contains methods for fabrics, schools, dictionaries with resources.

        Parameters
        ----------
        i: str
            Ideology name. Must be only "Anarchism", "Communism" or "Monarchism".
        
        name: str
            Name of the country.
        """
        super().__init__(i)
        self.args_dict = {"i": i, "name": name}
        self.name = name
        self.weapon = 0
        self.fabrics = []
        self.rtypes = ["weapon", "petroleum", "food", "iron", "clock", "water", "books", "uranium"]
        self.fresources = {"weapon": 0, "food": 0, "books": 0, "clock": 0}
        self.mresources = {"petroleum": 0, "iron": 0, "water": 0, "uranium": 0}
        self.allr = self.fresources | self.mresources
        self.energy = 0
        self.sources = []
        self.bad = [[], [], [], []]
        self.generators = []
        self.units = 0
        self.wmoney = 0
        self.prices = []
        self.inflation = 0
        self.bill = 0
        self.gdplist = []
        self.inflationlist = []
        self.populationlist = []
        self.weaponlist = []
        self.foodlist = []
        self.bookslist = []
        self.clocklist = []
        self.petroleumlist = []
        self.ironlist = []
        self.uraniumlist = []
        self.waterlist = []
        self.workers = []
        self.pay = {"weapon": 20, "food": 10, "books": 10, "clock": 20, "petroleum": 100, 
                    "iron": 50, "water": 75, "uranium": 200}
        self.cw = {"weapon": 10, "food": 5, "books": 7, "clock": 9}
        self.cm = {"petroleum": 10, "iron": 5, "water": 10, "uranium": 20}
    def new_fabric(self, *args) -> None:
        """
        This method creates new fabric.
        If you want, you can to add the arguments (in *args).

        Parameters
        ----------
        *args: str
            *args[0] (first argument) should be the name of fabric type: "weapon", "food", "books" or "clock".
        """
        money = random.randint(1, 10)
        self.i.gdp += money/(abs(self.i.nation) + 1)
        self.bill -= money/(abs(self.i.nation) + 1)
        if len(args) == 0:
            t = random.randint(0, len(list(self.fresources.keys())) - 1)
            self.fabrics.append([random.randint(5, 9) * (self.i.nation + self.i.equal + self.i.news), list(self.fresources.keys())[t], self.cw[list(self.fresources.keys())[t]]])
        else:
            count = random.randint(5, self.cw[args[0]])
            self.fabrics.append([random.randint(5, 9) * (self.i.nation + self.i.equal), args[0], count])
            self.workplace += count
    def new_school(self) -> None:
        """
        This method creates new school.
        """
        k = random.randint(1, 10)
        self.i.gdp += k*(self.science+1)
        self.bill -= k*(self.science+1)
        self.i.nation += random.randint(1, 5)
        self.science += random.randint(1, 5)
    def new_university(self) -> None:
        """
        This method creates new university.
        """
        k = random.randint(10, 20)
        self.i.gdp += k*(self.science+1)
        self.bill -= k*(self.science+1)
        self.i.nation += random.randint(1, 10)
        self.science += random.randint(1, 10)
    def explore(self) -> None:
        """
        This method finds new resources source ("petroleum", "water", "iron", "uranium")
        """
        rtype = random.randint(0, len(list(self.mresources.keys())) - 1)
        if self.science > random.randint(0, 20):
            self.sources.append([list(self.mresources.keys())[rtype], random.randint(100, 1000)])
            self.i.nation += self.science
    def mine(self, snum) -> None:
        """
        This method mines random number of resources from source with index snum.

        Parameters
        ----------
        snum: int 
            Index of the source.
        """
        if len(self.sources) > 1:
            h = random.randint(int(self.sources[snum][1]/10), int(self.sources[snum][1]))
            self.sources[snum][1] -= h
            self.energy += h/2
            self.mresources[self.sources[snum][0]] += h/2
            if self.sources[snum][1] == 0:
                self.sources.remove(self.sources[snum])
            k = random.randint(1, 10)
            self.i.gdp += k
    def newgenerator(self) -> None:
        """
        This method creates new generator of energy.
        """
        b = random.randint(1, 100)
        self.generators.append(random.randint(2, 10))
        self.i.gdp += b/10
    def generate(self) -> None:
        """
        Creates energy for fabrics and other things.
        """
        for i in range(len(self.generators)):
            self.energy += self.generators[i]
    def newworker(self) -> None:
        """
        Adds new worker if there is new people at the age >= 18.
        """
        for k in range(len(self.population["m"])):
            if self.population["m"][k] >= 18 and ["m", k, "weapon"] not in self.workers and ["m", k, "food"] not in self.workers and ["m", k, "petroleum"] not in self.workers:
                a = random.randint(0, 100//self.i.work)
                numtype = random.randint(0, len(self.rtypes) - 1)
                if a > (100//self.i.work / 1.5):
                    self.workers.append(["m", k, self.allr[self.rtypes[numtype]]])
                    self.workplace -= 1
                    self.i.work += 1
        for j in range(len(self.population["w"])):
            if self.population["w"][j] >= 18:
                a = random.randint(0, 100//self.i.work)
                numtype = random.randint(0, len(self.rtypes) - 1)
                if a > (100//self.i.work / 1.5):
                    if self.rtypes[numtype] in self.allr:
                        self.workers.append(["w", j, self.allr[self.rtypes[numtype]]])
                    self.workplace -= 1
                    self.i.work += 1
        self.units += self.pay[self.workers[-1][2]]
    def output(self) -> None:
        """
        Prints current stats.
        """
        print("Year:", len(self.gdplist))
        for key, value in self.i_dict.items():
            if value == self.i: 
                print("Ideology:", key)
        print("Population:", len(self.everyone), "Men:", self.population["m"], "Women:", self.population["w"])
        print("GDP:", self.i.gdp)
        print("GDP per capita", self.i.gdp/(len(self.everyone) + 1))
        print("Science:", self.science)
        print("Epidemic:", self.epidemic)
        print("Work:", self.i.work)
        print("Sources:", self.sources)
        print("Nation:", self.i.nation)
        print("Military:", self.i.military)
        print("Propaganda:", self.i.news)
        print("Terror:", self.i.terror)
        print("Equal:", self.i.equal)
        print("War:", self.war)
        print("Resources:", self.fresources)
        print("Fabrics:", self.fabrics)
        print("Aggression:", self.aggression)
        print("Bill:", self.bill)
        print("Inflation:", self.inflation)
        print("Revolution:", self.revolution)

class Country(Economy):
    def __init__(self, i: str, name: str, countries: list[str], ideologies: list[str]) -> None:
        """
        This class is a country. A country has it`s own economy class. The country can war with other countries, buy or sell.

        Parameters
        ----------
        i: str
            Ideology of the country.
        
        name: str
            Name of the country.
        
        countries: list[str]
            Names of other countries.
        
        ideologies: list[str]
            Names of other countries ideologies.
        """
        super().__init__(i, name)
        self.args_dict = {"i": i, "name": name, "countries": countries, "ideologies": ideologies}
        self.countries_dict = {}
        for j in range(len(countries)):
            self.countries_dict.update({countries[j]: Economy(ideologies[j], countries[j])})
        self.name = name
        self.xn = 0
        self.i = self.i_dict[i]
        self.warlist = []
        self.relations = {}
        self.country_years = {}
        self.sold_to = {}
        self.st_list = []
        self.new_fabric("weapon")
        self.new_fabric("food")
        self.new_fabric("books")
        self.new_fabric("clock")
        self.new_school()
        self.new_university()
        self.newgenerator()
    def peace(self, c2: str) -> None:
        """
        End war with other country.

        Parameters
        ----------
        c2: str
            The country you need to end war with.
        """
        self.countries_dict[c2].war = False
        self.countries_dict[c2].warlist = []
        self.war = False
        self.aggression = 4
        self.i.terror = 2
        self.i.news += 5
        self.warlist = []
    def startwar(self, c2: str) -> None:
        """
        Start war with other country.
        
        Parameters
        ----------
        c2: str
            Name of country you need to start war with.
        """
        self.countries_dict[c2].war = True
        self.war = True
        self.warlist.append(c2)
    def relationship(self) -> None:
        """
        Builds dictionary of relationship with other countries (depending on ideology).
        """
        for key, value in self.countries_dict.items():
            if key != self.name:
                self.relations.update({key: self.left[value.i.iname] - self.left[self.i.iname]})
    def war_action(self) -> None:
        """
        War action with other country.
        """
        for j in self.warlist:
            if self.i.military >= self.countries_dict[j].i.military * 2 and self.fresources["weapon"] >= self.countries_dict[j].fresources["weapon"] * 3:
                self.win(j)
                break
            act = random.randint(0, 3)
            if act == 0:    
                continue
            elif act == 1:
                if self.i.terror > self.countries_dict[j].i.terror:
                    self.countries_dict[j].i.military -= self.i.military
                elif self.i.terror < self.countries_dict[j].i.terror:
                    self.i.military -= self.countries_dict[j].i.military
            elif act == 2:
                if self.i.terror > self.countries_dict[j].i.terror:
                    self.fresources["weapon"] *= 1.5
                elif self.i.terror < self.countries_dict[j].i.terror:
                    self.fresources["weapon"] /= 1.5
            else:
                p = random.randint(1, 30)
                if p == 1:
                    self.peace(j)
                    break
    def win(self, c2: str) -> None:
        """
        This method is called when the country wins.
        
        Parameters
        ----------
        c2: str
            The country that was defeated.
        """
        for key, value in self.countries_dict[c2].fresources.items():
            self.fresources[key] += value/random.randint(1, 10)
            self.countries_dict[c2].fresources[key] -= value/random.randint(1, 10)
        for key, value in self.countries_dict[c2].mresources.items():
            self.mresources[key] += value/random.randint(1, 10)
            self.countries_dict[c2].mresources[key] -= value/random.randint(1, 10)
        self.population["m"] += self.countries_dict[c2].population["m"][0:int(len(self.countries_dict[c2].population["m"])*random.randint(1, 10)/10)]
        self.population["w"] += self.countries_dict[c2].population["w"][0:int(len(self.countries_dict[c2].population["w"])*random.randint(1, 10)/10)]
        self.i.military += self.countries_dict[c2].i.military/(random.randint(1, 10)/10)
        self.i.terror += self.countries_dict[c2].i.terror/(random.randint(1, 10)/10)
        self.revolution += self.countries_dict[c2].revolution/(random.randint(1, 10)/10)
        self.i.equal -= self.countries_dict[c2].i.equal/(random.randint(1, 10)/10)
        self.fabrics += self.countries_dict[c2].fabrics[0:int(len(self.countries_dict[c2].fabrics)*random.randint(1, 10)/10)]
        self.generators += self.countries_dict[c2].fabrics[0:int(len(self.countries_dict[c2].generators)*random.randint(1, 10)/10)]
        self.energy += self.countries_dict[c2].energy/(random.randint(1, 10)/10)
        self.aggression += self.countries_dict[c2].aggression/(random.randint(1, 10)/10)
        self.i.gdp += self.countries_dict[c2].i.gdp/(random.randint(1, 10)/10)
        self.bill += self.countries_dict[c2].bill/(random.randint(1, 10)/10)
        self.i.news -= self.countries_dict[c2].i.news/(random.randint(1, 10)/10)
        self.i.work += self.countries_dict[c2].i.work/(random.randint(1, 10)/10)
        self.war = False
        self.countries_dict[c2].war = False
        self.aggression = 10
        self.i.terror = 5
        self.i.news += 10
        self.warlist = []
        self.countries_dict[c2].warlist = []
    def buy(self, thing: str, units: int | float, c2: str) -> None:
        """
        Buy something from other country.

        Parameters
        ----------
        thing: str
            Name of resource that you want to buy.
        
        units: int | float
            How many of this thing you need to buy.
        
        c2: str
            Name of the country you are buying from.
        """
        if thing in self.fresources:
            if self.countries_dict[c2].fresources[thing] > 0:
                self.countries_dict[c2].fresources[thing] -= units
                self.countries_dict[c2].i.gdp += self.fresources[thing] / (self.i.gdp + 1) / (self.relations[c2] + 4.1)
                self.countries_dict[c2].i.gdp -= self.fresources[thing] / (self.i.gdp + 1) / (self.relations[c2] + 4.1)
                self.fresources[thing] -= units
                self.xn -= self.fresources[thing] / (self.i.gdp + 1) / (self.relations[c2] + 4.1)
        if thing in self.mresources:
            if self.countries_dict[c2].mresources[thing] > 0:
                self.countries_dict[c2].mresources[thing] -= units
                self.countries_dict[c2].i.gdp += self.mresources[thing] / (self.i.gdp + 1) / (self.relations[c2] + 4.1)
                self.countries_dict[c2].i.gdp -= self.mresources[thing] / (self.i.gdp + 1) / (self.relations[c2] + 4.1)
                self.mresources[thing] -= units
                self.xn -= self.mresources[thing] / (self.i.gdp + 1) / (self.relations[c2] + 4.1)
        if len(self.countries_dict[c2].epidemic) > 0:
            if random.randint(1, 150) == 100:
                self.epidemic.append(self.countries_dict[c2].epidemic[random.randint(0, len(self.countries_dict[c2].epidemic) - 1)])
                self.countries_dict[c2].disease = True
    def sell(self, thing: str, units: int | float, c2: str) -> None:
        """
        Sell something to other country.

        Parameters
        ----------

        thing: str
            Name of thing you need to sell.

        units: int | float
            How many of this thing you need to sell.
        
        c2: str
            Name of the country you selling this thing to.
        """
        if thing in self.fresources:
            self.fresources[thing] -= units
            self.countries_dict[c2].i.gdp -= self.countries_dict[c2].fresources[thing] / (self.countries_dict[c2].i.gdp + 1) * (self.relations[c2] + 4.1)
            self.countries_dict[c2].fresources[thing] += units
            self.xn += self.countries_dict[c2].fresources[thing] / (self.countries_dict[c2].i.gdp + 1) * (self.relations[c2] + 4.1)
            if self.countries_dict[c2].fresources[thing] > 0:
                self.xn /= self.countries_dict[c2].fresources[thing]
        else:
            self.mresources[thing] -= units
            self.countries_dict[c2].i.gdp -= self.countries_dict[c2].mresources[thing] / (self.countries_dict[c2].i.gdp + 1) * (self.relations[c2] + 4.1)
            self.countries_dict[c2].mresources[thing] += units
            self.xn += self.countries_dict[c2].mresources[thing] / (self.countries_dict[c2].i.gdp + 1) * (self.relations[c2] + 4.1)
            if self.countries_dict[c2].mresources[thing] > 0:
                self.xn /= self.countries_dict[c2].mresources[thing]
        if len(self.epidemic) > 0:
            if random.randint(1, 150) == 100:
                self.countries_dict[c2].epidemic.append(self.epidemic[random.randint(0, len(self.epidemic) - 1)])
                self.disease = True

class World(People):
    def __init__(self, countries: list[str], ideologies: list[str]) -> None:
        """
        Major class that connects other classes to each other.

        Parameters
        ----------
        countries: list[str]
            Array of country names.
        
        ideologies: list[str]
            Array of country ideologies.
        """
        super().__init__(random.choice(ideologies))
        self.args_dict = {"countries": countries, "ideologies": ideologies}
        self.countries_dict = {}
        self.tips = 0
        for i in range(len(countries)):
            self.countries_dict.update({countries[i]: Country(ideologies[i], countries[i], countries, ideologies)})
        for j in range(len(countries)):
            self.countries_dict[countries[j]].relationship()
        self.sold = []
    def year(self, name: str, temp) -> None:
        """
        One year of country.

        Parameters
        ----------
        name: str
            Name of the country.
        """
        price = 0
        self.countries_dict[name].gdplist.append(self.countries_dict[name].i.gdp)
        self.countries_dict[name].inflationlist.append(self.countries_dict[name].inflation)
        self.countries_dict[name].populationlist.append(len(self.countries_dict[name].everyone))
        self.countries_dict[name].weaponlist.append(self.countries_dict[name].fresources["weapon"])
        self.countries_dict[name].foodlist.append(self.countries_dict[name].fresources["food"])
        self.countries_dict[name].bookslist.append(self.countries_dict[name].fresources["books"])
        self.countries_dict[name].clocklist.append(self.countries_dict[name].fresources["clock"])
        self.countries_dict[name].petroleumlist.append(self.countries_dict[name].mresources["petroleum"])
        self.countries_dict[name].uraniumlist.append(self.countries_dict[name].mresources["uranium"])
        self.countries_dict[name].waterlist.append(self.countries_dict[name].mresources["water"])
        self.countries_dict[name].ironlist.append(self.countries_dict[name].mresources["iron"])
        self.countries_dict[name].war_action()
        if len(list(self.countries_dict[name].population)) > 0:
            for i in self.countries_dict[name].workers:
                if i[2] in self.countries_dict[name].fresources:
                    price += (self.countries_dict[name].pay[i[2]] + random.randint(-5, 5)) / self.countries_dict[name].fresources[i[2]] + 1
                else:
                    price += (self.countries_dict[name].pay[i[2]] + random.randint(-5, 5)) / (self.countries_dict[name].mresources[i[2]]*2) + 1
            price /= len(self.countries_dict[name].everyone) + 1
            self.countries_dict[name].prices.append(price)
            self.countries_dict[name].bill += self.countries_dict[name].units/(abs(self.countries_dict[name].inflation)*random.randint(1, 10)/10 + 1)
            if len(self.countries_dict[name].population["m"]) > 0 and len(self.countries_dict[name].population["w"]) > 0 and random.randint(0, 5) == 5:
                self.countries_dict[name].dem()
            if self.countries_dict[name].war == True and random.randint(0, 10) == 5:
                self.countries_dict[name].fresources["weapon"] -= 50
                self.countries_dict[name].i.military -= random.randint(1, 100)/100
                self.countries_dict[name].death(random.randint(5, 10)/10)
            if self.countries_dict[name].bill >= len(self.countries_dict[name].everyone) * 3:
                self.countries_dict[name].inflation += 1
            if self.countries_dict[name].inflation > random.randint(25, 100):
                self.countries_dict[name].i.gdp -= self.countries_dict[name].inflation/100
                self.countries_dict[name].spend += self.countries_dict[name].inflation/100
                if random.randint(1, 10) == 1:
                    self.countries_dict[name].bill -= self.countries_dict[name].inflation * 10
            if self.countries_dict[name].i.gdp*10 < self.countries_dict[name].inflation or random.randint(1, 20) == 20:
                if random.randint(0, 4) % 2 == 0:
                    for key, value in self.countries_dict[name].fresources.items():
                        if value > 0:
                            c2 = list(self.countries_dict[name].relations.keys())[random.randint(0, len(list(self.countries_dict[name].relations.keys())) - 1)]
                            self.countries_dict[name].sell(key, value / 2, c2)
                            self.countries_dict[name].sold_to.update({c2: {key: value}})
                            self.countries_dict[name].st_list.append(c2)
                else:
                    for key, value in self.countries_dict[name].mresources.items():
                        if value > 0:
                            c2 = list(self.countries_dict[name].relations.keys())[random.randint(0, len(list(self.countries_dict[name].relations.keys())) - 1)]
                            self.countries_dict[name].sell(key, value / 2, c2)
                            self.countries_dict[name].sold_to.update({c2: {key: value}})
                            self.countries_dict[name].st_list.append(c2)
            for key, value in self.countries_dict[name].fresources.items():
                if value < len(self.countries_dict[name].everyone) / 5 and self.countries_dict[name].i.gdp > 3:
                    self.countries_dict[name].buy(key, random.randint(5, 20), list(self.countries_dict[name].relations.keys())[random.randint(0, len(list(self.countries_dict[name].relations.keys())) - 1)])
            if self.countries_dict[name].workplace < len(self.countries_dict[name].everyone):
                self.countries_dict[name].i.work -= self.countries_dict[name].workplace/len(self.countries_dict[name].everyone)
            if self.countries_dict[name].workplace >= len(self.countries_dict[name].everyone):
                self.countries_dict[name].i.work = 10
            if self.countries_dict[name].disease == True:
                self.countries_dict[name].bad[0].append(1)
            else:
                self.countries_dict[name].bad[0].append(0)
            if self.countries_dict[name].war == True:
                self.countries_dict[name].bad[1].append(2)
            else:
                self.countries_dict[name].bad[1].append(0)
            if self.countries_dict[name].famine == True:
                self.countries_dict[name].bad[2].append(3)
            else:
                self.countries_dict[name].bad[2].append(0)
            if self.countries_dict[name].is_revolution == True:
                self.countries_dict[name].bad[3].append(4)
            else:
                self.countries_dict[name].bad[3].append(0)
            self.countries_dict[name].is_revolution = False
            if temp > random.randint(50, 100):
                self.countries_dict[name].i.nation -= 0.1
                self.countries_dict[name].energy -= random.randint(1, 10)/40
                self.countries_dict[name].revolution += random.randint(1, 10)/10
            if len(self.countries_dict[name].sources) > 0:
                values = []
                for i in range(len(self.countries_dict[name].sources)):
                    values.append(self.countries_dict[name].sources[i][1])
                self.countries_dict[name].mine(self.countries_dict[name].sources.index(self.countries_dict[name].sources[values.index(max(values))]))
            payworkers = 0
            self.countries_dict[name].fresources["food"] -= len(self.countries_dict[name].everyone) * 3
            for e in self.countries_dict[name].workers:
                payworkers += e[2]
            if random.randint(1, 250) == 1:
                self.countries_dict[name].epidemic.append(list(self.countries_dict[name].diseases.keys())[random.randint(0, len(list(self.countries_dict[name].diseases.keys())) - 1)])
                self.countries_dict[name].disease = True
            for l in range(len(self.countries_dict[name].fabrics)):
                self.countries_dict[name].fresources[self.countries_dict[name].fabrics[l][1]] += self.countries_dict[name].fabrics[l][0]
                self.countries_dict[name].energy -= self.countries_dict[name].fabrics[l][0]/self.countries_dict[name].fabrics[l][2]
            if self.tips > 20 or self.countries_dict[name].i.equal < 4 or self.countries_dict[name].bill < payworkers or (self.countries_dict[name].aggression > self.countries_dict[name].i.nation * 3) or self.countries_dict[name].fresources["weapon"] >= self.countries_dict[name].fresources["food"] * 5:
                self.countries_dict[name].revolution += random.randint(1, 5)
                self.countries_dict[name].i.equal -= 0.05
                self.tips -= 5
                if self.countries_dict[name].science > self.countries_dict[name].aggression:
                    self.countries_dict[name].revolution += 1
                for key, value in self.countries_dict[name].fresources.items():
                    if value > 0 and self.countries_dict[name].i.gdp < 3:
                        c2 = list(self.countries_dict[name].relations.keys())[random.randint(0, len(list(self.countries_dict[name].relations.keys())) - 1)]
                        self.countries_dict[name].sell(key, value // random.randint(2, 5), c2)
                        self.countries_dict[name].sold_to.update({c2: {key: value}})
                        self.countries_dict[name].st_list.append(c2)
                for key, value in self.countries_dict[name].mresources.items():
                    if value > 0 and self.countries_dict[name].i.gdp < 3:
                        c2 = list(self.countries_dict[name].relations.keys())[random.randint(0, len(list(self.countries_dict[name].relations.keys())) - 1)]
                        self.countries_dict[name].sell(key, value // random.randint(2, 5), list(self.countries_dict[name].relations.keys())[random.randint(0, len(list(self.countries_dict[name].relations.keys())) - 1)])
                        self.countries_dict[name].sold_to.update({c2: {key: value}})
                        self.countries_dict[name].st_list.append(c2)
                self.countries_dict[name].i.nation -= 1
                self.countries_dict[name].units += len(self.countries_dict[name].everyone)
            if self.countries_dict[name].revolution > 50:
                self.countries_dict[name].propaganda()
            if self.countries_dict[name].i.gdp > 3:
                if random.randint(1, 10) == 5:
                    self.countries_dict[name].new_fabric(list(self.countries_dict[name].fresources.keys())[random.randint(0, len(list(self.countries_dict[name].fresources.keys())) - 1)])
            if self.countries_dict[name].science < 5 or random.randint(0, 100) > 97:
                self.countries_dict[name].new_school()
                self.countries_dict[name].new_university()
            if self.countries_dict[name].bill < len(self.countries_dict[name].everyone):
                self.countries_dict[name].units += len(self.countries_dict[name].everyone)/5
            if self.countries_dict[name].energy < 10:
                self.countries_dict[name].newgenerator()
                self.countries_dict[name].newgenerator()
            if self.countries_dict[name].science > 5 and random.randint(1, 10) == 10:
                self.countries_dict[name].explore()
            if self.countries_dict[name].i.nation < 0 or self.countries_dict[name].famine == True:
                self.countries_dict[name].revolution += 20
            for i in range(len(self.countries_dict[name].population["m"])):
                self.countries_dict[name].population["m"][i] += 1
            for j in range(len(self.countries_dict[name].population["w"])):
                self.countries_dict[name].population["w"][j] += 1
            if self.countries_dict[name].fresources["food"] < len(self.countries_dict[name].everyone)*0.5:
                self.countries_dict[name].famine = True
            if random.randint(0, 5) == 5:
                self.countries_dict[name].death(random.randint(7, 10))
            self.countries_dict[name].spend = 0
            if random.randint(1, 5) == 5:
                self.countries_dict[name].science += self.countries_dict[name].fresources["books"]
            if self.countries_dict[name].revolution >= 200 and len(self.countries_dict[name].everyone) > 0:
                self.countries_dict[name].is_revolution = True
                self.countries_dict[name].bad[3].append(4)
                i_num = random.randint(0, 2)
                self.countries_dict[name].i = self.countries_dict[name].i_dict[["Anarchism", "Communism", "Monarchism"][i_num]]
                self.countries_dict[name].inflation -= 50
                self.countries_dict[name].aggression = random.randint(0, 100)
                self.countries_dict[name].i.nation += 5
                for i in range(random.randint(0, len(self.countries_dict[name].everyone) - 1)):
                    self.countries_dict[name].death(random.randint(5, 10))
                self.countries_dict[name].i.military -= 5 
                self.countries_dict[name].i.gdp -= 2 
                self.countries_dict[name].i.equal += 2 
                self.countries_dict[name].revolution = 0
            if ((self.countries_dict[name].i.military > 10 or self.countries_dict[name].aggression > 20) and self.countries_dict[name].i.terror > 30) and self.countries_dict[name].war == False:
                for key, value in self.countries_dict[name].relations.items():
                    if (value > 2 or value < -2) and key not in self.countries_dict[name].warlist:
                        self.countries_dict[name].startwar(key)
                        break
            epidemic2 = self.countries_dict[name].epidemic.copy()
            for i in range(len(self.countries_dict[name].epidemic)):
                if self.countries_dict[name].science >= self.countries_dict[name].diseases[self.countries_dict[name].epidemic[i]]:
                    epidemic2.remove(self.countries_dict[name].epidemic[i])
            if len(epidemic2) == 0:
                self.countries_dict[name].disease = False
            self.countries_dict[name].epidemic = epidemic2
            if self.countries_dict[name].i.gdp < 0:
                a = random.randint(0, 4)
                if a == 4:
                    self.tips += random.randint(5, 10)
            if self.countries_dict[name].disease == True and random.randint(1, 5) == 5:
                if len(self.epidemic) > 0:
                    coeff = random.randint(7, 10)/self.diseases[self.epidemic[random.randint(0, len(self.epidemic) - 1)]]*10000
                    self.countries_dict[name].death(coeff)
            for j in range(len(self.countries_dict[name].workers)):
                self.countries_dict[name].bills -= self.tips * self.countries_dict[name].pay[self.countries_dict[name].workers[j][2]]
                self.countries_dict[name].i.gdp += self.countries_dict[name].pay[self.countries_dict[name].workers[j][2]]
            self.countries_dict[name].everyone = self.countries_dict[name].population["m"] + self.countries_dict[name].population["w"]
            self.countries_dict[name].i.gdp += self.countries_dict[name].spend + self.countries_dict[name].xn
            if len(self.countries_dict[name].prices) > 5:   
                if self.countries_dict[name].prices[-2] != 0:
                    self.countries_dict[name].inflation = (self.countries_dict[name].prices[-1] / self.countries_dict[name].prices[-2] - 1) * 100
    def start(self, output: bool, temp: int | float) -> None:
        """
        This method starts simulation, but without feelings of society (artfeel_E_00000002 module) and graph.
        
        Parameters
        ----------
        output: bool
            If you want to see the output, it`s True.
            Else, it`s False.
        """
        while len(list(self.countries_dict.keys())) > 1:
            startlen = len(list(self.countries_dict.keys()))
            for i in range(len(list(self.countries_dict.keys()))):
                self.year(list(self.countries_dict.keys())[i], temp)
                if len(list(self.countries_dict.keys())) < startlen:
                    break
                if output == True:
                    self.countries_dict[list(self.countries_dict.keys())[i]].output()
                l = input(self.countries_dict[list(self.countries_dict.keys())[i]].output)
                if "g" in l.split():
                    plt.subplot(3, 2, 1)
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].gdplist, "-b", label="GDP")
                    plt.legend()
                    plt.subplot(3, 2, 2)
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].inflationlist, "-m", label="Inflation")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].populationlist, "-g", label="Population")
                    plt.legend()
                    plt.subplot(3, 2, 3)
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].weaponlist, "-r", label="Weapon")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].foodlist, "-g", label="Food")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bookslist, "-y", label="Books")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].clocklist, "-k", label="Clock")
                    plt.legend()
                    plt.subplot(3, 2, 4)
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].petroleumlist, "-k", label="Petroleum")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].waterlist, "-b", label="Water")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].uraniumlist, "-y", label="Uranium")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].ironlist, "-c", label="Iron")
                    plt.legend()
                    plt.subplot(3, 2, 5)
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].populationlist, "-g", label="Population")
                    plt.legend()
                    plt.subplot(3, 2, 6)
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[0], "-y", label="Epidemic")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[1], "-m", label="War")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[2], "-c", label="Famine")
                    plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[3], "-b", label="Revolution")
                    plt.show()
    def start2(self, graph: bool, output: bool, temp: int | float) -> None:
        """
        This method starts simulation, but without feelings of society (artfeel_E_00000002 module).
        
        Parameters
        ----------
        graph: bool
            If you want to see the graph of countries economy, it`s True.
            Else, it`s False.
        
        output: bool
            If you want to see the output, it`s True.
            Else, it`s False.
        """
        while len(list(self.countries_dict.keys())) > 1:
            startlen = len(list(self.countries_dict.keys()))
            for i in range(len(list(self.countries_dict.keys()))):
                self.year(list(self.countries_dict.keys())[i], temp)
                if len(list(self.countries_dict.keys())) < startlen:
                    break
                if output == True:
                    self.countries_dict[list(self.countries_dict.keys())[i]].output()
                if len(self.countries_dict[list(self.countries_dict.keys())[i]].gdplist) % graph == 0:
                    if input(" ") == "g":
                        plt.subplot(3, 2, 1)
                        plt.title(list(self.countries_dict.keys())[i])
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].gdplist, "-b", label="GDP")
                        plt.legend()
                        plt.subplot(3, 2, 2)
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].inflationlist, "-m", label="Inflation")
                        plt.legend()
                        plt.subplot(3, 2, 3)
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].weaponlist, "-r", label="Weapon")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].foodlist, "-g", label="Food")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bookslist, "-y", label="Books")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].clocklist, "-k", label="Clock")
                        plt.legend()
                        plt.subplot(3, 2, 4)
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].petroleumlist, "-k", label="Petroleum")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].waterlist, "-b", label="Water")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].uraniumlist, "-y", label="Uranium")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].ironlist, "-c", label="Iron")
                        plt.legend()
                        plt.subplot(3, 2, 5)
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].populationlist, "-g", label="Population")
                        plt.legend()
                        plt.subplot(3, 2, 6)
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[0], "-y", label="Epidemic")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[1], "-m", label="War")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[2], "-c", label="Famine")
                        plt.plot(self.countries_dict[list(self.countries_dict.keys())[i]].bad[3], "-b", label="Revolution")
                        plt.legend()
                        plt.show()

def start(countries: list[str], ideologies: list[str]):
    """
    Creates countries and ideologies dictionary and countries.World() class.

    Parameters
    ----------
    countries: list[str]
        Names of the countries.

    ideologies: list[str]
        Names of the ideologies of countries.
    
    Returns
    -------
    co_so: dict
        Dictionary of country name as key and society (artfeel_E_00000002()) as value.

    w: countries.World()
        World() class returned by start() function.
    """
    w = World(countries, ideologies)
    co_so = {}
    for key in list(w.countries_dict.keys()):
        a = art.Act()
        a.new_society(len(w.countries_dict[key].population))
        co_so.update({key: a})
    return co_so, w

def game(w: World, co_so: dict, graph: int, graphTF: bool, end: int, years: int, temp: int | float):
    """
    This game is countries module simulation mixed with artfeel_E_00000002 module simulation.

    Parameters
    ----------
    w: countries.World()
        World() class returned by start() function.
    
    co_so: dict
        Dictionary of country name as key and society (artfeel_E_00000002()) as value.
    
    graph: int
        Every {graph} years the game will show graph of economy.
    
    graphTF: bool
        If True, the game will show you graph every {graph} years.
        Else, the game will not show you the graph.

    end: int
        When years will be equal to this value, this function will end.
    
    years: int
        Current value of game years.
    
    Returns
    -------
    years: int
        New value of game() years.
    """
    while (int(years)) % int(end) != 0 or int(years) < int(end):
        antisocial = []
        for key, value in co_so.items():
            love = 0
            hate = 0
            fear = 0
            joy = 0
            sad = 0
            tired = 0
            if key in list(w.countries_dict.keys()):
                for key2, value2 in value.everyone.items():
                    value2.years(False, 1)
                    if abs(value2.sub_good - value2.o_good) > value2.o_good and abs(value2.sub_bad - value2.o_bad) > value2.o_bad:
                        antisocial.append(key)
                    w.countries_dict[key].revolution -= len(antisocial)/len(w.countries_dict[key].population)
                    love += value2.love/len(list(value2.everyone.keys()))/10000
                    hate += value2.hate/len(list(value2.everyone.keys()))/10000
                    fear += value2.fear/len(list(value2.everyone.keys()))/10000
                    joy += value2.joy/len(list(value2.everyone.keys()))/10000
                    sad += value2.sad/len(list(value2.everyone.keys()))/10000
                    tired += value2.tired/len(list(value2.everyone.keys()))/10000
                    if random.randint(1, 10) == 10 and value2.tired < 1:
                        value.create(key2)
                    w.countries_dict[key].revolution += 1000/(abs((hate - love - fear/2)/len(w.countries_dict[key].population)) + 1)/10000
                    w.year(key, temp)
                    if key in list(w.countries_dict.keys()):
                        if len(list(value2.everyone.keys())) < len(w.countries_dict[key].population):
                            for i in range(len(w.countries_dict[key].population)):
                                value2.everyone.update({str(i + len(list(value2.everyone.keys()))): art.One(str(i), value.everyone)})
        years += 1
        if years % graph == 0 and graphTF == True:
            if input(" ") == "g":
                for i in range(len(list(w.countries_dict.keys()))):
                    plt.subplot(3, 2, 1)
                    plt.title(list(w.countries_dict.keys())[i])
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].gdplist, "-b", label="GDP")
                    plt.legend()
                    plt.subplot(3, 2, 2)
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].inflationlist, "-m", label="Inflation")
                    plt.legend()
                    plt.subplot(3, 2, 3)
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].weaponlist, "-r", label="Weapon")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].foodlist, "-g", label="Food")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].bookslist, "-y", label="Books")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].clocklist, "-k", label="Clock")
                    plt.legend()
                    plt.subplot(3, 2, 4)
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].petroleumlist, "-k", label="Petroleum")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].waterlist, "-b", label="Water")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].uraniumlist, "-y", label="Uranium")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].ironlist, "-c", label="Iron")
                    plt.legend()
                    plt.subplot(3, 2, 5)
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].populationlist, "-g", label="Population")
                    plt.legend()
                    plt.subplot(3, 2, 6)
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].bad[0], "-y", label="Epidemic")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].bad[1], "-m", label="War")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].bad[2], "-c", label="Famine")
                    plt.plot(w.countries_dict[list(w.countries_dict.keys())[i]].bad[3], "-b", label="Revolution")
                    plt.legend()
                    plt.show()
    return years