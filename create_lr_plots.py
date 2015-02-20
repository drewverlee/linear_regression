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
            estimated_y_plot, 
            regression_line_plot,
            sum_of_squares_regression_plot_with_line, 
            sum_of_squares_regression_plot_with_box, 


            ]

    normal = pd.DataFrame({
        'x': [1,2,3,4,5,6,7],
        'y': [1,3,2,5,3,7,5]})
    normal.name = ''

    outlier = pd.DataFrame({
        'x': [1,1,5,5,25,10],
        'y': [1,5,1,10,10,5]})
    outlier.name = 'with outlier'

    dataframes = [normal, outlier]

    for df in dataframes:
        linear_regression(df)
        dfs = [df] * len(plots)
        pc = PlotContainer(plots, dfs)
        # now we want to successively create plots and overlay them over previous 
        # ones
        for i in range(len(pc)):
            fname = 'Linear Regression {0} example part {1}'.format(pc.dfs[i].name, i)
            pc.graph(fname, directory='images', setup=shared_setup, start=0, stop=1+i)
