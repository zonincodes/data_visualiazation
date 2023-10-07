import matplotlib
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

if __name__ == "__main__":
    draw_scatter()
