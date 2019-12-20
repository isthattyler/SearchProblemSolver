# Search Problem Solver

## Introduction

This project is done as the solution to an assignment I had in school.

It uses BFS, DFS, and A* searching algorithm to solve problems.

The algorithm is made as generic as possible to be used for many other different searching problems, not limited to these particular ones that I have.

I'm looking forward to port this over to **Java** as well in the future. Please watch for update.

## Details

### ADTs

Each searching algorithm uses an ADT that works well for the implementation. Specifically, BFS uses Queue, DFS uses Stack, and A* uses Priority Queue.

### Files

#### *main*.py

This is the main file of the program. Running it is as easy as this:

```bash
cd src/Python
python3 main.py
```

#### *searchAI*.py

**setProblem**: This function sets the problem to be used. It serves particular to my problem set only.

**trace**: trace back to search for the optimal solution.

**isFinalState**: implemented by the problem class.

**dfsSearch**: DFS algorithm to search for optimal solution.

**bfsSearch**: BFS algorithm to search for optimal solution.

**astarSearch**: A* algorithm to search for optimal solution.

**search**: Main driver for this program. All it does is setting the problem that needs to be solved, and choosing an algorithm to solve.

## Usage

To use this program, you will need to do some modification.

1. Create a new problem class that has the following methods:
    - isFinateState(): When the problem is considered solved.
    - generateStates(): How a state generates its children.
    - str(): how you want the class to be printed out.
    - gt() / lt() / ne(): how you want the class compares itself with another instance. Implementing gt() is recommended to be able to use A* search.
    - heuristic function: heuristic function is used in A* to find the optimal solution. It's not explicitly written out in my case, but it's within the gt() magic method.
2. Modify *searchAI*.py
    - Importing your new problem class.
    - Setting your problem in **search** method, and choose your desire search function.
    - Optional: Modifying str() if you want to have different representation.

## Issues

This solver definitely has some unforseen issues that I, at the moment, cannot find out. If you see some issues, please open it up so I can fix it, or fork it and make a pull request so that I can merge your new change in, if needed.

Thank you, and enjoy using this solver!
