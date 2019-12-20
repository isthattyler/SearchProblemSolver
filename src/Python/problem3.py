class State3:
    
    def __init__(self, start, end, path=[], distance=0, children=[]):
        self.start = start
        self.end = end
        self.children = children
        self.path=path
        self.distance=distance
        self.states = {'N':(0.2, 1), 'P':(1.35, 4.25), 'U':(2.15, 0.875), 'E':(3.42, 2.125), 'J':(3.8, 4.575), 'M':(6.7, 3.875), 'S':(6.7, 1.875), 'V':(5.6, 0.1)}
        self.edges={'N':['P','U'], 'P':['N','U','E','J'], 'U':['N','P','E'], 'E':['P','U','J','V'], 'J':['P','E','M'], 'M':['J','S','V'], 'S':['M'], 'V':['E','M']}

    def straightDistance(self, start, end):
        import math
        x1, y1 = self.states[start]
        x2, y2 = self.states[end]
        x3 = (x2-x1)**2
        y3 = (y2-y1)**2
        answer = round((x3+y3)**(1/2), 1)
        temp = math.ceil(answer)
        if answer <= temp-0.5:
            answer=temp-0.5
        elif temp - answer <= 0.1:
            answer=temp
        return answer

    def isFinalState(self):
        if self.start==self.end:
            return 1
        return 0

    def generateStates(self):
        if self.start not in self.path:
            self.path.append(self.start)
        for edge in self.edges[self.start]:
            if edge not in self.path: # make sure that there's no cyclic path, or repeated edge
                distance=self.straightDistance(self.start,edge)
                temp=self.path[:]
                temp.append(edge)
                self.children.append(State3(edge, self.end, temp, self.distance+distance,[]))
        return self.children

    def __str__(self):
        temp = [self.path, self.distance]
        string=str(temp)
        return string

    def __gt__(self, other):
        return other.distance > self.distance

    def getDistance(self):
        return self.distance