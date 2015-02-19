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
    finds the estimated y values based on linear regression
    """
    df.estimated_y = estimated_y(df)




