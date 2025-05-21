import seaborn as sns
import matplotlib.pyplot as plt

def plot_chart(df, chart_type, x_axis, y_axis=None):
    """
    Plot a chart based on the suggested parameters.
    Returns the object matplotlib figure.
    """
    
    fig, ax = plt.subplots(figsize=(16, 7))
    
    if chart_type == "bar":
        # Group and calculate mean
        grouped  = df.groupby(x_axis)[y_axis].mean().reset_index()
        sns.barplot(data=grouped, x=x_axis, y=y_axis, ax=ax)
        
    elif chart_type == "box":
        sns.boxplot(data=df, x=x_axis, y=y_axis, ax=ax)
        
    elif chart_type == "histogram":
        sns.histplot(data=df, x=y_axis, kde=True, ax=ax)
        
    ax.tick_params(axis='x', labelrotation=60)
    plt.tight_layout()
        
    return fig