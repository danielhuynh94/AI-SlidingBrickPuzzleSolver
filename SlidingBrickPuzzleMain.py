import SlidingBrickPuzzle


def main():
    # Main function

    # Init a puzzle state
    puzzleState = SlidingBrickPuzzle.State()

    # Load a state from file
    puzzleState.loadFromFile("SBP-level0.txt")
    # Perform 3 random walks
    SlidingBrickPuzzle.randomWalk(3, puzzleState)

    # Load a state from file
    puzzleState.loadFromFile("SBP-level1.txt")
    SlidingBrickPuzzle.solveUsingBreadthFirstSearch(puzzleState)
    SlidingBrickPuzzle.solveUsingDepthFirstSearch(puzzleState)
    SlidingBrickPuzzle.solveUsingIterativeDeepeningSearch(puzzleState)
    # SlidingBrickPuzzle.solveUsingAStarSearch(puzzleState)

# Run the main function
main()
