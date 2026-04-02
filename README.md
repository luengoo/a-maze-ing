*This project has been created as part of the 42 curriculum by alluengo, zalabib-*

# A-Maze-ing

## Description
A-Maze-ing is a project written in Python 3.12. It is configurable via a .txt file. The main goal is to create a fully random maze, save it in a hexadecimal format, and display it visually with a few interactive options. The program also includes a solver function that searches for the shortest path and saves it in the same output file.

## Instructions

### Compilation & Installation
To install the necessary dependencies and prepare the environment, run the following command at the root of the repository:

make install

### Execution

make run

Other Make rules:

make debug  -> run the main script in debug mode using Python's built-in debugger (pdb)
make clean  -> remove cache and temporary files/directories
make lint   -> run strict flake8 checks

## Configuration file

The config.txt file MUST exist to run this program. It follows a strict KEY=VALUE format.

### Format
KEY=VALUE

### Example
WIDTH=15
HEIGHT=15
ENTRY=0,0
EXIT=14,14
OUTPUT_FILE=maze.txt
PERFECT=True

### Description of parameters
ENTRY: Starting point of the maze  
EXIT: Goal position  
OUTPUT_FILE: File where the maze is stored in hexadecimal format, along with the shortest path using N (North), S (South), E (East), W (West)  
PERFECT: If True, generates a perfect maze (only one path between entry and exit). If False, additional walls are removed to create multiple possible paths  

## Maze Generation Algorithm

### Chosen algorithm

- Generation: We implemented Prim's random maze algorithm. This algorithm starts from a random node and progressively expands across the grid by connecting adjacent nodes. It maintains two sets of vertices: one already included in the Minimum Spanning Tree (MST), and another with remaining vertices. At each step, it selects the minimum-weight edge connecting both sets and adds the corresponding node to the MST.

Advantages:
- Guaranteed to produce a valid spanning tree in a connected weighted graph  
- Time complexity of O((E + V) * log(V)) using efficient data structures  
- Relatively simple to implement  
- Produces visually appealing mazes with organic expansion  

Disadvantages:
- Can be slower on dense graphs  
- Requires additional memory for the priority queue  

- Solver: Initially, we considered using recursive backtracking. However, this approach does not guarantee the shortest path in non-perfect mazes, as it stops at the first valid solution found. To solve this, we implemented a Breadth-First Search (BFS) algorithm. BFS uses a queue to explore all possible paths level by level, ensuring that the first time the exit is reached corresponds to the shortest path. This solution works reliably for both perfect and non-perfect mazes.

## Reusability

The project is designed with modularity in mind. Core components such as the Maze and Cell classes are independent from execution scripts. This allows easy reuse of the maze generation and solving logic in other Python projects by importing the relevant modules:

## Reusable Module

The maze generation logic is implemented as a standalone module that can be reused in other Python projects. It is designed around a main class (e.g., MazeGenerator) that encapsulates all generation logic.

### Basic usage
```python
from mazegen import MazeGenerator
```
# Create a generator with custom parameters

maze = MazeGenerator(width=15, height=15, seed=42)

# Generate the maze
maze.generate()

The generate() method builds the maze and initializes its internal attributes, such as the grid representation and the solution path.
# Access the maze structure
grid = maze.grid

# Get the shortest path (solution)
solution = maze.path

## What worked well

- Clear modular structure (Maze, Cell, solver separation)  
- Good communication and collaboration between team members  
- Effective use of Git branches when needed  

## What could be improved

- Better handling of edge cases such as terminal resizing during execution  
- More advanced use of version control tools (branching strategy, commit structure)

## Team and Project Management

Parsing and maze generation: alluengo  
Menu, solver, and optimizations: zalabib-  
maze_algorithm: alluengo (Prim's algorithm implementation)    
Makefile: zalabib-
Packaging: zalabib- 
README: alluengo, zalabib- 

### Planning and evolution

Initially, we planned to implement a recursive backtracking solver. During development, we realized that it did not guarantee the shortest path in non-perfect mazes. As a result, we switched to a BFS-based solver.

We also improved the project structure early on by separating configuration parsing, maze generation, and solving into independent modules. This made collaboration easier and reduced integration issues.

Our workflow with Git also evolved, as we progressively made better use of branches and coordination between team members.

### Tools used

- Git & GitHub for version control and collaboration  
- Make for automation  
- Flake8 for linting and code quality  
- VS Code as the development environment  

## Resources
- Artificial Intelligence was used in this project for documentation purposes (explaining algorithms and concepts) and to assist with debugging in specific cases.

### References

main ressources:
- https://www.geeksforgeeks.org/dsa/prims-minimum-spanning-tree-mst-greedy-algo-5/  
- https://es.wikipedia.org/wiki/Algoritmo_de_Prim  
- https://www.jamisbuck.org/mazes/
- https://www.youtube.com/watch?v=4wgRlNqIKqM