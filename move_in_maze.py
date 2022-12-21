from pathlib import Path
from blessed import Terminal

import time
import os

class MoveInMaze:
    def __init__(self, maze: list, path: Path, maze_to_solve: int, name: str, steps: int, choice: int):
        self.maze = maze
        self.steps = steps
        self.name = name
        self.choice = choice
        self.maze_to_solve = maze_to_solve
        self.path = path
        self.terminal = Terminal()
        self.start_positions = None

    def get_start_positions(self):
        start_positions: list = []
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == "^":
                    start_positions.append((row, col))

        self.start_positions = start_positions

    def find_next(self, coordinates):
        next_coordinates = []
        if coordinates[0] - 1 >= 0 and self.maze[coordinates[0] - 1][coordinates[1]] != "1":
            next_coordinates.append((coordinates[0] - 1, coordinates[1]))
        if coordinates[0] + 1 < len(self.maze) and self.maze[coordinates[0] + 1][coordinates[1]] != "1":
            next_coordinates.append((coordinates[0] + 1, coordinates[1]))
        if coordinates[1] + 1 < len(self.maze[0]) and self.maze[coordinates[0]][coordinates[1] + 1] != "1":
            next_coordinates.append((coordinates[0], coordinates[1] + 1))
        if coordinates[1] - 1 >= 0 and self.maze[coordinates[0]][coordinates[1] - 1] != "1":
            next_coordinates.append((coordinates[0], coordinates[1] - 1))
        return next_coordinates

    def write_solution(self, coordinates: tuple, used_steps: int, exit_found: bool):
        """
        Write the solution to a file
        :param exit_found: Boolean
        :param coordinates: Tuple with the finale coordinates
        :param used_steps: Number of steps used to reach the goal
        :return: None
        """

        write_file_path = self.path / f"solved/{self.name}_maze-{self.choice}_solution.txt"
        y, x = coordinates

        if exit_found:
            final = f"\nExit found at coordinates: [x:{x} y:{y}], used {used_steps} steps of " \
                    f"{self.steps}\n"
        else:
            final = f"\nExit not found, used {used_steps} steps of {self.steps} and " \
                    f"final position was [x:{x} y:{y}]\n"

        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_maze()
        print(final)
        with open(write_file_path, "w") as file:
            file.write(final)
            file.write(f"{'-' * 50}\n")
            for row in self.maze:
                file.write("".join(row).replace("0", " ").replace("1", "#") + "\n")

    def print_info(self, current: tuple, used_steps: int):
        print(f"{'-' * 50}\nVisiting:", current)
        print("Steps used:", used_steps, "\nSteps left:", self.steps - used_steps, "\n")
        self.print_maze()

    def solve_maze(self):
        self.get_start_positions()
        print(self.start_positions, self.maze_to_solve)
        if not self.start_positions:
            return False

        stack = []
        visited = set()
        curr_pos = self.start_positions[0]  # choose the first start position as the current position

        for start in self.start_positions:
            stack.append(start)
        used_steps = 0
        print(f"Available steps: {self.steps}")

        while stack:
            curr = stack.pop()

            if curr in visited:
                continue

            visited.add(curr)

            if self.maze[curr[0]][curr[1]] == "E":
                self.maze[curr[0]][curr[1]] = "^"
                self.write_solution(coordinates=curr, used_steps=used_steps, exit_found=True)
                return True

            self.maze[curr[0]][curr[1]] = "^"

            self.maze[curr_pos[0]][curr_pos[1]] = "."
            used_steps += 1

            self.print_info(current=curr, used_steps=used_steps)

            curr_pos = curr  # update the current position
            next_coords = self.find_next(curr)

            for coord in next_coords:
                if used_steps >= self.steps:
                    self.write_solution(coordinates=curr, used_steps=used_steps, exit_found=False)
                    return False
                stack.append(coord)
        return False

    def print_maze(self):
        time.sleep(0.1)
        self.terminal.clear()
        # Clear the screen
        self.terminal.move(0, 0)
        for row in self.maze:
            print(" ".join(row).replace("0", " ").replace("1", "#"))
