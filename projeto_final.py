# Situação 4

import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# conectar ou criar o banco 
def conectar():
    return sqlite3.connect('meu_banco_de_dados.db')

# criar tabela se ela não existir
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute(''' 
      CREATE TABLE IF NOT EXISTS usuarios(
             id INTEGER PRIMARY KEY,
             nome TEXT,
             peso INTEGER,   
             altura REAL            
        )
    ''')
    conn.commit()
    conn.close()

# inserindo dados no banco de dados
def agregar_usuarios():
    nome = entry_nome.get()
    peso = entry_peso.get()
    altura = entry_altura.get()


    if nome and peso and altura:
       conn = conectar()
       c = conn.cursor()
       c.execute('INSERT INTO usuarios(nome, peso, altura) VALUES(?, ?, ?)', (nome, peso, altura))
       conn.commit()
       conn.close()
       messagebox.showinfo('Resultado IMC', ) 
       mostrar_usuarios()
    else:
       messagebox.showerror('Erro', 'Ocorreu um erro, o IMC não foi calculado')

# mostrar dados 
def mostrar_usuarios():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * from usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1], usuario[2], usuario[3]))
    conn.close()

# deletar dados 
def eliminar_usuario():
    selected = tree.selection()
    if selected:
        user_id = tree.item(selected[0])['values'][0]
        conn = conectar() 
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Exito', 'DADOS DELETADOS')
        mostrar_usuarios()
    else:
        messagebox.showerror('Erro', 'Dados não deletados')

def atualizar_usuario():
    selected = tree.selection()
    if selected:
        user_id = tree.item(selected)['values'][0]
        novo_nome = entry_nome.get()
        novo_peso = entry_peso.get()
        nova_altura = entry_altura.get()
        if novo_nome and novo_peso and nova_altura:
            conn = conectar() 
            c = conn.cursor()
            c.execute('UPDATE usuarios SET nome = ?, peso = ?, altura = ? WHERE id = ?', 
                     (novo_nome, novo_peso, nova_altura, user_id)) 
            conn.commit()
            conn.close()
            messagebox.showinfo('Exito', 'Dados alterados')
            mostrar_usuarios()
        else:
            messagebox.showerror('Erro', 'Dados não inseridos')
    else:
        messagebox.showwarning('Atenção', 'O dado não foi selecionado')

janela = tk.Tk()
janela.title('Saúde & Bem-Estar')

label_nome = tk.Label(janela, text='NOME')
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_peso = tk.Label(janela, text='PESO')
label_peso.grid(row=1, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=1, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text='ALTURA')
label_altura.grid(row=2, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=2, column=1, padx=10, pady=10)

btn_agregar = tk.Button(janela, text='INSERIR DADOS', command=agregar_usuarios)
btn_agregar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text='ATUALIZAR DADOS', command=atualizar_usuario)
btn_atualizar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

btn_deletar = tk.Button(janela, text='DELETAR DADOS', command=eliminar_usuario)
btn_deletar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

columns = ('ID', 'NOME', 'PESO', 'ALTURA')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuarios()

janela.mainloop()
 