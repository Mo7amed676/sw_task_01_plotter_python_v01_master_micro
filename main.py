# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
# Use a breakpoint in the code line below to debug your script.
# @ created by eng.Mohamed Mahmoud

from PySide2.QtWidgets import QApplication, QVBoxLayout, QPushButton, QLineEdit, QLabel, QWidget, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import re


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.function = QLineEdit(self)
        self.min_x = QLineEdit(self)
        self.max_x = QLineEdit(self)

        self.plot_button = QPushButton('Plot', self)
        self.plot_button.clicked.connect(self.plot)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Enter function of x like "5*x^3 + 2*x" or constant function like "9" or "-3" '
                                'etc. with using operators (+,-,*,/,^,(,)):'))
        self.function.setPlaceholderText("Enter function of x can meet with a function rules...")

        layout.addWidget(self.function)
        layout.addWidget(QLabel('Enter minimum value of x that pose to be smaller than maximum value of x '
                                '"Must be a number":'))
        layout.addWidget(self.min_x)
        self.min_x.setPlaceholderText("Enter Lower Bound Range value of x...")

        layout.addWidget(QLabel('Enter maximum value of x that pose to be greater than minimum value of x '
                                '"Must be a number":'))
        layout.addWidget(self.max_x)
        self.max_x.setPlaceholderText("Enter Upper Bound Range value of x...")

        layout.addWidget(self.plot_button)

        self.setLayout(layout)

    def validate_inputs(self):
        function_pattern = r'^(?i)[+\-*/^0-9(x)\s]+(?<![+\-*/^])$'  # check pattern of all components of the mathematical function
        min_max_pattern = r'^[+-]?\d*\.?\d+$'  # check for numbers +ve and -ve and decimal

        function_valid = re.match(function_pattern, self.function.text())  # function user input
        min_x_valid = re.match(min_max_pattern, self.min_x.text())  # minimum user input
        max_x_valid = re.match(min_max_pattern, self.max_x.text())  # maximum user input

        # here all checks and tests for testcases

        if not function_valid:
            QMessageBox.warning(self, 'Invalid Input Function', 'Please enter valid input functions of x like '
                                                                '5*x^3 + 2*x , 1/x , ( ) for priority,etc. or '
                                                                'also can use capital X letter')
            return False

        if not min_x_valid:
            QMessageBox.warning(self, 'Invalid Input Number', 'Please enter valid input numbers like '
                                                              '4,-7,9,-1,0,8.4,.9,'
                                                              'etc Must be smaller than next number".')
            return False

        if not max_x_valid:
            QMessageBox.warning(self, 'Invalid Input Number', 'Please enter valid input numbers like '
                                                              '4,-7,9,-1,0,3.1,-8.2,etc '
                                                              '"Must be greater than previous number".')
            return False

        if 'x' not in self.function.text().lower():
            if not re.match(r'^[+-]?\d*\.?\d*$', self.function.text()):  # regex start with +|-
                QMessageBox.warning(self, 'Invalid Input',
                                    'Function must contain the variable "x" or be a constant.')
                return False

        # Check for consecutive Xs and number without an operator  <xx, 2x, x2, **x, 4^^, etc...
        if re.search(r'\dx|\d+x|x\d|x\d+|[+\-\*^/][+\-\*^/]+(x|\d)|^[*/^].*', self.function.text()) \
                or re.search(r'xx|\d+x+', self.function.text()):
            QMessageBox.warning(self, 'Invalid Input',
                                'Invalid expression. Use an operator (+, -, *, /, ^) between the number and variable.')
            return False

        min_x = float(self.min_x.text())
        max_x = float(self.max_x.text()) 

        if min_x >= max_x:
            QMessageBox.warning(self, 'Invalid Input',
                                'Minimum value of x cannot be greater than or equal to maximum value.')
            return False
        return True

    def plot(self):
        if not self.validate_inputs():
            return
        self.figure.clear()

        x = np.linspace(float(self.min_x.text()), float(self.max_x.text()), 400)
        if 'x' in self.function.text().lower():
            y = eval(self.function.text().lower().replace('^', '**'))  # support ^ in the function
            plt.plot(x, y, label=f'y={self.function.text()} , Range [{self.min_x.text()},{self.max_x.text()}]') # legend
        else:  # if constant function
            constant_value = float(self.function.text())
            if constant_value == 0:
                y = constant_value
                plt.axhline(y=constant_value, color='b', linestyle='-', label=f'y={y} , Range [{self.min_x.text()},{self.max_x.text()}]')
            else:
                y = constant_value
                plt.axhline(y=constant_value, color='b', linestyle='-', label=f'y={y} , Range [{self.min_x.text()},{self.max_x.text()}]')

        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Function Plotter')
        plt.grid(True)
        plt.legend()
        plt.show()


# Press the green button in the gutter to run the script
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
