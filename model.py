import sisyphus as m

c = m.City()


# you can replace this books with your downloaded books (.txt files) if you want
books1 = ["Book1", "Book2"]
books2 = ["Book3", "Book4"] 
books3 = ["Book5", "Book6"]
books4 = ["Book7", "Book8"]

c.new_Person("Existence1", ["E_1", "E_2"], [books1, books2], [1, 1, 1, 1, -1, 1])
c.new_Person("Existence2", ["E_3", "E_4"], [books3, books4], [1, -1, -1, 1, -1, 1])
c.person_learn_quest("Existence1")
c.person_learn_quest("Existence2")
c.update()
c.threads_chat(["Existence1", "Existence2"], 10)
