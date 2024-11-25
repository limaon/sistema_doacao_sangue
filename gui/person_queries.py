import tkinter as tk
from tkinter import ttk, messagebox


class PersonQueries(ttk.Frame):
    def __init__(self, parent, prolog):
        super().__init__(parent)
        self.prolog = prolog
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry para o nome da pessoa
        pessoa_label = ttk.Label(self, text="Nome da Pessoa:")
        pessoa_label.pack(pady=10)

        self.pessoa_entry = ttk.Entry(self, width=30)
        self.pessoa_entry.pack(pady=5)

        # Botões para doar e receber
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(pady=10)

        doar_btn = ttk.Button(
            buttons_frame, text="Para Quem Pode Doar", command=self.para_quem_pode_doar
        )
        doar_btn.grid(row=0, column=0, padx=10)

        receber_btn = ttk.Button(
            buttons_frame,
            text="De Quem Pode Receber",
            command=self.de_quem_pode_receber,
        )
        receber_btn.grid(row=0, column=1, padx=10)

        # Área para exibir resultados
        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.pack(pady=10)

    def para_quem_pode_doar(self):
        pessoa = self.pessoa_entry.get().strip().lower()
        if not pessoa:
            messagebox.showwarning(
                "Input Inválido", "Por favor, insira o nome da pessoa."
            )
            return

        # Consulta Prolog: findall(Receptor, podedoar(Pessoa, Receptor), Receptores).
        try:
            resultados = list(
                self.prolog.query(
                    f"findall(Receptor, podedoar({pessoa}, Receptor), Receptores)."
                )
            )
            receptores = resultados[0]["Receptores"]
            self.result_text.delete(1.0, tk.END)
            if receptores:
                self.result_text.insert(
                    tk.END, f"{pessoa.capitalize()} pode doar para:\n"
                )
                for receptor in receptores:
                    self.result_text.insert(tk.END, f"- {receptor.capitalize()}\n")
            else:
                self.result_text.insert(
                    tk.END, f"{pessoa.capitalize()} NÃO pode doar para ninguém."
                )
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a consulta: {e}")

    def de_quem_pode_receber(self):
        pessoa = self.pessoa_entry.get().strip().lower()
        if not pessoa:
            messagebox.showwarning(
                "Input Inválido", "Por favor, insira o nome da pessoa."
            )
            return

        # Consulta Prolog: findall(Doador, podedoar(Doador, Pessoa), Doadores).
        try:
            resultados = list(
                self.prolog.query(
                    f"findall(Doador, podedoar(Doador, {pessoa}), Doadores)."
                )
            )
            doadores = resultados[0]["Doadores"]
            self.result_text.delete(1.0, tk.END)
            if doadores:
                self.result_text.insert(
                    tk.END, f"{pessoa.capitalize()} pode receber de:\n"
                )
                for doador in doadores:
                    self.result_text.insert(tk.END, f"- {doador.capitalize()}\n")
            else:
                self.result_text.insert(
                    tk.END, f"{pessoa.capitalize()} NÃO pode receber de ninguém."
                )
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a consulta: {e}")
