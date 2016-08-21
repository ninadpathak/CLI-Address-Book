#!/usr/bin/python3
import tkinter

main_window = tkinter.Tk() 
z
messageL = tkinter.Label(main_window, text="Hello World", padx = 50, pady = 50)
stop_button = tkinter.Button(main_window , text = "Stop", command = main_window.destroy, padx = 40, marginx = 20)
messageL.pack()
stop_button.pack()

main_window.title("Address Book")
main_window.mainloop() # Keeps the window open
