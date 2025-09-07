import tkinter as tk
from tkinter import messagebox, scrolledtext
from functions import ToolkitSuporte, Relatorio

# Interface Tkinter
root = tk.Tk()
root.title("Console de Suporte Técnico")
root.geometry("500x400")
root.configure(bg="#1e1e2e")

fonte = ("Segoe UI", 10)

# Título
titulo = tk.Label(root, text="Console de Suporte Técnico", bg="#1e1e2e", fg="#00ffff", font=("Segoe UI", 16, "bold"))
titulo.pack(pady=15)

# Frame com botões
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=10)

botoes = [
    ("Verificar IP", ToolkitSuporte.verificar_ip),
    ("Testar Ping", ToolkitSuporte.testar_ping),
    ("Limpar Temporários", ToolkitSuporte.limpar_temporarios),
    ("Otimizar Disco", ToolkitSuporte.otimizar_unidades),
    ("Limpar Unidades", ToolkitSuporte.executar_cleanmgr),
    ("Abrir UpdateManager", ToolkitSuporte.abrir_update_manager),
    ("Ver Relatório", Relatorio.abrir_ultimo_log),
    ("Sair", root.destroy)
]

for i, (texto, comando) in enumerate(botoes):
    btn = tk.Button(frame, text=texto, command=comando, width=25, height=2, bg="#2e2e3e", fg="#ffffff", font=fonte)
    btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)

# Rodapé
status = tk.Label(root, text="Desenvolvido por Thiago Camargo", bg="#1e1e2e", fg="#aaaaaa", font=("Segoe UI", 8))
status.pack(side="bottom", pady=5)

root.mainloop()
