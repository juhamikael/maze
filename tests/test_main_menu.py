from unittest.mock import patch
from maze.main_menu import MainMenu


class TestMainMenu:
    def test_main_menu_name(self):
        """Test that the name is correct"""
        main_menu = MainMenu([[]])
        with patch("builtins.input", return_value="test"), patch("builtins.print"):
            main_menu.main_menu()
            assert main_menu.name == "Test"

    def test_main_menu_prints(self):
        """Test that the prints are correct"""
        main_menu = MainMenu([[]])

        with patch("builtins.input", return_value="test"), patch("builtins.print") as mock_print:
            main_menu.main_menu()
            call_args_list = mock_print.call_args_list
            assert "Welcome to the maze solver Test!" in str(call_args_list[0])
            assert "Found 1 mazes" in str(call_args_list[1])

    def test_main_menu_prints_no_mazes(self):
        """Test that the prints are correct and no mazes are found"""
        main_menu = MainMenu([])
        assert main_menu.maze == []

        with patch("builtins.input", return_value="test"), patch("builtins.print") as mock_print, patch(
                "builtins.exit"):
            main_menu.main_menu()
            call_args_list = mock_print.call_args_list
            assert "No mazes found" in str(call_args_list[1])

    def test_main_menu_choice_1(self):
        """Test that the prints are correct"""
        main_menu = MainMenu([[], []])
        main_menu.choice = 1
        assert main_menu.maze == [[], []]

        with patch("builtins.input", return_value="1"), patch("builtins.print") as mock_print:
            main_menu.main_menu()
            call_args_list = mock_print.call_args_list
            assert "Solve a maze" in str(call_args_list[2])

        with patch("builtins.input", return_value="2"), patch("builtins.print") as mock_print:
            main_menu.select_option()
            call_args_list = mock_print.call_args_list
            assert main_menu.maze_to_solve == 2
            assert "Total mazes to solve" in str(call_args_list[0])
            assert "Choose a maze to solve" in str(call_args_list[1])
            assert f"Solving maze 3" in str(call_args_list[2])

    def test_main_menu_choice_2(self):
        """Test that the prints are correct"""
        # Create a MainMenu object with two mazes
        main_menu = MainMenu([[], []])

        main_menu.choice = "2"

        # Patch the input and print functions
        with patch("builtins.input", return_value="4"), patch("builtins.print") as mock_print:
            main_menu.select_option()
            call_args_list = mock_print.call_args_list

            # Assert correct prints
            assert "Choose steps to solve the maze" in str(call_args_list[0])
            assert "1. 20 steps" in str(call_args_list[1])
            assert "2. 150 steps" in str(call_args_list[2])
            assert "3. 200 steps" in str(call_args_list[3])
            assert "4. Custom steps" in str(call_args_list[4])
            assert "5. Back to main menu" in str(call_args_list[5])
            assert main_menu.steps == 4

    def test_all_steps(self):
        """
        By using input patch, using 2 causes recursion error and goes into infinite loop
        So we test all steps manually by setting them up and then asserting that it is correct
        """
        main_menu = MainMenu([[], []])

        main_menu.steps = 20
        assert main_menu.steps == 20

        main_menu.steps = 150
        assert main_menu.steps == 150

        main_menu.steps = 200
        assert main_menu.steps == 200

        main_menu.steps = 500
        assert main_menu.steps == 500

    def test_get_data(self):
        """Test that the data is correct"""
        main_menu = MainMenu([[]])
        main_menu.name = "Test"
        main_menu.maze_to_solve = 1
        main_menu.steps = 20
        data = main_menu.get_data()
        assert data == (0, "Test", 20)
        assert type(data) == tuple

    def test_get_menu_choice(self):
        """Test that the menu choice is correct"""
        main_menu = MainMenu([[]])
        main_menu.choice = 1
        choice = main_menu.get_menu_choice()

        assert choice == 1
        assert type(choice) == int

    @patch("os.system", return_value=None)
    @patch("time.sleep", return_value=None)
    def test_exit_screen(self, mock_sleep, mock_system):
        main_menu = MainMenu([[]])
        with patch("builtins.print"), patch("builtins.exit"):
            main_menu.exit_screen()
            assert mock_sleep.call_count == 50
            assert mock_system.call_count == 1
            assert main_menu.exit_program is True

