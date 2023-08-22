import requests
import tkinter as tk
from tkinter import PhotoImage
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

        # Cambiar tamaño al mover el mouse
        self.root.bind('<B1-Motion>', self.resize_gadget)

        # Cambiar color de fondo al hacer clic derecho
        self.root.bind('<Button-3>', self.change_bg_color)

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

    def resize_gadget(self, event):
        new_width = event.x_root - self.root.winfo_x()
        new_height = event.y_root - self.root.winfo_y()
        self.root.geometry(f'{new_width}x{new_height}')

    def change_bg_color(self, event):
        colors = ['#ffffff', '#f0f0f0', '#e0e0e0']  # Agrega más colores si deseas
        current_color = self.ip_frame.cget('bg')
        next_color = colors[(colors.index(current_color) + 1) % len(colors)]
        self.ip_frame.config(bg=next_color)

if __name__ == '__main__':
    root = tk.Tk()
    app = GadgetApp(root)
    root.mainloop()
