# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:19:40 2020

@author: khizer
"""

# -*- coding: utf-8 -*-
"""

"""
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import os
from spectral import *
from osgeo import gdal
import tifffile as tiff
from PIL import ImageTk,Image
import scipy.io
import PIL
###
global b1,b2,b3


#click command
#click command
def openfile():
    root.filename=filedialog.askopenfilename(initialdir='/',title="Select A File",filetypes=(("tif files","*.tif"),("hdr files","*.hdr"),("mat files","*.mat"),("all the files","*.*")))
    _, ext = os.path.splitext(root.filename)
    ext = ext.lower()
    if ext == '.mat':
        # Load Matlab array
        return scipy.io.loadmat(root.filename)
    elif ext == '.tif' or ext == '.tiff':
        # Load TIFF file
        return imageio.imread(root.filename)
    elif ext == '.hdr':
        img = open_image(root.filename)
        return img.load()
    else:
        raise ValueError("Unknown file format: {}".format(ext))
#    mat = scipy.io.loadmat(root.filename)
    mat.keys()
    data=mat['data']
    print(f'The size of the hypersepctral image is ')
    print(mat['data'].shape)        
    # return data
        
##
    
    
def get_lanfile():
    mat = scipy.io.loadmat(root.filename)
    mat.keys()
    data=mat['data']
    print(f'The size of the hypersepctral image is ')
    print(mat['data'].shape)
    return data
    
###
def bands():
    # new_window = Toplevel(root)
    # new_window.title("For Displaying the RGB Image")
    #
    my_notebook.add(my_frame1,text="Display RGB Image")


#
    new_window = Toplevel(root)
    new_window.title("For Displaying the RGB Image")
#    new_window.place(x=60, y=150)
#    Label(new_window, text ='For Displaying the RGB Image', font = "20",fg="red",anchor="center").grid(row=0)
    Label(new_window, text = "Select the First Band:").grid(row=1, column=0)
    Label(new_window, text = "Select the Second Band:").grid(row=2, column=0)
    Label(new_window, text = "Select the Third Band:").grid(row=3, column=0)

    num1 = Entry(new_window)
    num2 = Entry(new_window)
    num3 = Entry(new_window)

    num1.grid(row=1, column=1)
    num2.grid(row=2, column=1)
    num3.grid(row=3, column=1)
        
    # if num1 or num2 or num3 >get_lanfile().shape[2]:
    #     bands()
    bt1= Button(new_window, text='Quit',fg='red', command=new_window.destroy)
    bt1.grid(row=4, column=0, padx = 2, pady = 2)

    def retrieve_input():     
        b1 = int(num1.get())
        b2 = int(num2.get())
        b3= int(num3.get())
        new_window.destroy() 
        
        #
     #   new_window2 = Toplevel(root)    
    
    #
        lan_data=get_lanfile()
        save_rgb('rgb.jpg', lan_data, [b1, b2, b3])
        view_rgb=ImageTk.PhotoImage(Image.open('rgb.jpg') ) ##for displaying rgb image ##for displaying rgb image
    
        my_frame1.image = view_rgb
     
        Label(my_frame1, text='View RGB ', image=view_rgb).place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
     #   my_notebook.add(my_frame1, text='View RGB ', image=view_rgb,compound='right')

    
    bt2= Button(new_window, text='Show RGB Image',command=lambda: retrieve_input())
    bt2.grid(row=4, column=1,padx = 2, pady = 2)    
       


def anomoly():
    my_notebook.add(my_frame2,text="Anomoly Detection")
    data=get_lanfile()
    rximg = rx(data)
    # #save_rgb('rx.jpg', rximg)
    n_img=PIL.Image.fromarray(rximg, mode=None)
    view_rx=ImageTk.PhotoImage(n_img )
    my_frame2.image = view_rx
 
    Label(my_frame2, text='RX detector', image=view_rx).place(relx = 0.5, rely = 0.5, anchor = CENTER)

     #   my_notebook.add(my_frame1, text='View RGB ', image=view_rgb,compound='right')



def target():
    my_notebook.add(my_frame3,text="Target Detection")



# def rx():
#     data=get_lanfile
#     rximg = rx(data)

###
root=Tk()
root.title("iVison Target and Anomoly Detector")




my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New ",command=openfile)
file_menu.add_separator()
file_menu.add_command(label="Exit ",command=lambda: exit_gui())

###
run_menu=Menu(my_menu)
my_menu.add_cascade(label="Run ",menu=run_menu)
if os.path.isfile('./dc2.lan'):
    run_menu.add_command(label="Display RGB Image ", command=lambda: bands())
else:
    run_menu.add_command(label="Display RGB Image ",state=DISABLED)

run_menu.add_command(label="Anomoly Detection",command=lambda: anomoly())
run_menu.add_command(label="Target Detection ", command=lambda: target())


###Frame
my_notebook=ttk.Notebook(root)
my_notebook.pack(pady=15)
my_frame1=Frame(my_notebook,width=1200,height=1100)
my_frame2=Frame(my_notebook,width=1200,height=1100)

my_frame1.pack(fill="both",expand=1)
my_frame2.pack(fill="both",expand=1)

my_notebook.add(my_frame1,text="anomoly Detection ")
my_notebook.add(my_frame2,text="Target Detection ")
my_notebook.hide(0)
my_notebook.hide(1)


#my_notebook.mainloop()
root.mainloop()