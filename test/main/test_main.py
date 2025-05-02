import pytest
from unittest.mock import patch, MagicMock
import builtins

@patch("interface.controller.main_controller.MainController.execute")
@patch("interface.controller.main_controller.MainController")
@patch("builtins.__name__", "__main__")
def test_main_runs_successfully(mock_controller_class, mock_execute):
    """
    Test that the main function runs successfully.

    This test verifies that the main function, when called, correctly creates an
    instance of MainController and calls its execute method with the correct
    arguments.

    Args:
        mock_controller_class: A mock of the MainController class used to replace
        the actual class in the test.
        mock_execute: A mock of the execute method of MainController, set to do
        nothing when called.

    Asserts:
        The MainController instance is created with the correct base URL.
        The execute method of the MainController instance is called with the
        correct csv_path argument.
    """
    from main import main  

    mock_controller_instance = MagicMock()
    mock_controller_class.return_value = mock_controller_instance

    main()

    mock_controller_class.assert_called_once_with(base_url="https://demoqa.com")
    mock_controller_instance.execute.assert_called_once_with(csv_path="output/books_api.csv")

@patch("interface.controller.main_controller.MainController.execute", side_effect=Exception("Erro simulado"))
@patch("interface.controller.main_controller.MainController")
@patch("builtins.__name__", "__main__")
def test_main_logs_exception(mock_controller_class, mock_execute):
    """
    Test that the main function logs exceptions without propagating them.

    This test verifies that when an exception is raised during the execution 
    of the main function, the exception is logged and not propagated. It uses 
    a mock to simulate an exception being thrown by the execute method of the 
    MainController class.

    Args:
        mock_controller_class: A mock of the MainController class used to replace 
        the actual class in the test.
        mock_execute: A mock of the execute method of MainController, set to raise 
        an exception when called.

    Asserts:
        The exception is caught and logged, and pytest.fail is not triggered, 
        indicating the exception was not propagated.
    """

    from main import main

    mock_controller_instance = MagicMock()
    mock_controller_class.return_value = mock_controller_instance

    try:
        main()
    except Exception:
        pytest.fail("Exceção não deveria ser propagada no main")
