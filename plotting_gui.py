#%% plotting gui.py
# plotting gui.py
from tkinter import *
import pandas as pd
from matplotlib import pyplot as plt

# %%
# gui functions
def read_data(filename = "Data.csv"):
    data = pd.read_csv(filename, sep = "\t")
    return data

def plot_data(dataframe, default_x = "X", default_y = "Y"):
    data.plot(x = default_x, y = default_y)
    return

def gen_sample_data():
    datalist = [[1,1],[2,2],[3,4],[4,8],[5,16]]
    dataframe = pd.DataFrame(datalist)
    dataframe.columns = ["X","Y"]
    dataframe.to_csv("Data.csv", sep = "\t")
    return dataframe

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.title = "Data Loader"

        self.pack(fill = BOTH, expand = 1)
        exit_button = Button(self, text = "Exit", command = self.click_exit_button)
        exit_button.place(x = 0, y = 0)
        
        data_load_button = Button(self, text = "Load Data", command = self.click_load_data)
        data_load_button.place(x = 0, y = 30)
        
        sample_data_button = Button(self, text = "Generate Sample Data", command = self.click_sample_data)
        sample_data_button.place(x = 0, y = 60)
        
        plot_data_button = Button(self, text = "Plot DataFrame", command = self.click_plot_data)
        plot_data_button.place(x = 0, y = 90)

    def click_exit_button(self):
        exit()
        
    def click_load_data(self):
        data = read_data
        return data
        
    def click_sample_data(self):
        data = gen_sample_data
        return data
        
    def click_plot_data(self):
        plot_data

# %%
root = Tk()
app = Window(root)
root.wm_title("Tkinter Button")
root.geometry("320x200")
root.mainloop()

# %%
# execute gui code
root = Tk()
app = Window(root)
root.wm_title("Tkinter Button")
root.geometry("320x200")
root.mainloop()