class Puzzle(object):

    """Puzzle class for holding the 15-puzzle"""

    def __init__(self, initial_state):
        """Initialize the board

        Args:
            initial_state (tuple): Starting board position
        """

        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 9,
                           10, 11, 12, 13, 14, 15, 0)
        self.solvable = self.solvable(initial_state)

    def solvable(self, state):
        """Check if the board is solvable

        Args:
            state (tuple): state to check

        Returns:
            bool: Whether the state is solvable
        """

        row_number = state.index(0)/4 + 1

        inversions = 0
        for i in range(16):
            for j in range(i+1, 16):
                if state[i] == 0 or state[j]==0:
                    continue
                if state[i] > state[j]:
                    inversions += 1

        return (inversions + row_number) % 2 == 0

    def heuristic(self, state):
        """Using Hamming distance as heuristic.

        Args:
            state (tuple): state to check

        Returns:
            int: number of positions state differs from goal state
        """

        goal = self.goal_state
        error = 0
        for i in range(16):
            if state[i] != goal[i]:
                error += 1
        return error

    def sucessors(self, state):
        """Summary

        Args:
            state (tuple): state to retrieve sucessors

        Returns:
            List of tuples: List of sucessor states
        """
        state = list(state)
        i = state.index(0)
        if i == 0:
            neighbors = [1, 4]
        elif i == 1:
            neighbors = [0, 2, 5]
        elif i == 2:
            neighbors = [1, 3, 6]
        elif i == 3:
            neighbors = [2, 7]
        elif i == 4:
            neighbors = [0, 5, 8]
        elif i == 5:
            neighbors = [1, 4, 6, 9]
        elif i == 6:
            neighbors = [2, 5, 7, 10]
        elif i == 7:
            neighbors = [3, 6, 11]
        elif i == 8:
            neighbors = [4, 9, 12]
        elif i == 9:
            neighbors = [5, 8, 10, 13]
        elif i == 10:
            neighbors = [6, 9, 11, 14]
        elif i == 11:
            neighbors = [7, 10, 15]
        elif i == 12:
            neighbors = [8, 13]
        elif i == 13:
            neighbors = [9, 12, 14]
        elif i == 14:
            neighbors = [10, 13, 15]
        elif i == 15:
            neighbors = [11, 14]

        sucessors = []
        for j in neighbors:
            state[i], state[j] = state[j], state[i]
            sucessors.append(tuple(state))
            state[i], state[j] = state[j], state[i]
        return sucessors

    def print_board(self, state):
        board = "%2d %2d %2d %2d \n%2d %2d %2d %2d \n%2d %2d %2d %2d \n%2d %2d %2d %2d\n\n" % state
        board = board.replace("10", "*").replace("0", "_").replace("*","10")
        print board

    def print_solution(self, list_of_states):
        for state in list_of_states:
            self.print_board(state)


