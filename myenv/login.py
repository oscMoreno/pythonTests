import customtkinter
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'


# Configuración del tema y la apariencia
customtkinter.set_appearance_mode('dark')  # Tema oscuro
customtkinter.set_default_color_theme('blue')  # Tema azul por defecto

# Crear ventana principal
root = customtkinter.CTk()
root.geometry('350x400')  # Aumentar tamaño para mostrar todos los widgets

def login():
    print('Bienvenido')  # Acción al presionar el botón

# Crear un frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill='both', expand=True)

# Etiqueta de título
label = customtkinter.CTkLabel(master=frame, text='Login', font=("Arial", 20))
label.pack(pady=12, padx=10)

# Campo de entrada para el nombre de usuario
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)

# Campo de entrada para la contraseña
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)

# Botón para iniciar sesión
button = customtkinter.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

# Iniciar la aplicación
root.mainloop()
