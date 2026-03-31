*This project has been created as part of the 42 curriculum by alluengo, zalabib-*

# A-Maze-ing

## Description
A-Maze-ing is a project written in Python 3.12. It is configurable via .txt file. The main goal is to create a full random maze, save it in a hexadecimal format and display it visually with a few interactive options. The program also includes a backtracking-solver function that searches for the shortest path and saves it in the same output file.

## Instructions

### Compilation & Installation
To install the necessary dependencies and prepare the enviroment, run the following command at the root of the repository:
```

make install
```

### Execution
```
make run
```

Other Make rules:
```
make debug -->> run the main script in debug mode using Python's built-in debugger pdb.
make clean -->> removes cache and trash files/directories
make lint -->> strict flake8 standards
```

## Configuration file
The config.txt file MUST exist to run this program. It works via KEY=VALUE, no other formats allowed:
*WIDTH=15*
*HEIGHT=15*
*ENTRY=0,0*
*EXIT=14,14*
*OUTPUT_FILE=maze.txt*
*PERFECT=True*

ENTRY: Starting point of the maze
EXIT: Goal
OUTPUT_FILE: Here is where we store the maze in hexadecimal value, and the shortest path in N(North), S(South), E(East), W(West), each step being a cardinal point.
PERFECT: Our maze algorithm (later explained) makes a perfect maze by default, being perfect a single path between two points of the maze (in this case, between entry and exit). If perfect is True, run the normal algorithm. Otherwise, remove some random walls.

## Maze Generation Algorithm

### Chosen algorithm
- **Generation**: We chose to implement the **Prim's random maze algorithm**. This algorithm always starts with a single and random node in the grid and moves through several adjacent nodes, in order to explore all of the connected edges along the way. The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST (Minimum Spanning Tree), and the other set contains the vertices yet not included. At every step, it considers all the edges that connect the two sets and picks the MINIMUM WEIGHT edge from these. After picking the edge, it moves the other endpoint of the edge to the set containing MST.

    **Advantages**: Prim's algorithm is guaranteed to find the MST in a connected, wighted graph. Its time complexity is O((E+V)*log(V)) using a binary heap or Fibonacci heap, where E is the number of edges and V the number of vertices. It is relatively simple to understand and implement compared to some other MST allgorithms. The real reason we chose it was because of the beauty of its generation, as it expands as a virus.

    **Disadvantages**: It can be slow on dense graphs with many edges, as it requires iterating over all edges at least once. It relies on a priority queue, which can take up extra memory and slow down the algorithm in very large graphs.
- **Solver**:

## Reusability
The entire project is built with modularity in mind. All core logic (such as the Maze and Cell classes) is decoupled from the specific execution scripts. You can easily reuse the maze generation and solving logic in any other Python project by simply importing the modules:

```
from maze_algorithm import Cell
...
```

## Team and Project management

'a_maze_ing': zalabib- with the implementation of the menu and the main program.
'config_checker': alluengo, being the first thing made of the project. Parsing the config file.
'maze_algorithm': alluengo, with the Prim's algorithm.
'solver': zalabib- with the creation of the solver.
'Makefile': zalabib- with the whole Makefile creation.
'README': alluengo, writing everything he thought inside this file.

At first, we took a look and talked about the main project structure, making a CHECKLIST file and realising the git branches work flow was going to be one of the big parts of this project. Then, we both worked on everything and with good communication and undestanding we made the project work.

Each of us had our parts to work in, but we both worked on everything, as the main idea was being made by one, and the development by both.

## Resources

### References

- https://www.geeksforgeeks.org/dsa/prims-minimum-spanning-tree-mst-greedy-algo-5/
- https://es.wikipedia.org/wiki/Algoritmo_de_Prim
- https://www.jamisbuck.org/mazes/

### AI Usage
Artificcial Intelligence was used in this project specifically for documentation purposes.