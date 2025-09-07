import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import subprocess
import socket
import datetime

class ToolkitSuporte:
    # Funções de ação do Toolkit
    def verificar_ip():
        try:
            nome_maquina = socket.gethostname()
            ip_local = socket.gethostbyname(nome_maquina)
            Relatorio.salvar_log(f"IP Local: {ip_local}")
            messagebox.showinfo("IP Local", f"IP da máquina: {ip_local}")
        except Exception as e:
            Relatorio.salvar_log(f"Erro ao verificar IP: {e}")
            messagebox.showerror("Erro", f"Erro ao verificar IP: {e}")

    def testar_ping():
        resposta = os.system("ping www.google.com")
        if resposta == 0:
            Relatorio.salvar_log("Ping bem-sucedido.")
            messagebox.showinfo("Ping", "Conectado à internet!")
        else:
            Relatorio.salvar_log("Falha no ping.")
            messagebox.showwarning("Ping", "Sem conexão com a internet.")

    def limpar_temporarios():
        try:
            os.system("del /q /s %temp%\\*")
            Relatorio.salvar_log("Arquivos temporários limpos.")
            messagebox.showinfo("Limpeza", "Arquivos temporários removidos com sucesso.")
        except Exception as e:
            Relatorio.salvar_log(f"Erro na limpeza: {e}")
            messagebox.showerror("Erro", f"Erro ao limpar: {e}")

    def otimizar_unidades():
        try:
            subprocess.run(["dfrgui"], shell=True)
            Relatorio.salvar_log("Ferramenta de Otimização de Unidades aberta.")
            messagebox.showinfo("Otimização", "Ferramenta de Otimização de Disco aberta.")
        except Exception as e:
            Relatorio.salvar_log(f"Erro ao abrir Otimizador de Disco: {e}")
            messagebox.showerror("Erro", f"Erro ao abrir o Otimizador: {e}")      

    def executar_cleanmgr():
        try:
            subprocess.Popen("cleanmgr")
            Relatorio.salvar_log("Cleanmgr aberto com sucesso. Usuário pode escolher o disco.")
        except Exception as e:
            Relatorio.salvar_log(f"Erro ao abrir o Cleanmgr: {e}")

    def abrir_update_manager():
        try:
            subprocess.run(["control", "/name", "Microsoft.WindowsUpdate"], shell=True)
            Relatorio.salvar_log("Update Manager aberto.")
        except Exception as e:
            Relatorio.salvar_log(f"Erro ao abrir o Update Manager: {e}")


class Relatorio:
    # Caminho para salvar os logs do relatório
    LOG_DIR = "relatorios"
    os.makedirs(LOG_DIR, exist_ok=True)

    def salvar_log(texto):
        data = datetime.datetime.now().strftime("%Y-%m-%d")
        arquivo = os.path.join(Relatorio.LOG_DIR, f"logs_{data}.txt")
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {texto}\n")

    def abrir_ultimo_log():
        try:
            data = datetime.datetime.now().strftime("%Y-%m-%d")
            arquivo = os.path.join(Relatorio.LOG_DIR, f"logs_{data}.txt")
            if not os.path.exists(arquivo):
                messagebox.showinfo("Relatório", "Nenhum log encontrado para hoje.")
                return

            with open(arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()

            janela_log = tk.Toplevel()
            janela_log.title("Relatório Técnico")
            janela_log.geometry("600x400")
            janela_log.configure(bg="#1e1e2e")

            txt = scrolledtext.ScrolledText(janela_log, wrap=tk.WORD, bg="#2e2e3e", fg="white", font=("Consolas", 10))
            txt.insert(tk.END, conteudo)
            txt.pack(expand=True, fill="both", padx=10, pady=10)
            txt.configure(state="disabled")

        except Exception as e:
            Relatorio.salvar_log(f"Erro ao abrir relatório: {e}")
            messagebox.showerror("Erro", f"Erro ao abrir relatório: {e}")
