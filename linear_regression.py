import pandas as pd
import matplotlib.pyplot as plt

class PlotContainer(object):

    def __init__(self, plots, dataframes):
        """
        plots: list: contains the setup information to create the graph
        dataframes: list: contains the dataframes that provide the information
            to be plotted.
        """
        self.plots = plots
        self.dfs = dataframes
        self.fig = plt.figure(1)

    def __len__(self):
        return len(self.plots)

    def add(self, plot, dataframe):
        """
        plot: method: a method that creates a plot
        dataframe: the dataframe associated with the plot
        """
        self.plots.append(plot)
        self.dfs.append(dataframe)

    def graph(self, start=0, stop=None):
        """
        creates the graph from the containers plots and DataFrame Store.
        """
        for i, plot in enumerate(self.plots[start: stop]):
            plot(self.dfs[i])

        title = 'linear_regression_{0}_{1}'.format(df.name, i)
        plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.savefig(title)

    def successive(self):
        """
        with each iteration we graph and merge in one more graph
        """
        for i in range(self.__len__()):
            self.graph(0, i + 1)


def scatter_plot(df):
    """
    df: DataFrame
    creates a scatter plot of the x and y points
    """
    plt.scatter(x=df.x, y=df.y, color='g', marker='x', 
            linewidth=20, alpha=0.8, label='data points')


def regression_line_plot(df):
    """
    df: DataFrame
    creates a 2d line that represents the regression line through the x and y 
    points.
    """
    plt.plot(df.x, regression_line(df.x, df.slope, df.intercept) , 'bo', 
            df.x,  regression_line(df.x, df.slope, df.intercept), 'k', 
            color="black", c=10, linewidth=5, alpha=0.8,
            marker='x', markersize=15)


def sum_of_squares_regression_plot_with_line(df):
    """
    df: DataFrame
    creates a visual representation of the sum of squares for the 
    regression line of the x and y points.
    """
    for i in range(len(df)):
        #we need to make a box
        #  between (x,y) and (x, estimated)
        x = (df.x[i], df.x[i])
        y = (df.estimated_y[i], df.y[i])
        
        plt.plot(x, y, color='blue', linewidth=5, alpha=0.6, linestyle='--')

def sum_of_squares_regression_plot_with_box(df):
    """
    df: DataFrame
    creates a visual representation of the sum of squares for the 
    regression line of the x and y points.
    """
    for i in range(len(df)):
        #we need to make a box
        #  between (x,y) and (x, estimated)
        x = (df.x[i], df.x[i])
        y = (df.estimated_y[i], df.y[i])

        d = abs(df.estimated_y[i] - df.y[i])
        # top line 
        tx = (df.x[i], df.x[i] + d) 
        ty = (df.y[i], df.y[i])
        # bottom line
        bx = (df.x[i], df.x[i] + d)
        by = (df.estimated_y[i], df.estimated_y[i])
        # adjacent line
        ax = (df.x[i] + d, df.x[i] + d)
        ay = (df.y[i], df.estimated_y[i])

        plt.plot(x, y, tx, ty, bx, by, ax, ay, 
                color='silver', linewidth=5, alpha=0.6, linestyle='--')


def regression_line(x, slope, intercept): 
    """
    x: column of x coordinates
    slope: float: the slope of the line
    intercept: float: the intercept of the line
    rype: column of the estimated y coordinates. i.e the regression line
    """
    return (slope * x) + intercept


def estimated_y(df):
    """ 
    df: Dataframe
    rytpe: column representing the estimated y values.
    """
    df.slope = df.x.cov(df.y) / df.x.var()
    df.intercept = df.y.mean() - (df.slope * df.x.mean())
    return (df.x * df.slope) + df.intercept


def linear_regression(df):
    """
    
    df: DataFrame
    sets up the DataFrame and creates graphs featuring linear regression.
    """
    df.estimated_y = estimated_y(df)
    plots = [scatter_plot, sum_of_squares_regression_plot_with_line, 
            sum_of_squares_regression_plot_with_box, regression_line_plot]
    dfs = [df] * len(plots)
    dfs_plot_container = PlotContainer(plots, dfs)
    dfs_plot_container.successive()

if __name__ == '__main__':

    rec = pd.DataFrame({
        'x': [1,1,5,5,10,10],
        'y': [1,5,1,5,1,5]})
    rec.name = 'square'

    outlier = pd.DataFrame({
        'x': [1,1,5,5,10,10],
        'y': [1,5,1,10,30,5]})
    outlier.name = 'outlier'

    data = [rec, outlier]

    for df in data:
        linear_regression(df)

