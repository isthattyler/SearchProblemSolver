class State2:
    def __init__(self, m, n, i, goal, jug1=0, jug2=0, tub=0, children=[]):
        # Rule: goal <= i
        self.m = m
        self.n = n
        self.i = i
        self.goal = goal
        self.jug1 = jug1 # m
        self.jug2 = jug2 # n
        self.tub = tub # i
        self.children = children

    def isFinalState(self):
        if (self.jug1==self.jug2==0) and (self.tub==self.goal):
            return 1
        return 0

    def generateStates(self):
        if self.jug1==self.jug2==0: # initial state
            if self.n > self.m:# fill the larger jug
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1, self.jug2+self.n,self.tub,[]))
            else:
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1+self.m, self.jug2,self.tub,[]))
        # empty first jug if has water
        if self.jug1 > 0:
            # empty first jug to second jug
            if self.jug1+self.jug2<= self.n:
                self.children.append(State2(self.m, self.n, self.i, self.goal, 0, self.jug1+self.jug2,self.tub,[]))
            else: # can only fill partially
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1-(self.n-self.jug2), self.n,self.tub,[]))
            # empty first jug to the tub
            if self.jug1+self.tub<=self.goal:
                self.children.append(State2(self.m, self.n, self.i, self.goal, 0, self.jug2, self.jug1+self.tub,[])) # fill the tub
            else: # fill partially to reach goal
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1-(self.goal-self.tub), self.jug2,self.goal,[]))
            # dump all water to ground
            self.children.append(State2(self.m, self.n, self.i, self.goal, 0, self.jug2,self.tub,[]))
        if self.jug2 > 0:
            # empty second jug to first jug
            if self.jug1+self.jug2<= self.m:
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1+self.jug2, 0,self.tub,[]))
            else: # can only fill partially
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.m, self.jug2-(self.m-self.jug1), self.tub,[]))
            # empty second jug to the tub
            if self.jug2+self.tub<=self.goal:
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1, 0, self.jug2+self.tub,[])) # fill the tub
            else: # fill partially to reach goal
                self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1, self.jug2-(self.goal-self.tub), self.goal,[]))
            #dump all water to ground
            self.children.append(State2(self.m, self.n, self.i, self.goal, self.jug1, 0, self.tub,[]))
        return self.children

    def __str__(self):
        string = "\n(Jug 1: " + str(self.jug1) + "\tJug 2: " + str(self.jug2) + "\tTub: " + str(self.tub) + ")"
        return string

    def __eq__(self, other):
        return (self.jug1, self.jug2, self.tub)==(other.jug1, other.jug2, other.tub)

    def __ne__(self, other):
        return not (self==other)

    def __hash__(self):
        return hash(str(self.jug1) + str(self.jug2) + str(self.tub))

    def __gt__(self, other):
        return self.tub > other.tub