import random
import string
from tkinter import Tk, Label, Entry, Button, END
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha

def crear_Captcha(flag=0):
    """Definiendo el método crear_Captcha() que creará
    y generar una imagen de Captcha basada en un azar
    cadenas generadas."""
    global cadena_random
    global imagen_label
    global imagen_display
    global entry
    global verificacion_label
    global ventana

    """El bloque IF a continuación solo funciona cuando presionamos el botón
    Botón Recargar en la interfaz. Básicamente elimina la etiqueta (si está visible) que muestra si el
    cadena ingresada es correcta o incorrecta."""
    if flag == 1:
        verificacion_label.grid_forget()

    # Remover el contenido del input box.
    entry.delete(0,END)

    # Generar una cadena aleatoria para el Captcha
    cadena_random = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Crear imagen Captcha
    imagen_captcha = ImageCaptcha(width=250, height=125)
    imagen_generada = imagen_captcha.generate(cadena_random)
    imagen_display = ImageTk.PhotoImage(Image.open(imagen_generada))

    # Remover la anterior imagen y mostrar la nueva
    imagen_label.grid_forget()
    imagen_label = Label(ventana, image=imagen_display)
    imagen_label.grid(row=1, column=0, columnspan=2, padx=10)


def check(x, y):
    """Definiendo el método check() que verificará si la cadena ingresada por el usuario coincide con la cadena generada aleatoriamente. 
    Si hay una coincidencia y luego aparece "CAPTCHA CORRECTO!" en la ventana.
    De lo contrario, "CAPTCHA INCORRECTO!" aparece y aparece un nuevo Captcha se genera una imagen para que 
    el usuario vuelva a intentarlo."""

    global verificacion_label

    verificacion_label.grid_forget()

    if x.lower() == y.lower():
        verificacion_label = Label(master=ventana,text="CAPTCHA CORRECTO!",font="Arial 15",bg='#ffe75c',fg="#00a806")
        verificacion_label.grid(row=0, column=0, columnspan=2, pady=10)
        boton_cerrar = Button(ventana, text="Cerrar", font="Arial 10", command=ventana.destroy)
        boton_cerrar.grid(row=3, column=1, columnspan=3, pady=12)
    else:
        verificacion_label = Label(master=ventana,text="CAPTCHA INCORRECTO!",font="Arial 15",bg='#ffe75c',fg="#fa0800")
        verificacion_label.grid(row=0, column=0, columnspan=2, pady=10)
        crear_Captcha()

#if __name__ == "__main__":
    # Inicializamos Tkinter y creamos una ventana

ventana = Tk()
ventana.title('Imagen Captcha')
ventana.configure(background='#2B2DB4')

verificacion_label = Label(ventana)
imagen_label = Label(ventana)

# Definimos el Input Box y lo ponemos en la ventana
entry = Entry(ventana, width=10, borderwidth=5,font="Arial 15", justify="center")
entry.grid(row=2, column=0)
# Creamos la imagen Captcha.
crear_Captcha()

    # Ruta de la imagen de recarga
ruta_img = 'Archivos/recargar.png'
recargar_imagen = ImageTk.PhotoImage(Image.open(ruta_img).resize((32, 32), Image.ANTIALIAS))
recargar_boton = Button(image=recargar_imagen, command=lambda: crear_Captcha(1))
recargar_boton.grid(row=2, column=1, pady=10)

    # Creamos el boton de Aceptar
boton_aceptar = Button(ventana, text="Aceptar", font="Arial 10", command=lambda: check(entry.get(), cadena_random))
boton_aceptar.grid(row=3, column=0, columnspan=2, pady=10)
ventana.bind('<Return>', func=lambda Event: check(entry.get(), cadena_random))
ventana.mainloop()

