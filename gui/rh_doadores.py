import tkinter as tk
from tkinter import ttk, messagebox


class RhDoadores(ttk.Frame):
    def __init__(self, parent, prolog):
        super().__init__(parent)
        self.prolog = prolog
        self.create_widgets()

    def create_widgets(self):
        # Frame para selecionar tipo sanguíneo
        tipo_frame = ttk.LabelFrame(self, text="Tipo Sanguíneo")
        tipo_frame.pack(pady=10, padx=10, fill="x")

        tipo_label = ttk.Label(tipo_frame, text="Tipo Sanguíneo:")
        tipo_label.pack(side="left", padx=5, pady=5)

        self.tipo_var = tk.StringVar()
        tipos = ["a", "b", "ab", "o"]
        self.tipo_combobox = ttk.Combobox(
            tipo_frame, textvariable=self.tipo_var, values=tipos, state="readonly"
        )
        self.tipo_combobox.pack(side="left", padx=5, pady=5)
        self.tipo_combobox.current(0)

        buscar_tipo_btn = ttk.Button(
            tipo_frame, text="Buscar", command=self.buscar_por_tipo
        )
        buscar_tipo_btn.pack(side="left", padx=5, pady=5)

        # Frame para selecionar fator Rh
        rh_frame = ttk.LabelFrame(self, text="Fator Rh")
        rh_frame.pack(pady=10, padx=10, fill="x")

        rh_label = ttk.Label(rh_frame, text="Fator Rh:")
        rh_label.pack(side="left", padx=5, pady=5)

        self.rh_var = tk.StringVar()
        rh_fatores = ["+", "-"]
        self.rh_combobox = ttk.Combobox(
            rh_frame, textvariable=self.rh_var, values=rh_fatores, state="readonly"
        )
        self.rh_combobox.pack(side="left", padx=5, pady=5)
        self.rh_combobox.current(0)

        buscar_rh_btn = ttk.Button(rh_frame, text="Buscar", command=self.buscar_por_rh)
        buscar_rh_btn.pack(side="left", padx=5, pady=5)

        # Área para exibir resultados
        self.result_text = tk.Text(self, height=25, width=80)
        self.result_text.pack(pady=10)

    def buscar_por_tipo(self):
        tipo = self.tipo_var.get().lower()
        if not tipo:
            messagebox.showwarning(
                "Input Inválido", "Por favor, selecione um tipo sanguíneo."
            )
            return

        # Consulta Prolog: findall(Nome, doadores_com_tipo(Tipo, Nome), Nomes).
        try:
            consulta = f"findall(Nome, doadores_com_tipo({tipo}, Nome), Nomes)."
            resultados = list(self.prolog.query(consulta))
            nomes = resultados[0]["Nomes"]
            self.result_text.delete(1.0, tk.END)
            if nomes:
                self.result_text.insert(
                    tk.END, f"Pessoas com tipo sanguíneo {tipo.upper()}:\n"
                )
                for nome in nomes:
                    self.result_text.insert(tk.END, f"- {nome.capitalize()}\n")
            else:
                self.result_text.insert(
                    tk.END,
                    f"Nenhuma pessoa encontrada com tipo sanguíneo {tipo.upper()}.",
                )
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a consulta: {e}")

    def buscar_por_rh(self):
        rh = self.rh_var.get()
        if not rh:
            messagebox.showwarning(
                "Input Inválido", "Por favor, selecione um fator Rh."
            )
            return

        # Consulta Prolog: findall(Nome, doadores_com_rh(Rh, Nome), Nomes).
        try:
            consulta = f"findall(Nome, doadores_com_rh('{rh}', Nome), Nomes)."
            resultados = list(self.prolog.query(consulta))
            nomes = resultados[0]["Nomes"]
            self.result_text.delete(1.0, tk.END)
            if nomes:
                self.result_text.insert(tk.END, f"Pessoas com fator Rh {rh}:\n")
                for nome in nomes:
                    self.result_text.insert(tk.END, f"- {nome.capitalize()}\n")
            else:
                self.result_text.insert(
                    tk.END, f"Nenhuma pessoa encontrada com fator Rh {rh}."
                )
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a consulta: {e}")
