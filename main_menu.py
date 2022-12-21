import os
import time


class MainMenu:
    def __init__(self, maze: list):
        self.maze = maze
        self.name = ""
        self.steps = 200
        self.choice = None
        self.maze_to_solve = None
        self.exit_program = False

    def main_menu(self) -> None:
        if self.name == "":
            self.name = input("Please enter your name: ").lower().capitalize()
            print(f"\nWelcome to the maze solver {self.name}!")
        if len(self.maze) == 0:
            print("No mazes found, please create or get mazes to solve, check documentation\n"
                  "Exiting...")
            exit()
        else:
            print(f"\n{'-' * 50}\nFound {len(self.maze)} mazes in the folder to solve \n{'-' * 50}")
            print("1. Solve a maze")
            print(f"2. Choose steps (current {self.steps})")
            print("3. Exit")
        self.choice = input("Choose an option: ")
        self.select_option()

    def select_steps(self) -> None:
        print(f"\n{'-' * 40}\nChoose steps to solve the maze\n{'-' * 40}")
        print("1. 20 steps")
        print("2. 150 steps")
        print("3. 200 steps")
        print("4. Custom steps")
        print("5. Back to main menu")
        choice = input("Choose an option: ")
        # If not a number or not in range
        while choice not in ["1", "2", "3", "4", "5"] or not choice.isdigit():
            print("Invalid choice, try again")
            choice = input("Choose an option: ")

        if choice == "1":
            self.steps = 20
            self.main_menu()
        elif choice == "2":
            self.steps = 150
            self.main_menu()
        elif choice == "3":
            self.steps = 200
            self.main_menu()
        elif choice == "4":
            custom_steps = input("Enter custom steps: ")
            while not custom_steps.isdigit():
                print("Please enter a number")
                custom_steps = input("Enter custom steps: ")
            self.steps = int(custom_steps)
            self.main_menu()
        elif choice == "5":
            self.main_menu()

    def select_option(self) -> None:
        if self.choice == "1":
            self.store_selected_option()
        elif self.choice == "2":
            self.select_steps()
        elif self.choice == "3":
            self.exit_screen()

    def store_selected_option(self) -> None:
        print(f"\nTotal mazes to solve: {len(self.maze)} \n{'-' * 40}")
        print("Choose a maze to solve")
        self.maze_to_solve = int(input("Maze: "))
        while self.maze_to_solve not in range(1, len(self.maze) + 1):
            print("Invalid choice, try again")
            self.maze_to_solve = int(input("Maze: "))

        self.solve_specific_maze()

    def solve_specific_maze(self) -> None:
        print(f"Solving maze {self.maze_to_solve + 1} for {self.name}...\n")

    def get_data(self) -> tuple:
        return int(self.maze_to_solve)-1, self.name, int(self.steps)

    def get_menu_choice(self) -> str:
        return self.choice

    def exit_screen(self):
        print("Exiting")
        for i in range(50):
            print("=" * i, end="\r")
            time.sleep(0.05)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.exit_program = True
        exit()
