from pathlib import Path


class CreateMaze:
    def __init__(self, path: Path):
        self.files = []
        self.maze = []
        self.path = path

    def load_files(self) -> None:
        """
        Load the files from the path
        :return: None
        """
        files = []
        for file in self.path.iterdir():
            if file.name.startswith("maze-task") and file.name.endswith(".txt"):
                files.append(file)
        self.files = files
        self.create_dir()
        self.create_solved_dir()
        self.read_files()
        self.write_files()

    def read_files(self) -> None:
        """
        Read the files and store the mazes in a list
        :return: None
        """
        maze_list = []
        for file in self.files:
            # In maze, Change characters: # to 0 & " " to 1
            with open(file, "r") as text_file:
                maze_file = text_file.read().replace("#", "1").replace(" ", "0")
            maze_list.append(maze_file)

        self.maze = maze_list

    def create_dir(self):
        """
        Create a directory to store the mazes in self.path
        :return: None
        """
        Path(f"{self.path}/mazes").mkdir(parents=True, exist_ok=True)

    def create_solved_dir(self) -> None:
        """
        Create a directory to store the solved mazes in self.path
        :return: None
        """
        Path(f"{self.path}/solved").mkdir(parents=True, exist_ok=True)

    def write_files(self) -> None:
        """
        Write the number_mazes to a file as maze-task-{nmbr}_2.
        Not necessary for testing purposes only
        :return: None
        """
        paths = self.files

        for path in paths:
            # Remove ".txt" from the file name
            file_name = path.name.replace(".txt", "")

            # Avoiding to create multiple _numbers_numbers....txt files
            if file_name.endswith("_numbers"):
                file_name = file_name[:-8]
            new_file_name = file_name + "_numbers.txt"

            # Create a new file with the same name as the original file
            with open(f"{self.path}/mazes/{new_file_name}", "w") as maze_file:
                maze_file.write("")

            with open(f"{self.path}/mazes/{new_file_name}", "w") as maze_file:
                maze_file.write(self.maze[paths.index(path)])

    def create_matrix(self):
        """
        Create a matrix from the maze of 0's & 1's
        :param maze_matrix:
        :return: List of lists
        """
        new_path = self.path / "mazes"

        matrix = []
        for file in new_path.iterdir():
            if file.name.startswith("maze-task") and file.name.endswith(".txt"):
                with open(file, "r") as maze_file:
                    maze_list = maze_file.read()
                    temp_matrix = []
                    for row in maze_list.splitlines():
                        temp_matrix.append(list(row))
                    matrix.append(temp_matrix)

        self.maze = matrix

    def get_maze(self):
        return self.maze
