import math
import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

BIRTHSTONES = {
    1: ("#781244", "Garnet"),
    2: ("#9966CC", "Amethyst"),
    3: ("#7FFFD4", "Aquamarine"),
    4: ("#FFFFFF", "Diamond"),
    5: ("#50C878", "Emerald"),
    6: ("#F0F8FF", "Pearl"),
    7: ("#E0115F", "Ruby"),
    8: ("#E6E200", "Peridot"),
    9: ("#0F52BA", "Sapphire"),
    10: ("#A8C3BC", "Opal"),
    11: ("#FFC87C", "Topaz"),
    12: ("#40E0D0", "Turquoise")
}

# ... [All the previous color calculation functions remain the same] ...

def generate_astrological_colors(birthday):
    # ... [The generate_astrological_colors function remains the same] ...

class AstrologicalColorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Astrological Color Generator")
        master.geometry("400x500")

        self.label = tk.Label(master, text="Select your birthday:")
        self.label.pack(pady=10)

        self.cal = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.cal.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generate Colors", command=self.generate_colors)
        self.generate_button.pack(pady=10)

        self.birthstone_label = tk.Label(master, text="")
        self.birthstone_label.pack(pady=5)

        self.sun_frame = tk.Frame(master, width=300, height=50)
        self.sun_frame.pack(pady=5)
        self.sun_label = tk.Label(master, text="")
        self.sun_label.pack()

        self.moon_frame = tk.Frame(master, width=300, height=50)
        self.moon_frame.pack(pady=5)
        self.moon_label = tk.Label(master, text="")
        self.moon_label.pack()

        self.rising_frame = tk.Frame(master, width=300, height=50)
        self.rising_frame.pack(pady=5)
        self.rising_label = tk.Label(master, text="")
        self.rising_label.pack()

    def generate_colors(self):
        birthday = self.cal.get_date().strftime("%m/%d/%Y")
        sun, moon, rising, birthstone = generate_astrological_colors(birthday)

        self.birthstone_label.config(text=f"Birthstone: {birthstone}")

        self.sun_frame.config(bg=sun)
        self.sun_label.config(text=f"Sun color: {sun}")

        self.moon_frame.config(bg=moon)
        self.moon_label.config(text=f"Moon color: {moon}")

        self.rising_frame.config(bg=rising)
        self.rising_label.config(text=f"Rising color: {rising}")

def main():
    root = tk.Tk()
    app = AstrologicalColorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
