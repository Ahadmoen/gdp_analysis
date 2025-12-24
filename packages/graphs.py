import matplotlib.pyplot as plt
import seaborn as sns


def histplot(x):
    histplot(x=x)


def boxplot(x):
    sns.boxplot(x=x, color='lightblue')


def violin(data, x, y, hue):
    sns.violinplot(
    data=data,
    y=x,
    x=y,
    hue=hue
)