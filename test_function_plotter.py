
import pytest
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
from main import Window
from unittest.mock import patch

@pytest.fixture
def app(qtbot):
    application = QApplication.instance()
    if not application:
        application = QApplication([])
    window = Window()
    qtbot.addWidget(window)
    yield window
    application.quit()

def test_valid_input(app, qtbot):
    # Simulate user input
    app.function.setText("5*x^3 + 2*x")
    app.min_x.setText("-10")
    app.max_x.setText("10")

    # Simulate button click
    qtbot.mouseClick(app.plot_button, Qt.LeftButton)

    # Assert the plot is displayed correctly
    assert len(app.figure.axes) == 1
    assert app.figure.axes[0].get_xlabel() == 'x-axis'
    assert app.figure.axes[0].get_ylabel() == 'y-axis'
    assert app.figure.axes[0].get_title() == 'Function Plotter'

def test_invalid_input(app, qtbot):
    # Simulate user input with invalid function
    app.function.setText("5*x^3 + 2*")
    app.min_x.setText("0")
    app.max_x.setText("10")

    # Simulate button click
    with patch('PySide2.QtWidgets.QMessageBox.warning') as mock_warning:
        qtbot.mouseClick(app.plot_button, Qt.LeftButton)

        # Assert error message is displayed
        mock_warning.assert_called_once()
        assert mock_warning.call_args[0][0] == app
        assert mock_warning.call_args[0][1] == 'Invalid Input Function'

    # -----------------------------

    # Simulate user input with invalid min_x
    app.function.setText("5*x^3 + 2*x")
    app.min_x.setText("abc")
    app.max_x.setText("10")

    # Simulate button click
    with patch('PySide2.QtWidgets.QMessageBox.warning') as mock_warning:
        qtbot.mouseClick(app.plot_button, Qt.LeftButton)

        # Assert error message is displayed
        mock_warning.assert_called_once()
        assert mock_warning.call_args[0][0] == app
        assert mock_warning.call_args[0][1] == 'Invalid Input Number'

    # -----------------------------

    # Simulate user input with invalid function
    app.function.setText("++3x+-")
    app.min_x.setText("0")
    app.max_x.setText("10")

    # Simulate button click
    with patch('PySide2.QtWidgets.QMessageBox.warning') as mock_warning:
        qtbot.mouseClick(app.plot_button, Qt.LeftButton)

        # Assert error message is displayed
        mock_warning.assert_called_once()
        assert mock_warning.call_args[0][0] == app
        assert mock_warning.call_args[0][1] == 'Invalid Input Function'

    # -----------------------------

    # Simulate user input with invalid function
    app.function.setText("xx")
    app.min_x.setText("0")
    app.max_x.setText("10")

    # Simulate button click
    with patch('PySide2.QtWidgets.QMessageBox.warning') as mock_warning:
        qtbot.mouseClick(app.plot_button, Qt.LeftButton)

        # Assert error message is displayed
        mock_warning.assert_called_once()
        assert mock_warning.call_args[0][0] == app
        assert mock_warning.call_args[0][1] == 'Invalid Input Function'

if __name__ == "__main__":
    pytest.main()
