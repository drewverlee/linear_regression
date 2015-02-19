import matplotlib.pyplot as plt
from linear_regression import regression_line
def scatter_plot(df):
    """
    df: DataFrame
    creates a scatter plot of the x and y points
    """
    plt.scatter(x=df.x, y=df.y, color='g', marker='x', 
            linewidth=20, alpha=0.8, label='data points')

def estimated_y_plot(df):
    """
    df: DataFrame
    creates a 2d line that represents the estimated y points.
    """
    plt.plot(df.x, df.estimated_y, 'bo', 
            color="red", linewidth=5, alpha=0.8, label='estimated y', 
            marker='x', markersize=15)


def regression_line_plot(df):
    """
    df: DataFrame
    creates a 2d line that represents the regression line through the x and y 
    points.
    """
    plt.plot(df.x, regression_line(df.x, df.slope, df.intercept) , 
            color="red", linewidth=5, alpha=0.6, label='regression line')


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
        if i == 0:
            plt.plot(x, y, 
                    color='blue', linewidth=5, alpha=0.6, linestyle='--', label='least squares')
        else:
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

        if i == 0:
            plt.plot(x, y, tx, ty, bx, by, ax, ay, 
                    color='silver', linewidth=5, alpha=0.6, linestyle='--')
        else:
            plt.plot(x, y, tx, ty, bx, by, ax, ay, color='silver', linewidth=5, alpha=0.6, linestyle='--')
