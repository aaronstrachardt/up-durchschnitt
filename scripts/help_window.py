import tkinter as tk

class HelpWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Hilfe")
        self.geometry("1000x420")
        self.resizable(False, False)
        self.help_widgets()

    def help_widgets(self):

        self.text = tk.Label(self, text="Was ist zu tun?", font=("Bahnschrift", 16), bg="#818BAC", fg="#f2f2f2")
        self.text.pack(pady=20,anchor="center")

        self.text1 = tk.Label(self, text="1. Melde dich bei PULS an", font=("Bahnschrift", 12), bg="#f2f2f2", fg="#000000")
        self.text1.pack(padx=50, pady=10,anchor="w")

        self.text2 = tk.Label(self, text="2. Gehe zur Leistungsübersicht", font=("Bahnschrift", 12), bg="#f2f2f2", fg="#000000")
        self.text2.pack(padx=50, pady=10,anchor="w")

        self.text3 = tk.Label(self, text="3. Speichere die Seite als .html-Datei (Strg+S)", font=("Bahnschrift", 12), bg="#f2f2f2", fg="#000000")
        self.text3.pack(padx=50, pady=10,anchor="w")

        self.text4 = tk.Label(self, text="4. Wähle im UP-Durchschnittsberechner deine .html-Datei aus", font=("Bahnschrift", 12), bg="#f2f2f2", fg="#000000")
        self.text4.pack(padx=50, pady=10,anchor="w")

        self.text5 = tk.Label(self, text="5. Klicke auf \"Berechnen\" und lass dir deinen aktuellen Durchschnitt ausgeben", font=("Bahnschrift", 12), bg="#f2f2f2", fg="#000000")
        self.text5.pack(padx=50, pady=10,anchor="w")





