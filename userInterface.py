import Tkinter as tk
import main
import screenshot
mw = tk.Tk()
frame = tk.Frame(mw, width=200, height=100, background="bisque")
frame.pack(fill=None, expand=False)
result = ""
def buttonCall():
     result = main.runner()
     tk.Label(mw, text=result).pack()
goButton = tk.Button(mw, text="GO!",command=buttonCall)
goButton.pack()

mw.mainloop()