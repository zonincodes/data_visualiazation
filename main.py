import matplotlib.pyplot as plt


def plot_squares():
    """App entry point"""

    # numbers and squares to plot
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    # set the line width
    plt.plot(input_values, squares, linewidth=5)

    # set the chart title and label axis
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of the value")

    # set size of the tick labels.abs
    plt.tick_params(axis='both', labelsize=14)

    # draw the plot to screen
    plt.show()


def draw_scatter():
    """Draws a scatter plot"""

    plt.scatter(2, 4, s=200)
    
    # set the chart title and label axis
    plt.title("Square numbers", fontsize=16)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # set the size of tick label:
    plt.tick_params(axis='both', which='major', labelsize=14)

    # Show the chart
    plt.show()


def draw_multiple_scatter():
    """Draw multiple  scatter plots"""
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 2, 9, 16, 25]

    plt.scatter(x_values, y_values, s=100)

    # set the chart and label axis
    plt.title("Square numbers", fontsize=24)
    plt.xlabel("Values", fontsize=16)
    plt.ylabel("Square of Value", fontsize=16)

    # set the size of the tick label
    plt.tick_params(axis='both', which='major', labelsize=14)

    # Draw the plot
    plt.show()


def calculate_data_automatically():

    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in x_values]

    # scatter points and remove outlines
    plt.scatter(x_values, y_values, c="red", edgecolors='none', s=10)

    # set the chart and label axis
    plt.title("Square numbers", fontsize=24)
    plt.xlabel("Value", fontsize=16)
    plt.ylabel("Square of Value", fontsize=16)

    # set the size of the tick label
    plt.tick_params(axis='both', which='major', labelsize=14)

    # set the range for each axis
    plt.axis((0, 1100, 0, 1100000))

    # draw the plot
    plt.show()


if __name__ == "__main__":
    # draw_scatter()
    # draw_multiple_scatter()
    calculate_data_automatically()
