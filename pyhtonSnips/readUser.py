

import hjson
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

#this class finaly static
class fromUser():

    @classmethod # could be static method
    def load_data(cls):
        cls.refresh_hjson()
        cls.refresh_filename("file1")
        cls.refresh_xydata()

        
    #will return each part at one time, no need to store extra stuff
    @classmethod
    def get_sect(cls,sect):
        if sect == "all":
            return cls.hjson_data
            
        # do a check here for missing data
        else: 
            return cls.hjson_data[sect]

    @classmethod
    def get_data(cls,dataArr):
        if dataArr == "x_data": return cls.x_data
        elif dataArr == "y_data": return cls.y_data

    @classmethod
    def refresh_hjson(cls):
        cls.hjson_data = cls.hjson_fromFile()

    @classmethod
    def refresh_xydata(cls):
        #this one needs editing
        cls.x_data, cls.y_data = cls.xydata_fromFile(cls.filename,cls.get_sect("file_data")["xdata"][1]-1,cls.get_sect("file_data")["ydata"][1]-1)

    @classmethod #this method is pointless, thus change varable itself
    def refresh_filename(cls,filename):
        cls.filename = filename

    @staticmethod
    def hjson_fromFile():
        with open("user.hjson",'r') as hjsonText:
            user_data = hjson.loads(hjsonText.read())
            return user_data

    @staticmethod # don't remeber what a_dict is
    def hjson_ToFile(a_dict,sect):
        pass


    @staticmethod
    def xydata_fromFile(file_name,xcol,ycol):
        time = []
        signal =[]
        with open(file_name ,'r') as reader:
            for row in reader:
                signal.append(round(float(row.split()[xcol]),2))
                time.append(round(float(row.split()[ycol]),2))

        return (time, signal)



    @staticmethod # this one needs editing so it won't crash
    def choose_file():
        #return "file1"
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        print(file_path)
        #dirname = tkinter.filedialog.askdirectory(parent=root, initialdir="/",title='Please select a directory')
        return file_path