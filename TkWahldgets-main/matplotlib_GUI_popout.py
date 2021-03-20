from tkinter import * 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
import numpy as np
import matplotlib.pyplot as plt
  
# plot function is created for plotting the graph in tkinter window 
root = Tk()
root.geometry("300x300") 
def plot(): 
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices)
    plt.show()

plot_button = Button(root, command = plot, height = 2, width = 10, text = "Plot")
plot_button.pack()
root.mainloop()