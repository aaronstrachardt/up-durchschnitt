import tkinter as tk
from tkinter import filedialog
import ctypes
import help_window as help_window

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("UP Durchschnitt")
        self.master.resizable(False, False)
        self.master.geometry("1400x420")
        self.master.configure(bg="#f2f2f2")
        self.bg_color="white"
        self.create_widgets()

    def create_widgets(self):
        self.buttons=[]

        self.text = tk.Label(self.master, text="Willkommen  zum (in)offiziellen UP Durchschnittsberechner", font=("Bahnschrift", 16), bg="#f2f2f2", fg="#000000")
        self.text.place(relx=0.5,y=70,anchor="center")

        self.file_label = tk.Label(self.master, text="Wähle bitte eine .html-Datei oder .txt-Datei aus", font=("Bahnschrift", 12), bg="#818BAC", fg="#f2f2f2")
        self.file_label.place(relx=0.5,y=140,anchor="center")

        self.choose_file_button = tk.Button(self.master, text="Datei auswählen", command=self.choose_file, bg="#00305E", fg="#f2f2f2", font=("Bahnschrift", 12))
        self.choose_file_button.place(relx=0.5,y=210,anchor="center")
        self.buttons.append(self.choose_file_button)

        self.calculate_button = tk.Button(self.master, text="Berechnen", command=self.calculate, bg="#00305E", fg="#f2f2f2", font=("Bahnschrift", 12))
        self.calculate_button.place(relx=0.5,y=280,anchor="center")
        self.buttons.append(self.calculate_button)

        self.result_label = tk.Label(self.master, text="", font=("Bahnschrift", 12), bg="#f2f2f2")
        self.result_label.place(relx=0.5,y=350,anchor="center")

        self.menu_button = tk.Button(self.master, text="Help", command=self.open_help_window, bg="#00305E", fg="#f2f2f2", font=("Bahnschrift", 12))
        self.menu_button.place(x=15,y=15)
        self.buttons.append(self.menu_button)

        self.dark_mode_button = tk.Button(self.master, text="Dark", command=self.change_mode ,bg="#00305E", fg="#f2f2f2", font=("Bahnschrift", 12))
        self.dark_mode_button.place(x=15,y=355)
        self.buttons.append(self.dark_mode_button)

    def change_mode(self):
        if self.bg_color == "white":
            self.master.configure(bg="#313338")
            self.text.configure(fg="#F2F3F5", bg="#313338")
            self.result_label.configure(fg="#F2F3F5", bg="#313338")
            self.dark_mode_button.configure(text="Light")

            for button in self.buttons:
                button.configure(fg="#F2F3F5",bg="#41434A")

            self.bg_color = "black"

        else:
            self.master.configure(bg="#f2f2f2")
            self.text.configure(fg="#000000", bg="#f2f2f2")
            self.result_label.configure(fg="#000000", bg="#f2f2f2")
            self.dark_mode_button.configure(text="Dark")

            for button in self.buttons:
                button.configure(fg="#f2f2f2",bg="#00305E")

            self.bg_color = "white"

    def open_help_window(self):
        help_window.HelpWindow()

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.configure(text=file_path)

    def calculate(self):
        file_path = self.file_label.cget("text")
        try:
            file = open(file_path)
            lines = file.readlines()
            file.close()
        except FileNotFoundError:
            self.result_label.configure(text="Datei nicht gefunden")
            return
        except:
            self.result_label.configure(text="Fehler beim Lesen der Datei")
            return

        main_list = []

        for count, line in enumerate(lines):
            modul = []
            if '<td colspan="6" class="puls_moduleFach" style="padding-left:' in line:
                mark = lines[count + 5].strip(" </td>rLP\n\t").replace(",", ".")
                credits = lines[count + 9].strip(" </td>rLP\n\t")
                if mark == "" or credits == "":
                    continue
                modul.append(float(mark))
                modul.append(float(credits))
                main_list.append(modul)

        if len(main_list) == 0:
            self.result_label.configure(text="Keine Module gefunden")
            return

        mark_sum = 0
        credits_sum = 0

        for element in main_list:
            mark_sum += element[0] * element[1]
            credits_sum += element[1]

        avg = mark_sum / credits_sum

        self.result_label.configure(text=f"Deine aktuelle Durchschnittsnote: {avg:.2f}")

root = tk.Tk()
app = MainWindow(master=root)
app.mainloop()
