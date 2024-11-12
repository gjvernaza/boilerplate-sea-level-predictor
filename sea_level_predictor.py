import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv', sep=',')
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    

    # Create first line of best fit

    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    # y    =  mx + b
    y_pred = slope * x_pred + intercept

    ax.plot(x_pred, y_pred, 'r')

    # Create second line of best fit

    df_forecasted = df[df['Year'] >= 2000].reset_index(drop=True)
    x_forecasted = df_forecasted['Year']
    y_forecasted = df_forecasted['CSIRO Adjusted Sea Level']
    slope_forecasted, intercept_forecasted, r_value_forecasted, p_value_forecasted, std_err_forecasted = linregress(x_forecasted, y_forecasted)
    x_pred_forecasted = pd.Series([i for i in range(2000, 2051)])
    y_pred_forecasted = slope_forecasted * x_pred_forecasted + intercept_forecasted
    ax.plot(x_pred_forecasted, y_pred_forecasted, 'g')
    

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()