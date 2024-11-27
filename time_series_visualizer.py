import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

df = pd.read_csv("C:/Users/Ziad\Desktop\Data Analysis Projects/boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv",
                 parse_dates=['date'],
                 index_col='date')

# Clean data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15,5))
    plt.plot(df.index,df['value'],c='firebrick')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
# draw_line_plot()
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_bar = df_bar.groupby(['year','month'])['value'].mean()
    df_bar = df_bar.unstack()
    df_bar.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    
    fig = df_bar.plot(kind= 'bar',figsize=(8,6), xlabel='Years',ylabel='Average Page Views').figure

    plt.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    

    fig, ax = plt.subplots(nrows= 1, ncols= 2, figsize=(18,6))

    ax[0]= sns.boxplot(data=df_box,x=df_box['year'], y = df_box['value'], ax=ax[0],palette=sns.color_palette())
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    months_order= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'],categories=months_order,ordered=True)

    ax[1]= sns.boxplot(x=df_box['month'], y = df_box['value'], ax=ax[1],palette=sns.color_palette('husl',12))
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Draw box plots (using Seaborn)
    
    # fig, (ax1,ax2) = plt.subplots(1,2, figsize=(18,6))
    # sns.boxplot(x=df_box['year'],y=df_box['value'],data=df_box,ax=ax1)
    # # ,palette=sns.color_palette()
    # ax1.set_title('Year-wise Box Plot (Trend)')
    # ax1.set_xlabel('Year')
    # ax1.set_ylabel('Page Views')

    # months_order= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # df_box['month'] = pd.Categorical(df_box['month'],categories=months_order,ordered=True)
    
    # sns.boxplot(data=df_box,ax=ax2,x='month',y='value',order=months_order)
    # # ,palette=sns.color_palette('husl',12)
    # ax2.set_title('Month-wise Box Plot (Seasonality)')
    # ax2.set_xlabel('Month')
    # ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()