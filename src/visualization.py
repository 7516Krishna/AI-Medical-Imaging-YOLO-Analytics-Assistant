import matplotlib.pyplot as plt

def plot_bar(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Prediction Distribution")
    return fig

def plot_pie(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Prediction Ratio")
    return fig

def plot_line(values):
    fig, ax = plt.subplots()
    ax.plot(values)
    ax.set_title("Confidence Trend")
    return fig