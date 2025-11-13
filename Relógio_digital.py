import tkinter as tk #serve para criar interfaces gráficas
import time #time para trabalhar com data e hora

# Função que atualiza o horário a cada segundo
def atualizar_relogio(): #função para atualizar o relógio
    horario_atual = time.strftime("%H:%M:%S")  # Formato 24h (HH:MM:SS)
    label_horario.config(text=horario_atual) #atualiza o texto do label com o horário atual
    label_horario.after(1000, atualizar_relogio)  # Atualiza a cada 1000ms (1 segundo)

# Criando a janela principal
janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("300x150")
janela.config(bg="black")

# Texto principal (horário)
label_horario = tk.Label(
    janela,
    text="00:00:00", # Texto inicial do relógio
    font=("DS-Digital", 48, "bold"),  # Pode usar Arial, Impact, etc. se não tiver essa fonte
    fg="lime",
    bg="black"
)
label_horario.pack(expand=True)

# Texto do rodapé
label_data = tk.Label( #segunda label para data para aparecer no rodapé
    janela,
    text=time.strftime("%d/%m/%Y"),
    font=("Arial", 20),
    fg="white",
    bg="black"
)
label_data.pack() #posiciona a label no rodapé

# Iniciar atualização
atualizar_relogio() #atualiza o relógio chamando a função

# Loop principal da janela
janela.mainloop()