# sw_task_01_plotter_python_v01_master_micro
Python function plotter

This is a simple function plotter application built with Python and PySide2. It allows users to plot mathematical functions and visualize them using the matplotlib library.

Installation

Clone the repository to your local machine:

git clone https://github.com/Mo7amed676/sw_task_01_plotter_python_v01_master_micro.git

Install the required dependencies using pip:

pip install -r requirements.txt

Run the application:

python main.py

# Usage

Enter a mathematical function of x in the input field. The function can contain operators (+, -, *, /, ^), parentheses for grouping, and the variable "x". For example:

Valid function: 5*x^3 + 2*x
Valid constant function: 9
Invalid function: 5*x^3 + 2* (missing operand)
Enter the minimum and maximum values for the x-axis range. These values define the interval over which the function will be plotted.

Click the "Plot" button to generate the plot.

The plot will be displayed in a separate window. You can interact with the plot, zoom in/out, and save it as an image if desired.

Examples
Valid Input
Function: 5*x^3 + 2*x

Minimum x-value: -10

Maximum x-value: 10

Valid Example

Invalid Input
Function: 5*x^3 + 2*

Minimum x-value: 0

Maximum x-value: 10


