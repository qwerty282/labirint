class LabirintTurtle:
    def load_map(self, name):
        self.f = open(name + '.txt')
        self.txt = []
        for i in self.f:
            z = []
            z.append(i)
            self.txt.append(z)

    def show_map(self, turtle = False):
        if turtle == True:
            for i in self.txt:
                for j in i:
                    print(j)
        else:
            for i in self.txt:
                for j in i:
                    if "A" in j:
                         j = j.replace('A',' ') 
                            






