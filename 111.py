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
                    print(j)







a = LabirintTurtle()
a.load_map('12')
a.show_map()
