import sisyphus as m

c = m.City()


# you can replace this books with your downloaded books (.txt files) if you want
books1 = ["Book1", "Book2"]
books2 = ["Book3", "Book4"] 

c.new_Person("Existence2", ["E_00000001", "E_00000002"], [books1, books2], "w", 6, 
             [1, 1, 1, 1, -1, 1], False, 5)
c.new_Person("Existence1", ["E_00000001", "E_00000002"], [books1, books2], "w", 6, 
             [1, 1, 1, 1, -1, 1], False, 5)
c.update()
c.threads_chat(["Existence1", "Existence2"], 10)