import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



def covid_time_series(df:pd.DataFrame): #Se especifica que el Dataframe es un objetivo de tipo pandas (pd)
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");

def plot_covid_latambars(df:pd.DataFrame):
    sns.barplot(
    data=df,
    x="value",
    y="country_region",
    palette=df.color
)

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");
