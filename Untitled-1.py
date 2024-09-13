import tkinter as tk
import random
import threading

# Luo tkinter-pääikkuna
window = tk.Tk()
window.title("Ernestin ja Kernestin 100m juoksu")

# Asetetaan lähtö ja maaliviiva
canvas = tk.Canvas(window, width=600, height=300)
canvas.pack()

# Lähtöviiva ja maaliviiva
canvas.create_line(50, 100, 50, 150, fill="black", width=5)  # Ernestin viiva
canvas.create_line(50, 200, 50, 250, fill="black", width=5)  # Kernestin viiva
canvas.create_line(550, 100, 550, 150, fill="black", width=5)
canvas.create_line(550, 200, 550, 250, fill="black", width=5)

# Tekstit
canvas.create_text(50, 80, text="Ernesti - Lähtö", font=('Helvetica', 12))
canvas.create_text(550, 80, text="Ernesti - Maali", font=('Helvetica', 12))
canvas.create_text(50, 180, text="Kernesti - Lähtö", font=('Helvetica', 12))
canvas.create_text(550, 180, text="Kernesti - Maali", font=('Helvetica', 12))

# Ernestin ja Kernestin hahmot
ernesti = canvas.create_oval(30, 110, 50, 130, fill="blue")  # Ernestin ympyrä
kernesti = canvas.create_oval(30, 210, 50, 230, fill="red")  # Kernestin ympyrä

# Tuloslabel
result_label = tk.Label(window, text="", font=('Helvetica', 14))
result_label.pack()

# Aikaleimat ja seuranta
ernesti_time = 0
kernesti_time = 0
ernesti_finished = False
kernesti_finished = False

def check_winner():
    """Tarkistaa, ovatko molemmat maalissa, ja näyttää voittajan."""
    if ernesti_finished and kernesti_finished:
        if ernesti_time < kernesti_time:
            result_text = f"Ernesti voitti ajalla {ernesti_time:.2f}s!\nKernestin aika: {kernesti_time:.2f}s."
        else:
            result_text = f"Kernesti voitti ajalla {kernesti_time:.2f}s!\nErnestin aika: {ernesti_time:.2f}s."
        result_label.config(text=result_text)

def ernesti_juoksee(nykyinen_x=30):
    global ernesti_time, ernesti_finished
    if nykyinen_x < 550:
        if ernesti_time == 0:
            ernesti_time = random.uniform(9.5, 10.5)  # Satunnainen juoksuaika
        askel_pituus = 500 / ernesti_time
        nykyinen_x += askel_pituus
        canvas.move(ernesti, askel_pituus, 0)
        canvas.update()
        window.after(1000, ernesti_juoksee, nykyinen_x)
    else:
        ernesti_finished = True
        check_winner()

def kernesti_juoksee(nykyinen_x=30):
    global kernesti_time, kernesti_finished
    if nykyinen_x < 550:
        if kernesti_time == 0:
            kernesti_time = random.uniform(10.0, 11.0)  # Satunnainen juoksuaika
        askel_pituus = 500 / kernesti_time
        nykyinen_x += askel_pituus
        canvas.move(kernesti, askel_pituus, 0)
        canvas.update()
        window.after(1000, kernesti_juoksee, nykyinen_x)
    else:
        kernesti_finished = True
        check_winner()

def yhteislahto():
    global ernesti_time, kernesti_time, ernesti_finished, kernesti_finished
    ernesti_time = 0
    kernesti_time = 0
    ernesti_finished = False
    kernesti_finished = False
    result_label.config(text="")  # Tyhjennä aiemmat tulokset

    # Käynnistetään Ernestin ja Kernestin juoksut yhtä aikaa ilman estettä
    threading.Thread(target=ernesti_juoksee).start()
    threading.Thread(target=kernesti_juoksee).start()

# Painikkeet Ernestin ja Kernestin juoksulle sekä yhteislähdölle
ernesti_button = tk.Button(window, text="Aloita Ernestin juoksu!", command=ernesti_juoksee)
ernesti_button.pack()

kernesti_button = tk.Button(window, text="Aloita Kernestin juoksu!", command=kernesti_juoksee)
kernesti_button.pack()

yhteislahto_button = tk.Button(window, text="Yhteislähtö", command=yhteislahto)
yhteislahto_button.pack()

# Käynnistetään pääsilmukka
window.mainloop()