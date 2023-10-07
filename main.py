import matplotlib
import matplotlib.pyplot as plt


def run_app():
    """App entry point"""
    squares = [1, 4, 9, 16, 25]
    plt.plot(squares)
    plt.show()


if __name__ == "__main__":
    run_app()
