""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk

def validate_id(message: str = "") -> bool:
    if message == "":
        return True
    if not message.isnumeric():
        return False
    return len(message) <= 8

window = tk.Tk()
window.title("Hello GUIs")
window.geometry("200x150")

container = tk.LabelFrame(window, text = "Container")
container.pack(expand = True, fill = "both", padx = 10, pady = 5)
container.grid_rowconfigure(0, weight = 4)
# container.grid_rowconfigure(1, weight = 1)
container.grid_rowconfigure(2, weight = 6)
container.grid_columnconfigure(0, weight = 1)

id_label = tk.Label(container, text = "ID", justify = "center", width = 0)
id_label.grid(row = 0, column = 0, sticky = tk.S)

id_field = tk.Entry(container, width = 10, justify = "center", validate = "key", validatecommand = (window.register(validate_id), "%P"))
id_field.grid(row = 1, column = 0, pady = 5)

submit_button = tk.Button(container, text = "Submit", command = window.destroy)
submit_button.grid(row = 2, column = 0, sticky = tk.N)


if __name__ == '__main__':
    window.mainloop()
