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

    def __len__(self):
        return len(self.plots)


    def add(self, plot, dataframe):
        """
        plot: method: a method that creates a plot
        dataframe: the dataframe associated with the plot
        """
        self.plots.append(plot)
        self.dfs.append(dataframe)


    def graph(self, fname='', directory='', setup=None,  start=0, stop=None, clean=True):
        """
        creates the graph from the containers plots and DataFrame Store.
        fname: string: filename
        start: int: starting point of graphs to overlay.
        stop: int: ending point of graphs to overlay.
        clean: boolean: we want to make sure we don't overlay between sets of graphs
        creates a 'master graph
        """
        for i, plot in enumerate(self.plots[start: stop]):
            plot(self.dfs[i])
        setup()
        plt.title(fname)
        path = fname if not directory else directory + '/' + fname
        plt.show() if not fname else plt.savefig(path)
        if clean: plt.gca().cla()

