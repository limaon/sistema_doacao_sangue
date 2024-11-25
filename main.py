import tkinter as tk
from gui.main_window import MainWindow
from pyswip import Prolog


def load_prolog():
    prolog = Prolog()
    prolog.consult("base_conhecimento.pl")
    return prolog


def main():
    prolog = load_prolog()
    app = MainWindow(prolog)
    app.mainloop()


if __name__ == "__main__":
    main()
