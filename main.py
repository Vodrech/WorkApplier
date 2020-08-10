import Workflow.apply as apply
from Window import application
import tkinter as tk

# LoggingConfig
# from Log.Handlers import ApplyingHandler


if __name__=='__main__':

    root = tk.Tk()
    app = application.Application(master=root)
    app.mainloop()
