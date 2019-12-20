from problem1 import *
from problem2 import *
from problem3 import *
from bfsQueue import *
from dfsStack import *
from aPrioQueue import *


class Search:
    def __init__(self):
        self.problem = None

    def setProblem(self, problem):
        self.problem=problem
        self.visited=None

    def trace(self, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    def isFinalState(self, state):
        return state.isFinalState()

    def dfsSearch(self):
        startState=self.problem
        visited=[]
        path={}
        stack = Stack()
        currState=startState
        visited.append(currState)
        while not self.isFinalState(currState):
            children=currState.generateStates()
            for child in children:
                if child not in visited:
                    stack.push(child)
                    visited.append(child)
                    path[child]=currState
            currState=stack.pop()
        sol = self.trace(path, startState, currState)
        self.visited=visited
        return sol

    def dfsSearch3(self): # special dfs for problem 3
        startState=self.problem
        visited=[]
        path={}
        stack = Stack()
        currState=startState
        visited.append(currState)
        accepted=[]
        flag=1
        while flag: # search all the levels
            children=currState.generateStates()
            for child in children:
                if child not in visited:
                    stack.push(child)
                    visited.append(child)
                    path[child]=currState
                if self.isFinalState(child): # add all instance of final state
                    accepted.append(child)
            if stack.size() == 0: # if there's nothing else in stack, signal to stop
                flag= not(flag)
            currState=stack.pop()
        distance=accepted[0].getDistance()
        for i in accepted:
            temp=i.getDistance()
            if temp <= distance:
                distance=temp
                currState=i
        sol = self.trace(path, startState, currState)
        sol=[sol[-1]]
        self.visited=visited
        return sol

    def bfsSearch(self):
        startState=self.problem
        visited=[]
        path={}
        queue=Queue()
        currState=startState
        visited.append(currState)
        accepted=[]
        while not self.isFinalState(currState):
            children=currState.generateStates()
            for child in children:
                if child not in visited:
                    queue.enqueue(child)
                    visited.append(child)
                    path[child]=currState
                if self.isFinalState(child): # add all instance of final state
                    accepted.append(child)
            currState=queue.dequeue()
        sol = self.trace(path, startState, currState)
        if isinstance(self.problem, State3): # in case of problem 3
            distance=accepted[0].getDistance()
            for i in accepted:
                temp=i.getDistance()
                if temp <= distance:
                    distance=temp
                    currState=i
            sol = self.trace(path, startState, currState)
            sol=[sol[-1]]
        self.visited=visited
        return sol

    def astarSearch(self):
        startState=self.problem
        visited=[]
        path={}
        queue=PriorityQueue()
        queue.enqueue(startState)
        currState=queue.dequeue()
        visited.append(currState)
        while not self.isFinalState(currState):
            children=currState.generateStates()
            for child in children:
                if child not in visited:
                    queue.enqueue(child)
                    visited.append(child)
                    path[child]=currState
            currState=queue.dequeue()
        sol = self.trace(path, startState, currState)
        if isinstance(self.problem, State3):
            sol=[sol[-1]]
        self.visited=visited
        return sol

    def search(self):
        a = int(input("Select problem you want to test(1, 2, 3): "))
        if a==1:
            self.setProblem(State1())
        elif a==2:
            m=int(input("What's the max volumn for jug1? "))
            n=int(input("What's the max volumn for jug2? "))
            i=int(input("What's the max volumn for tub? "))
            goal=int(input("What's the goal volumn for tub? "))
            while goal > i:
                goal=int(input("Goal is larger than max volumn of tub. Please enter different value: "))
            self.setProblem(State2(m,n,i,goal))
        else:
            start=input("What's your start state? ")
            final=input("What's your final state? ")
            self.setProblem(State3(start.upper(), final.upper()))
        a = int(input("Enter 1 for BFS search, 2 for DFS search, 3 for A* search: "))
        if a==1:
            self.problem=self.bfsSearch()
        elif a==2:
            if isinstance(self.problem, State3):
                self.problem=self.dfsSearch3()
            else:
                self.problem=self.dfsSearch()
        else:
            self.problem=self.astarSearch()

    def __str__(self):
        string = "\nPath:\n------------\n"
        for item in self.problem:
            string += item.__str__() + "\n"
        string+="\nVisited path:\n------------\n"
        for state in self.visited:
            string+= state.__str__() + "\n"
        string+="\nTotal states visited:\n------------\n"
        string+=str(len(self.visited))
        return string