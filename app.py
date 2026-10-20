import os
import tkinter as tk
from tkinter import messagebox, ttk
from models import*

CURRENT_USER=None
ENTRY_LOGIN=None

BG="#f9f1e5"
FIELD_BG="#ffffff"
FIELD_FG="#22262b"

FONT_TITLE=("Arial", 16,"bold")
FONT_LABEL=("Arial", 11,"bold")
FONT_BUTTON=("Arial", 12,"bold")

root=tk.Tk()
root.geometry("720x640")
root.configure(bg=BG)

container=tk.Frame(root, bg=BG)
container.pack(fill="both", expand=True, padx=20,pady=20)

def clear_screen():
    for w in container.winfo_children():
        w.destroy()

def make_title(text):
    return tk.Label(container, text=text, bg=BG, fg=FIELD_FG, font=FONT_TITLE).pack(pady=(0,15))  

def make_label(text):
    return tk.Label(container, text=text, bg=BG, fg=FIELD_FG, font=FONT_LABEL).pack(fill="x")        

def make_entry(password=False):
    entry=tk.Entry(container, font=FONT_BUTTON, bg=BG,fg=FIELD_FG, insertbackground=FIELD_FG, relief="solid", borderwidth=1) 
    if password:
        entry.configure(show="*")
    return entry     

def make_button(text,command, parent=None):
    host= container if parent is None else parent
    return tk.Button(host, text=text, command=command, font=FONT_BUTTON) 

def try_login(login, password):
    global CURRENT_USER
    login=login.strip()
    password=password.strip()
    if not login or not password:
        messagebox.showwarning("Внимание","Заполните логин и пароль")
        return
    user=find_user(login,password)  
    if user is None:
        messagebox.showerror("Ошибка","Вы ввели неверный логин или пароль")
        return
    CURRENT_USER=user
    messagebox.showinfo("Вы успешно авторизовались")  
    if user['role']=="Администратор":
        open_admin()
    else:
        open_user()

def open_login():
    clear_screen()
    make_title("Вход в систему")

    make_label("Логин")
    entry_login=make_entry()
    entry_login.pack(fill="x",pady=(0,8)) 
    make_label("Пароль")  
    entry_pass=make_entry()
    entry_pass.pack(fill="x", pady=(0,4)) 
    make_button("Войти", lambda: try_login(entry_login.get(), entry_pass.get())).pack(fill="x", ipady=6) 

def open_admin():
    clear_screen()
    make_title("Окно администратора")
    make_label(f"Вы вошли как: {CURRENT_USER['login']}").pack(pady=(0,6))
    make_button("Выйти", open_login).pack(ipadx=24,ipady=4)

def open_user():
    clear_screen()
    make_title("Рабочее место пользователя")
    make_label(f"Вы вошли как: {CURRENT_USER['login']}").pack(pady=(0,6))
    make_label(f"Роль: {CURRENT_USER['role']}").pack(pady=(0,10))
    make_button("Выйти", open_login)
      
open_login()
root.mainloop()