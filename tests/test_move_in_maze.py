from pathlib import Path
import shutil
from maze.move_in_maze import MoveInMaze
from unittest.mock import patch


def maze_matrix():
    valid_maze = [
        ["^", "1", "1", "1"],
        ["0", "1", "0", "E"],
        ["0", "0", "0", "1"],
        ["1", "1", "1", "1"]
    ]

    invalid_maze = [
        ["0", "1", "1", "1"],
        ["0", "1", "0", "E"],
        ["0", "0", "0", "1"],
        ["1", "1", "1", "1"]
    ]
    return {"valid": valid_maze, "invalid": invalid_maze}


class TestMoveInMaze:
    def test_init(self):
        """Test that the maze is initialized correctly"""
        maze = maze_matrix()["valid"]
        path = Path(__file__).parent
        move_in_maze = MoveInMaze(maze, path, 0, "test", 20, 1)

        assert move_in_maze.maze == maze
        assert move_in_maze.name == "test"
        assert move_in_maze.maze_to_solve == 0
        assert move_in_maze.steps == 20
        assert move_in_maze.choice == 1

    def test_get_start_positions(self):
        """Test that the start positions are found correctly"""
        maze = maze_matrix()["valid"]
        path = Path(__file__).parent
        move_in_maze = MoveInMaze(maze, path, 0, "test", 50, 0)

        move_in_maze.get_start_positions()
        assert move_in_maze.start_positions == [(0, 0)]

        maze = maze_matrix()["invalid"]
        move_in_maze = MoveInMaze(maze, path, 0, "test", 50, 0)
        move_in_maze.get_start_positions()
        assert move_in_maze.start_positions == []

    def test_find_next(self):
        """Test that the next coordinates are found correctly"""
        maze = maze_matrix()["valid"]
        path = Path(__file__).parent
        move_in_maze = MoveInMaze(maze, path, 0, "test", 50, 0)

        move_in_maze.get_start_positions()
        assert move_in_maze.find_next((0, 0)) == [(1, 0)]

    @patch("time.sleep", return_value=None)
    def test_write_solution(self, mock_sleep):
        """Test that the solution is written correctly"""
        with patch("builtins.print"):
            maze = maze_matrix()["valid"]
            solved_path = Path("test_files/solved")
            solved_path.mkdir(parents=True, exist_ok=True)

            file_name = f"user_name_maze-0_solution.txt"
            full_path = solved_path / file_name

            path = Path("test_files")
            move_in_maze = MoveInMaze(maze, path, 0, "user_name", 20, 0)
            move_in_maze.solve_maze()
            assert full_path.exists()
            assert mock_sleep.call_count == 7

            found_string = "Exit found at coordinates"
            with open(full_path, "r") as f:
                assert found_string in f.read()

            # Clean up
            shutil.rmtree(solved_path)



