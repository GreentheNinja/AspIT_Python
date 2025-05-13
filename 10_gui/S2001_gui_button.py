"""Vores første GUI: kun én knap i ét vindue.

Kør programmet.
Find ud af, hvad hver række kode gør. For eksempel ved at ændre koden en smule og køre den igen.
Læs alle kommentarerne.
Tag et kort kig på de linkede dokumentationer. Du vil få brug for dem i fremtidige øvelser.
Se youtube-videoen (link i kommentarerne)."""

import tkinter as tk  # import the GUI library

# Define the main window, its title text and its size
# These first 3 lines are typically roughly the same in every tkinter GUI
main_window = tk.Tk()  # create the main window
main_window.title("A GUI Most Foul")  # text shown in the top window bar
main_window.geometry("500x500")  # window size

# Create a button
# You can find all possible options of tk.Button() in the following documentations:
# https://tkdocs.com/shipman/button.html
# https://www.tutorialspoint.com/python/tk_button.htm#
button_1 = tk.Button(
    main_window,
    text = "My",
    anchor = "center"
)
button_2 = tk.Button(
    main_window,
    text = "compass",
    anchor = "center"
)
button_3 = tk.Button(
    main_window,
    text = "was",
    anchor = "center"
)
button_4 = tk.Button(
    main_window,
    text = "swallowed",
    anchor = "center"
)
button_5 = tk.Button(
    main_window,
    text = "by",
    anchor = "center"
)
button_6 = tk.Button(
    main_window,
    text = "the",
    anchor = "center"
)
button_7 = tk.Button(
    main_window,
    text = "sea",
    anchor = "center"
)

# Define where the button is positioned
# Watch this video from 1:48 till 7:03 to understand positioning in tkinter:
# https://www.youtube.com/watch?v=BSfbjrqIw20&t=108s
# You can find all possible options of grid() in the following documentations:
# https://tkdocs.com/shipman/grid.html
# https://www.tutorialspoint.com/python/tk_grid.htm
button_1.grid(row = 0, column = 2, sticky = tk.E)
button_2.grid(row = 1, column = 1, sticky = tk.W)
button_3.grid(row = 2, column = 0, sticky = tk.E)
button_4.grid(row = 3, column = 1, ipadx = 10, ipady = 10)
button_5.grid(row = 4, column = 2, ipadx = 50, ipady = 20)
button_6.grid(row = 5, column = 3, ipadx = 50, ipady = 20)
button_7.grid(row = 6, column = 2, ipadx = 50, ipady = 20)

# main program
if __name__ == "__main__":  # Executed only when this file is run.
    main_window.mainloop()  # Wait for button clicks and act upon them
