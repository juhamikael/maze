from pathlib import Path
from tempfile import TemporaryDirectory

from maze.create_maze import CreateMaze


class TestCreateMaze:

    def test_load_files(self):
        """ Test that the files are loaded """

        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            maze = CreateMaze(path)

            for i in range(5):
                with open(f"{temp_dir}/maze-task-{i + 1}.txt", "w") as f:
                    f.write("Maze file contents")

            maze.load_files()

            # Checking if the length of the list maze.files is equal to 5
            assert len(maze.files) == 5

            # Checking if the file names are correct
            for i in range(5):
                assert maze.files[i].name == f"maze-task-{i + 1}.txt"

            # assert that the files attribute only contains the mock maze files
            assert all(
                file.name.startswith("maze-task") and file.name.endswith(".txt")
                for file in maze.files
            )

    def test_read_files(self):
        """ Test that the files are read """

        # Absolute path to the test_files directory
        path = Path(__file__).parent.parent / Path("tests") / Path("test_files")
        maze = CreateMaze(path)

        maze.files = [
            path / Path("maze-task_test_maze_1.txt"),
            path / Path("maze-task_test_maze_1.txt")]

        maze.read_files()

        assert maze.maze
        assert len(maze.maze) == 2
        assert len(maze.maze) == len(maze.files)
        for i in range(len(maze.maze)):
            with open(maze.files[i], "r") as f:
                expected_output = f.read().replace("#", "1").replace(" ", "0")
            assert maze.maze[i] == expected_output

    def test_create_dir(self):
        """Test that the "mazes" directory is created"""
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            maze = CreateMaze(path)
            maze.create_dir()
            assert (path / Path("mazes")).exists()

    def test_create_solved_dir(self):
        """Test that the "solved" directory is created"""
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            maze = CreateMaze(path)
            maze.create_solved_dir()
            assert (path / Path("solved")).exists()

    def test_write_files(self):
        """Test that the write_files function writes the maze to a file with the correct name and contents"""
        # Set up test data
        maze_string = "101010101"
        expected_file_name = "maze-task_test_maze_1_numbers.txt"
        expected_file_contents = maze_string

        # Setting up the CreateMaze object and adding the test data to it
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)
            maze = CreateMaze(path)
            maze.maze = [maze_string]
            maze.files = [Path("./maze-task_test_maze_1.txt")]
            maze.create_dir()

            # Call the write_files function
            maze.write_files()

            # Assert that the file was created with the correct name and contents
            maze_file_path = path / Path("mazes") / Path(expected_file_name)
            assert maze_file_path.exists()
            with open(maze_file_path, "r") as f:
                actual_file_contents = f.read()
            assert actual_file_contents == expected_file_contents

    def test_create_matrix(self):
        """Test that the create_matrix function correctly creates a matrix of 0's and 1's"""

        # Set up test data and load the maze from the test files
        # Absolute path to the test_files directory
        path = Path(__file__).parent.parent / Path("tests") / Path("test_files")

        maze = CreateMaze(path)
        maze.files = [path / Path("maze-task_test_maze_1.txt")]

        maze.read_files()
        maze.create_dir()
        maze.write_files()

        temp_file_name = Path("mazes") / "maze-task_test_maze_1_numbers.txt"

        maze.create_matrix()

        # Checks that matrix is not empty and is created
        assert maze.maze is not [] or maze.maze is not [[]]

        # Checks that the matrix is created correctly and contains 5 rows (lists)
        # And 8 columns (elements)
        # Matrix size = 5x8
        assert len(maze.maze[0]) == 5
        assert len(maze.maze[0][0]) == 8

        # Deleting the temporary file and directory
        (path / temp_file_name).unlink()
        (path / Path("mazes")).rmdir()

        # Returns the matrix which is used in the test_get_maze function

    def test_get_maze(self):
        """Test that the get_maze function returns the correct maze"""
        # Set up test data
        path = Path("test_files")
        maze = CreateMaze(path)
        maze.maze = [[['1', '1', '1', '1', '1', '1', '1', '1'],
                      ['1', '1', '0', '1', '0', '0', '0', 'E'],
                      ['^', '0', '0', '1', '0', '1', '1', '1'],
                      ['1', '0', '0', '0', '0', '0', '0', '1'],
                      ['1', '1', '1', '1', '1', '1', '1', '1']]]

        actual_maze = maze.get_maze()

        assert actual_maze is not [] or actual_maze is not [[]]
        assert maze.maze == actual_maze
