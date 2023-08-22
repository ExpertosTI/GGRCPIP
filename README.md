# Gadget RCPIP - RENACE

Bienvenido al proyecto Gadget RCPIP, desarrollado por la Empresa RENACE. Este es un pequeño gadget de escritorio que muestra la dirección IP pública y permite copiarla al portapapeles. Además, ofrece la capacidad de mover y redimensionar el gadget según tus preferencias.

## Características Principales

- Muestra la dirección IP pública obtenida a través de la API de ipify.
- Permite copiar la dirección IP al portapapeles con un clic.
- Puedes mover el gadget manteniendo presionado el botón izquierdo del mouse.
- Puedes redimensionar el gadget manteniendo presionado el botón izquierdo del mouse y moviendo el cursor.
- Al hacer clic derecho en el gadget, se muestra un menú contextual con las opciones de mover, redimensionar y salir.

## Requisitos

- Python 3 (se recomienda la versión 3.6 o superior).
- Las siguientes bibliotecas de Python:
  - `requests`
  - `tkinter`
  - `PIL` (Pillow)

## Instrucciones de Uso

1. Abre una terminal y navega a la ubicación del archivo `gadget.py`.
2. Ejecuta el comando `python gadget.py`.
3. El gadget se abrirá en una ventana de tkinter.
4. Para moverlo, mantén presionado el botón izquierdo del mouse y arrástralo.
5. Para redimensionarlo, mantén presionado el botón izquierdo del mouse y mueve el cursor.
6. Haz clic derecho en el gadget para abrir el menú contextual y elige la acción deseada.
7. Puedes cerrar el gadget haciendo doble clic sobre él.

## Crear Ejecutable

Si deseas crear un ejecutable para Windows, puedes utilizar la herramienta PyInstaller. Ejecuta el siguiente comando en la terminal:

