import pandas as pd
from plotcontainer import PlotContainer
from linear_regression import linear_regression
from lr_plots import *

def shared_setup():
    """
    pc: PlotContainer
    adds some shared aspects to each plot
    """
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1), scatterpoints=1, ncol=4,
            fancybox=True, shadow=True, prop={'size':10}, markerscale=1 )

    plt.xlabel('x points')
    plt.ylabel('y points')
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')

if __name__ == '__main__':

    plots = [scatter_plot, 
            regression_line_plot,
            estimated_y_plot, 
            sum_of_squares_regression_plot_with_line, 
            sum_of_squares_regression_plot_with_box, 
            ]

    rec = pd.DataFrame({
        'x': [1,1,5,5,10,10],
        'y': [1,5,1,5,1,5]})
    rec.name = 'rectangle'

    outlier = pd.DataFrame({
        'x': [1,1,5,5,10,10],
        'y': [1,5,1,10,30,5]})
    outlier.name = 'rectangle with an outlier'

    dataframes = [rec, outlier]

    for df in dataframes:
        linear_regression(df)
        dfs = [df] * len(plots)
        pc = PlotContainer(plots, dfs)
        # now we want to successively create plots and overlay them over previous 
        # ones
        for i in range(len(pc)):
            fname = 'Linear Regression example {0} part {1}'.format(pc.dfs[i].name, i)
            pc.graph(fname, setup=shared_setup, start=0, stop=1+i)
