import requests
import tkinter as tk
from tkinter import PhotoImage, Menu
from PIL import Image, ImageTk

class GadgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title('RCPIP')
        self.root.overrideredirect(True)  # Sin bordes y barra de título
        self.root.geometry('200x150')  # Tamaño inicial

        self.bg_image = Image.open('background.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.pack(fill='both', expand=True)

        self.ip_frame = tk.Frame(self.root, bg='#ffffff', bd=5)
        self.ip_frame.pack(pady=20)

        self.font_title = ('Montserrat', 14, 'bold')
        self.title_label = tk.Label(self.ip_frame, text='RCPIP', bg='#ffffff', font=self.font_title)
        self.title_label.pack()

        self.font_style = ('Lato', 12)

        self.ip_value = tk.Label(self.ip_frame, text='', bg='#ffffff', font=self.font_style)
        self.ip_value.pack()

        self.copy_button = tk.Button(self.ip_frame, text='Copiar al Portapapeles', bg='#66ccff', fg='white', font=('Helvetica', 10), command=self.copy_ip)
        self.copy_button.pack(pady=5)

        # Variable para contar los clics
        self.click_count = 0

        # Deshabilitar el botón de cerrar
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)

        # Evento de doble clic para cerrar
        self.root.bind('<Double-1>', self.close_gadget)

        # Cambiar tamaño al mover el mouse (clic izquierdo)
        self.root.bind('<Button-1>', self.start_action)
        self.root.bind('<B1-Motion>', self.perform_action)
        self.root.bind('<ButtonRelease-1>', self.stop_action)

        # Agregar menú contextual
        self.root.bind('<Button-3>', self.show_context_menu)

        # Variable para determinar la acción actual
        self.action = None

        # Variables para guardar la posición y tamaño antes de la acción
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        # Obtener y mostrar la IP pública
        self.update_ip()

    def update_ip(self):
        try:
            response = requests.get('https://api64.ipify.org?format=json')
            data = response.json()
            self.ip_value.config(text=data['ip'])
        except Exception as e:
            self.ip_value.config(text=str(e))

    def copy_ip(self):
        ip = self.ip_value.cget('text')
        self.root.clipboard_clear()
        self.root.clipboard_append(ip)
        self.root.update()

    def close_gadget(self, event):
        self.click_count += 1
        if self.click_count >= 2:
            self.root.destroy()

    def start_action(self, event):
        self.x = event.x
        self.y = event.y

    def perform_action(self, event):
        if self.action == 'move':
            deltax = event.x - self.x
            deltay = event.y - self.y
            new_x = self.root.winfo_x() + deltax
            new_y = self.root.winfo_y() + deltay
            self.root.geometry(f'+{new_x}+{new_y}')
        elif self.action == 'resize':
            delta_width = event.x - self.x
            delta_height = event.y - self.y
            new_width = self.width + delta_width
            new_height = self.height + delta_height
            self.root.geometry(f'{new_width}x{new_height}')

    def stop_action(self, event):
        self.action = None

    def show_context_menu(self, event):
        menu = Menu(self.root, tearoff=0)
        menu.add_command(label="Mover", command=lambda: self.set_action('move'))
        menu.add_command(label="Redimensionar", command=lambda: self.set_action('resize'))
        menu.add_separator()
        menu.add_command(label="Salir", command=self.root.destroy)
        menu.post(event.x_root, event.y_root)

    def set_action(self, action):
        self.action = action
        self.x = self.root.winfo_pointerx()
        self.y = self.root.winfo_pointery()
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()

if __name__ == '__main__':
    root = tk.Tk()
    app = GadgetApp(root)
    root.mainloop()
