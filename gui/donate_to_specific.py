import tkinter as tk
from tkinter import ttk, messagebox


class DonateToSpecific(ttk.Frame):
    def __init__(self, parent, prolog):
        super().__init__(parent)
        self.prolog = prolog
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry para o nome do receptor
        receptor_label = ttk.Label(self, text="Nome do Receptor:")
        receptor_label.pack(pady=10)

        self.receptor_entry = ttk.Entry(self, width=30)
        self.receptor_entry.pack(pady=5)

        # Botão para realizar a consulta
        consultar_btn = ttk.Button(self, text="Consultar", command=self.consultar)
        consultar_btn.pack(pady=10)

        # Área para exibir resultados
        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.pack(pady=10)

    def consultar(self):
        receptor = self.receptor_entry.get().strip().lower()
        if not receptor:
            messagebox.showwarning(
                "Input Inválido", "Por favor, insira o nome do receptor."
            )
            return

        # Consulta Prolog: findall(Doador, podedoar(Doador, Receptor), Doadores).
        consulta = f"findall(Doador, podedoar(Doador, {receptor}), Doadores)."
        try:
            self.prolog.assertz(f"receptor({receptor}).")
            self.prolog.query(
                f"findall(Doador, podedoar(Doador, {receptor}), Doadores)."
            )
            resultados = list(
                self.prolog.query(
                    f"findall(Doador, podedoar(Doador, {receptor}), Doadores)."
                )
            )
            doadores = resultados[0]["Doadores"]
            self.result_text.delete(1.0, tk.END)
            if doadores:
                self.result_text.insert(
                    tk.END, f"Doadores aptos para {receptor.capitalize()}:\n"
                )
                for doador in doadores:
                    self.result_text.insert(tk.END, f"- {doador.capitalize()}\n")
            else:
                self.result_text.insert(
                    tk.END,
                    f"Nenhum doador apto encontrado para {receptor.capitalize()}.",
                )
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a consulta: {e}")
