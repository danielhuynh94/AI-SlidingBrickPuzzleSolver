SlidingBrickPuzzle

    SlidingBrickPuzzle is a library for representing Sliding Brick Puzzle game in Python. 
    The user can load a game state from a text file and apply different moves on the game state. 
    Moreover, the user can apply different search algorithms such as Breadth First Search, Depth First Search, Iterative Deepening Search to solve the game state. 
    You can play the game here: https://www.mathplayground.com/slidingblock.html

    Author: Huy "Daniel" Huynh

I. Installation
    1. Requirements
        * Linux
        * Python 3.3 and up

    2. Import Library In Python Files
        ```python
        import SlidingBrickPuzzle
        ```

    3. Files
        * SlidingBrickPuzzle.py - main library
        * SlidingBrickPuzzleMain.py - main function using the library to solve game states in files SBP-level0.txt and SBP-level1.txt
        * output-hw1.txt - text output of running SlidingBrickPuzzleMain.py
        * SBP-level0.txt - sample game state level 0
        * SBP-level0.txt - sample game state level 1
        * hw1.sh - content: 'python3 SlidingBrickPuzzleMain.py'

    4. Command line examples
        ```python
        python3 SlidingBrickPuzzleMain.py
        ```

        ```python
        python3 SlidingBrickPuzzleMain.py > output-hw1.txt
        ```

II. Usage
    1. Run The Default Main Function Containing Examples
        `$ ./hw1.sh`

    2. Load A State From A File
        ```python
        import SlidingBrickPuzzle
        # Init a puzzle state
        puzzleState = State()
        # Load a state from file
        puzzleState.loadFromFile("SBP-level0.txt")
        ```

    3. Perform Random Walk And Print Out Results
        ```python
        import SlidingBrickPuzzle
        # Init a puzzle state
        puzzleState = State()
        # Load a state from file
        puzzleState.loadFromFile("SBP-level0.txt")
        ```

    4. Perform Breadth First Search And Print Out Results
        ```python
        import SlidingBrickPuzzle
        # Init a puzzle state
        puzzleState = State()
        # Load a state from file
        puzzleState.loadFromFile("SBP-level0.txt")
        #Solve the puzzle using BFS and print the solution
        solveUsingBreadthFirstSearch(puzzleState)
        ```

    5. Perform Depth First Search And Print Out Results
        ```python
        import SlidingBrickPuzzle
        # Init a puzzle state
        puzzleState = State()
        # Load a state from file
        puzzleState.loadFromFile("SBP-level0.txt")
        #Solve the puzzle using DFS and print the solution
        solveUsingDepthFirstSearch(puzzleState)
        ```

    6. Perform Iterative Deepening Search And Print Out Results
        ```python
        import SlidingBrickPuzzle
        # Init a puzzle state
        puzzleState = State()
        # Load a state from file
        puzzleState.loadFromFile("SBP-level0.txt")
        #Solve the puzzle using IDS and print the solution
        solveUsingIterativeDeepeningSearch(puzzleState)
        ```

III. Documentation
    # Enumeration for the default values of certain bricks in the state
    enumeration BrickNumber
        goal = -1
        empty = 0
        wall = 1
        master_brick = 2

    # Enumeration for the default values of certain bricks in the state
    enumeration MoveDirection
        up = 1
        right = 2
        down = 3
        left = 4

    # Define a brick in the game
    class Brick(State state, int brickNumber):
        # Property for the reference of the game state
        state

        # Property for the brick number
        number

        # Return all possible moves of the brick
        function getAllPossibleMoves() 
            returns [Move]

        # Check whether the brick can move in certain direction
        function canMoveToDirection(int moveDirection) 
            returns boolean

    # Define a cell location in the state matrix
    class CellLocation(int rowIndex, int colIndex)
        # Property for the row index of the cell
        row

        # Property for the column index of the cell
        col

    # Define a move
    class Move(int brickNumber, int moveDirection)
        # Property for the brick number
        brickNumber

        # Property for the numeric value of the direction
        moveDirection

        # Return the string describing the move
        function getString()
            return string

    # Define a puzzle state
    class State([] matrix, State parentState, Move fromMove, int level, boolean isNormalized)
        # Property for the state matrix
        matrix

        # Property for the reference to the parent state
        parentState

        # Property for the current depth of the state
        level

        # Property for the reference to the move resulting in this state
        fromMove

        # Property for whether the state has been normalized
        isNormalized

        # Load a game state from the specified file
        function loadFromFile(fileName)

        # Normalize a puzzle state
        function normalize()

        # Swap the brick numbers of two bricks
        function swapIdx(int birckNumber1, int brickNumber2)

        # Clone a game state
        function clone():
            return State

        # Check whether the game state is solved
        function isSolved()
            return boolean

        # Print the game state
        function print()

        # Get all the possible moves of the state
        function getAllPossibleMoves()
            return [Move]

        # Get all the possible child states of this state
        function getAllPossibleNextStates()
            return [State]

        # Apply the specified move to this state
        function applyMove(Move move)

        # Apply the specified move to this state and return a clone
        function applyMoveCloning(Move move)
            return State

        # Check whether this state equals to the specified state
        function equals(State state)
            return boolean

    # Define check whether the specified value is a numeric value
    function isNumeric(string value)
        return boolean

    # Perform random walk on a game state, and print the results
    function randomWalk(int maxTurns, State puzzleState)

    # Solve a puzzle state using breadth first search, and print the results
    function solveUsingBreadthFirstSearch(State puzzleState)

    # Solve the game state using depth first search
    function solveUsingDepthFirstSearch(State puzzleState)

    # Solve the puzzle using depth limit search
    function solveUsingIterativeDeepeningSearch(State puzzleState)

    # Find a solved state of the puzzle within the specified depth limit
    function findSolutionUsingDepthLimitSearch(State puzzleState, int depthLimit)
        return State solvedState, [State] checkedStates

    # Check whether a state is in a list of state
    function checkStateInList(State state, [State] stateList, boolean skipLowerLevelItem)
        return boolean

    # A list of solution moves
    function printSearchSolution(State solvedState, int totalVisitedNodes, float solvingTime)

IV. License
    [MIT](https://choosealicense.com/licenses/mit/) © Huy "Daniel" Huynh