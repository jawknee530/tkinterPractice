try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480+80+400')
mainWindow['padx'] = 8

# set up col and row weights
for i in range(0, 5):
    mainWindow.columnconfigure(i, weight=1)

for i in range(0, 7):
    mainWindow.rowconfigure(i, weight=1)


result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky='nsew')

cButton = tkinter.Button(mainWindow, text="C")
cButton.grid(row=1, column=0, sticky='nsew')
ceButton = tkinter.Button(mainWindow, text="CE")
ceButton.grid(row=1, column=1, sticky='nsew')

buttonList = ['7', '8', '9', '+', '4', '5', '6', '-',
              '1', '2', '3', '*', '0', '=', '/']
index = 0
for i in range(2, 6):
    for j in range(0, 4):
        if index < len(buttonList):
            tkinter.Button(mainWindow, text=buttonList[index]).grid(row=i, column=j, sticky='nsew')
            index += 1









mainWindow.mainloop()