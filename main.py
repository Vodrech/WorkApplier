import Workflow.apply as apply
from Window import application
import tkinter as tk
import datetime
from os import path
import logging.config
from Log.Handlers import ApplyingHandler        # LoggingConfig

if __name__=='__main__':

    root = tk.Tk()
    app = application.Application(master=root)
    app.mainloop()

    # f = apply.ApplyingInterface()
    # f.apply_arbetsformedlningen()
