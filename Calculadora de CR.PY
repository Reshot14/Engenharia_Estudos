import tkinter as tk
from tkinter import ttk, messagebox

# Lista completa de disciplinas com créditos
DISCIPLINAS = [
    'ECOLOGIA GERAL (60)',
    'FUNDAMENTOS DE CÁLCULO E GEOMETRIA (60)',
    'CÁLCULO 1 (60)',
    'QUÍMICA GERAL TECNOLÓGICA (75)',
    'PROGRAMAÇÃO DE COMPUTADORES (60)',
    'INTRODUÇÃO À ENGENHARIA DE TELECOMUNICAÇÕES (30)',
    'FÍSICA I (68)',
    'FÍSICA EXPERIMENTAL I (30)',
    'CÁLCULO 2 (60)',
    'ESTRUTURAS DE DADOS (60)',
    'FUNDAMENTOS DE DESENHO TÉCNICO II (60)',
    'DESENHO UNIVERSAL PARA APLICAÇÕES WEB (60)',
    'ESTATÍSTICA BÁSICA (60)',
    'FÍSICA II (68)',
    'FÍSICA EXPERIMENTAL II (30)',
    'CÁLCULO 3 (60)',
    'CÁLCULO 4 (60)',
    'PROGRAMAÇÃO ORIENTADA A OBJETOS (68)',
    'REDES LOCAIS E DE ACESSO (60)',
    'CIRCUITOS DIGITAIS 1 (60)',
    'FÍSICA III (68)',
    'FÍSICA EXPERIMENTAL III (30)',
    'MÉTODOS MATEMÁTICOS APLICADOS À ENGENHARIA DE TELECOMUNICAÇÕES (60)',
    'ELETROMAGNETISMO I: CAMPOS ESTÁTICOS (60)',
    'MODELOS PROBABILÍSTICOS EM ENGENHARIA DE TELECOMUNICAÇÕES (60)',
    'INTERCONEXÃO DE REDES I (60)',
    'CIRCUITOS ELÉTRICOS NO DOMÍNIO DO TEMPO I (60)',
    'FÍSICA EXPERIMENTAL IV (30)',
    'FÍSICA IV (68)',
    'MÉTODOS NUMÉRICOS (60)',
    'ÉTICA, CIDADANIA E LEGISLAÇÃO (30)',
    'INTERCONEXÃO DE REDES II (60)',
    'ELETROMAGNETISMO II: CAMPOS VARIÁVEIS (60)',
    'SINAIS E SISTEMAS I (60)',
    'CIRCUITOS ELÉTRICOS NO DOMÍNIO DA FREQUÊNCIA I (60)',
    'ATIVIDADE DE EXTENSÃO I (60)',
    'SINAIS E SISTEMAS II (60)',
    'PROPAGAÇÃO EM GUIAS DE ONDA (60)',
    'PROPAGAÇÃO E ANTENAS (60)',
    'LABORATÓRIO DE REDES (60)',
    'TELEFONIA FIXA E ASPECTOS REGULATÓRIOS (60)',
    'ELETRÔNICA ANALÓGICA 1 (60)',
    'FUNDAMENTOS DE PROCESSAMENTO DIGITAL DE SINAIS I (60)',
    'ATIVIDADE DE EXTENSÃO II (60)',
    'SISTEMAS DE TRANSMISSÃO E RADIOENLACE (60)',
    'DISPOSITIVOS FOTÔNICOS (30)',
    'TEORIA DA INFORMAÇÃO E CÓDIGOS (60)',
    'SISTEMAS DE RADIODIFUSÃO (60)',
    'FUNDAMENTOS DE SISTEMAS MÓVEIS (60)',
    'ELETRÔNICA ANALÓGICA 2 (60)',
    'ESTÁGIO CURRICULAR OBRIGATÓRIO (160)',
    'SISTEMA DE COMUNICAÇÃO VIA SATÉLITE (60)',
    'SEGURANÇA DE REDES (60)',
    'ARQUITETURA E SISTEMAS DE COMPUTAÇÃO PARA TELECOMUNICAÇÕES (60)',
    'SISTEMAS DE COMUNICAÇÕES ÓTICAS (60)',
    'DISPOSITIVOS PASSIVOS DE MICRO-ONDAS (60)',
    'PROJETO DE EXTENSÃO (60)',
    'PROJETO DE ELETRÔNICA I (60)',
    'METODOLOGIA CIENTÍFICA APLICADA À ENGENHARIA DE TELECOMUNICAÇÕES (30)',
    'GERÊNCIA DE REDES E ENGENHARIA DE TRÁFEGO (60)',
    'APLICAÇÕES EM REDES (60)',
    'REDES MULTIMÍDIA (60)',
    'ANTENAS PARA ALTAS FREQUÊNCIAS E CONJUNTOS (60)',
    'MEDIÇÕES EM ÓTICA E RADIOFREQUÊNCIA (60)',
    'SISTEMAS DE COMUNICAÇÕES DE ÚLTIMA GERAÇÃO (60)',
    'PROJETO DE ELETRÔNICA II (60)',
    'PROJETO FINAL DE CURSO 1 (15)',
    'ADMINISTRAÇÃO APLICADA À ENGENHARIA (60)',
    'ECONOMIA APLICADA À ENGENHARIA (60)',
    'PROJETO FINAL DE CURSO 2 (15)',
]

class CalculadoraCR:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de CR")
        self.root.geometry("500x500")  # Define a geometria da janela

        # Define a cor de fundo para preto
        self.root.configure(bg="black")

        # Centraliza a janela na tela
        self.center_window()

        self.frame_entrada = tk.Frame(root, bg="black")
        self.frame_entrada.pack(pady=20)

        self.label_entrada_notas = tk.Label(self.frame_entrada, text="Número de matérias:", bg="black", fg="lime green", font=("Helvetica", 14))
        self.label_entrada_notas.grid(row=0, column=0, padx=10)

        self.entry_notas_entry = tk.Entry(self.frame_entrada, font=("Helvetica", 12, "bold"), justify="center")  # Centraliza o texto
        self.entry_notas_entry.grid(row=0, column=1, padx=10)

        self.botao_criar_lista = tk.Button(self.frame_entrada, text="Criar Lista", command=self.criar_lista_materias, bg="lime green", fg="black", font=("Helvetica", 12))
        self.botao_criar_lista.grid(row=0, column=2, padx=10)

        self.frame_materias = tk.Frame(root, bg="black")
        self.frame_materias.pack(pady=20)

        self.lista_combos = []
        self.entry_notas = {}

        # Adicionando label para mostrar o resultado do CR
        self.label_resultado_cr = tk.Label(root, text="", bg="black", fg="lime green", font=("Helvetica", 16))
        self.label_resultado_cr.pack(pady=20)

    def center_window(self):
        # Obtém a largura e a altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcula as coordenadas x e y para centralizar a janela
        x = (screen_width - 500) // 2
        y = (screen_height - 300) // 2

        # Define a geometria da janela para centralizá-la
        self.root.geometry(f"500x200+{x}+{y}")

    def criar_lista_materias(self):
        notas_entry = self.entry_notas_entry.get()

        # Verificar se a entrada é um número inteiro positivo
        if notas_entry.isdigit() and int(notas_entry) > 0:
            notas = int(notas_entry)
            if notas > 7:
                messagebox.showwarning("Aviso", f"Só é possível calcular até 7 matérias por vez!")
                return
        else:
            messagebox.showwarning("Aviso", "Insira um número inteiro positivo válido para o número de matérias.")
            return

        self.limpar_frame(self.frame_materias)

        self.lista_combos = []
        self.entry_notas = {}

        for i in range(1, notas + 1):
            label = tk.Label(self.frame_materias, text=f"Matéria {i}:", bg="black", fg="lime green", font=("Helvetica", 12))
            label.grid(row=i, column=0, pady=5, padx=5, sticky="e")

            combo = ttk.Combobox(self.frame_materias, values=DISCIPLINAS, state="readonly")
            combo.grid(row=i, column=1, pady=5, padx=5, sticky="w")

            entry_label = tk.Label(self.frame_materias, text="Nota:", bg="black", fg="lime green", font=("Helvetica", 12))
            entry_label.grid(row=i, column=2, pady=5, padx=5, sticky="e")

            entry = StyledEntry(self.frame_materias, font=("Helvetica", 12, "bold"), justify="center")  # Centraliza o texto
            entry.grid(row=i, column=3, pady=5, padx=5, sticky="w")

            # Adicionar combo e entrada ao dicionário
            self.lista_combos.append(combo)
            self.entry_notas[combo] = entry

        botao_calcular_cr = tk.Button(self.frame_materias, text="Calcular CR", command=self.calcular_cr, bg="lime green", fg="black", font=("Helvetica", 14))
        botao_calcular_cr.grid(row=notas + 1, column=0, columnspan=4, pady=10)

    def limpar_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def calcular_cr(self):
        try:
            lista_escolhida = []
            lista_notas = []
            lista_pesos = []

            for combo in self.lista_combos:
                materia_selecionada = combo.get()
                nota = self.entry_notas[combo].get()

                if nota == "":
                    messagebox.showwarning("Aviso", "Insira todas as notas antes de calcular o CR.")
                    return

                peso_materia = int(materia_selecionada.split("(")[-1].split(")")[0])  # Extrai o peso da disciplina
                lista_escolhida.append(materia_selecionada)
                lista_notas.append(float(nota))
                lista_pesos.append(peso_materia)

            resultado_final = 0.0

            if lista_notas and lista_escolhida:
                # Calculando o total de créditos ponderados
                total_creditos_ponderados = sum(nota * peso for nota, peso in zip(lista_notas, lista_pesos))

                # Calculando o total de créditos
                total_creditos = sum(lista_pesos)

                # Calculando o CR
                resultado_final = total_creditos_ponderados / total_creditos

                self.label_resultado_cr.config(text=f"O CR é: {resultado_final:.2f}")

            else:
                messagebox.showwarning("Aviso", "Insira pelo menos uma matéria e suas notas.")

        except ValueError:
            messagebox.showwarning("Aviso", "Certifique-se de inserir notas válidas.")

class StyledEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(justify="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCR(root)
    root.mainloop()
