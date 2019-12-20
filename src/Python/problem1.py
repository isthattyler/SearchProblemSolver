class State1:
    def __init__(self, start=['cat', 'duck', 'grain'], end=[], farmer=0, children=[]):
        self.start = start
        self.end = end
        self.farmer = farmer # check point to see if farmer is on left=0, or right=1
        self.children = children
        self.invalid = [['cat', 'duck', 'grain'], ['cat', 'duck'], ['duck', 'grain']]

    def isFinalState(self):
        if len(self.start)==0 and self.farmer:
            return 1
        return 0

    def isViolated(self):
        if self.start in self.invalid and self.end in self.invalid:
            return 1
        return 0
    
    def generateStates(self):
        if not self.farmer: # from start
            for item in self.start:
                start = self.start[:]
                end = self.end[:]
                start.remove(item)
                end.append(item)
                if end not in self.invalid and start not in self.invalid: ## if both start and end have valid characters
                    self.children.append(State1(sorted(start), sorted(end), 1, []))
            farmer = State1(sorted(self.start[:]), sorted(self.end[:]), 1, [])
            if farmer.start not in self.invalid:
                self.children.append(farmer)
        else:
            for item in self.end:
                start = self.start[:]
                end = self.end[:]
                end.remove(item)
                start.append(item)
                if end not in self.invalid and start not in self.invalid: ## if both start and end have valid characters
                    self.children.append(State1(sorted(start), sorted(end), 0, []))
            farmer = State1(sorted(self.start[:]), sorted(self.end[:]), 0, [])
            if farmer.start not in self.invalid:
                self.children.append(farmer)

        return self.children

    def __str__(self):
        if self.farmer:
            string = "\nStarting: "
            for i in self.start:
                string += i + " "
            string += "\nEnding: farmer "
            for i in self.end:
                string += i + " "
        else:
            string = "\nStarting: farmer "
            for i in self.start:
                string += i + " "
            string += "\nEnding: "
            for i in self.end:
                string += i + " "
        return string

    def __eq__(self, other):
        return (self.start, self.end, self.farmer)==(other.start, other.end, other.farmer)

    def __ne__(self, other):
        return not (self==other)

    def __hash__(self):
        return hash(str(self.start) + str(self.end) + str(self.farmer))

    def __lt__(self, other):
        return len(other.end) < len(self.end)

    def __gt__(self, other):
        return len(self.end) > len(other.end)