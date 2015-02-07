import pandas as pd
import matplotlib.pyplot as plt


def graph_all(graph, new_plot):
    graph.append(new_plot)
    [g() for g in graph]


def scatter():
    plt.scatter(x=df.cells, y=df.photo, color='g')


def mean():
    plt.plot(x_range, y_mean, color="brown")


def regression():
    plt.plot(df.cells, df.expected)


def SStotal():
    for i in range(len(df)):
        x = (df.cells[i], df.cells[i])
        y = (df.photo.mean(), df.photo[i])
        plt.plot(x, y, color='black')


def SSreg():
    for i in range(len(df)):
        x = (df.cells[i], df.cells[i])
        y = (df.expected[i], df.expected[i])
        plt.plot(x, y, color='black')


if __name__ == '__main__':
    df = pd.DataFrame({
        'cells': [116, 117, 120, 1, 52, 79, 109, 27, 85, 51, 78, 55, 26, 39, 107],
        'photo': [60, 67, 64, 8, 13, 63, 63, 2, 46, 27, 43, 24, 10, 28, 56]})

    plot_container = []
    graph_all(plot_container, scatter)

    x_range = df.cells.min(), df.cells.max()
    y_mean = df.photo.mean(), df.photo.mean()
    graph_all(plot_container, mean)

    slope = df.cells.cov(df.photo) / df.cells.var()
    intercept = df.photo.mean() - (slope * df.cells.mean())
    df.expected = (df.cells * slope) + intercept
    graph_all(plot_container, regression)

    graph_all(plot_container, SStotal)

    graph_all(plot_container, SSreg)

    sum_of_squares = {'total': ((df.photo - df.photo.mean())**2).sum()}
    sum_of_squares['regression'] = ((df.photo - df.expected)**2).sum()

    r_squared = 1 - (sum_of_squares['regression'] / sum_of_squares['total'])
