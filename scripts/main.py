import tkinter as tk
from tkinter import filedialog
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("UP Durchschnitt")
        self.master.resizable(False, False)
        self.master.geometry("1000x350")
        self.master.configure(bg="#f2f2f2")
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Label(self.master, text="Willkommen  zum (in)offiziellen UP Durchschnittsberechner", font=("Bahnschrift", 16), bg="#f2f2f2", fg="#000000")
        self.text.pack(pady=20)

        self.file_label = tk.Label(self.master, text="Wähle bitte eine .html-Datei oder .txt-Datei aus", font=("Bahnschrift", 12), bg="#818BAC", fg="#f2f2f2")
        self.file_label.pack(pady=10)

        self.choose_file_button = tk.Button(self.master, text="Datei auswählen", command=self.choose_file, bg="#00305E", fg="white", font=("Bahnschrift", 12))
        self.choose_file_button.pack(pady=10)

        self.calculate_button = tk.Button(self.master, text="Berechnen", command=self.calculate, bg="#00305E", fg="white", font=("Bahnschrift", 12))
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=("Bahnschrift", 12), bg="#f2f2f2")
        self.result_label.pack(pady=10)

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