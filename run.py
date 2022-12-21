from create_maze import CreateMaze
from main_menu import MainMenu
from move_in_maze import MoveInMaze
from pathlib import Path

from config import maze_path


def create_mazes(create_maze: CreateMaze) -> None:
    """
    Create a maze
    :param create_maze: CreateMaze object
    :return: CreateMaze.get_maze() (matrixes of mazes)
    """
    create_maze.load_files()
    create_maze.create_matrix()


def get_mazes(created_mazes: CreateMaze) -> list:
    """
    Get the mazes
    """
    return created_mazes.get_maze()


def solve_mazes(MAZES: list, MAZE_NUMBER: int, NAME: str, PATH: Path, STEPS) -> None:
    """
    :param MAZES: list of mazes
    :param MAZE_NUMBER: number of maze
    :param NAME: name of the user
    :param PATH: path to the maze/solved directory
    :param STEPS: number of steps selected by the user (default 200)
    """
    MAZE_TO_SOLVE = MAZES[MAZE_NUMBER]
    move = MoveInMaze(maze=MAZE_TO_SOLVE, path=PATH, name=NAME, maze_to_solve=MAZE_TO_SOLVE, steps=STEPS, choice=MAZE_NUMBER+1)
    move.solve_maze()


if __name__ == "__main__":
    path = Path(maze_path)
    maze = CreateMaze(path=path)

    create_mazes(maze)
    matrix = get_mazes(maze)

    menu = MainMenu(maze=matrix)
    while True:
        menu.main_menu()
        data = menu.get_data()
        if menu.get_menu_choice() == "3":
            break
        else:
            solve_mazes(MAZES=matrix, NAME=data[1], PATH=path, MAZE_NUMBER=data[0], STEPS=data[2])
