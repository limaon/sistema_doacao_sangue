import tkinter as tk
from tkinter import ttk
from gui.donate_to_specific import DonateToSpecific
from gui.person_queries import PersonQueries
from gui.rh_doadores import RhDoadores


class MainWindow(tk.Tk):
    def __init__(self, prolog):
        super().__init__()
        self.title("Sistema Especialista de Doação de Sangue")
        self.geometry("800x600")
        self.prolog = prolog

        # Configurar o notebook (abas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Adicionar abas
        self.donate_to_specific = DonateToSpecific(self.notebook, self.prolog)
        self.person_queries = PersonQueries(self.notebook, self.prolog)
        self.rh_doadores = RhDoadores(self.notebook, self.prolog)

        self.notebook.add(self.donate_to_specific, text="Doar para Específico")
        self.notebook.add(self.person_queries, text="Consultas de Pessoa")
        self.notebook.add(self.rh_doadores, text="Doadores por Fator Rh")
