import tkinter as tk  # Graafilise liidese loomise importimine
import math  # Ruutjuure lisamise jaoks importidud math funktsioon

class Calculator:
    def __init__(self, root):
        self.root = root  # Määrame akna, kus kalkulaator asub
        self.root.geometry("300x275")  # Määrame akna suuruse
        self.calculation = ""  # Muutuja arvutuste jaoks
        self.create_widgets()  # Ekraani ja nupu loomise meetod

    def create_widgets(self):
        # Loome tekstiakna, kus kuvatakse arvutused
        self.text_result = tk.Text(self.root, height=2, width=16, font=("Times New Roman", 24))
        self.text_result.grid(columnspan=5)  # Teksti aken esimesel real, laiendatult 5 realiseks

        # Nuppude loend: (nupu tekst, rida, veerg)
        buttons = [
            ('1', 2, 1), ('2', 2, 2), ('3', 2, 3),
            ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
            ('7', 4, 1), ('8', 4, 2), ('9', 4, 3),
            ('0', 5, 2), ('+', 3, 4), ('-', 4, 4),
            ('*', 5, 4), ('/', 6, 4), ('(', 5, 1),
            (')', 5, 3), ('=', 6, 2), ('C', 2, 4),
            ('^', 6, 1), ('√', 6, 3)  # Astendamine ja ruutjuur, on ka lisatud sulud. Ruutjuur ja Sulud on minu kaks lisatud funktsiooni
        ]

        # Loome iga numbri ja märgi jaoks eraldi nupu
        for (text, row, col) in buttons:
            if text == '=':  # Kui nupu tekst on '=', siis see hindab avaldist
                button = tk.Button(self.root, text=text, command=self.evaluate_calculation, width=5, font=("Times New Roman", 14))
            elif text == 'C':  # Kui nupu tekst on 'C', siis see tühjendab ekraani
                button = tk.Button(self.root, text=text, command=self.clear_field, width=5, font=("Times New Roman", 14))
            elif text == '^':  # Kui nupu tekst on '^', siis see lisab astendamise märgi, mis pythonis on ** ja siis ise lisad numbri kui kõrgele astendada tahad
                button = tk.Button(self.root, text=text, command=lambda: self.add_to_calculation("**"), width=5, font=("Times New Roman", 14))
            elif text == '√':  # Kui nupu tekst on '√', siis see arvutab ruutjuure
                button = tk.Button(self.root, text=text, command=self.calculate_square_root, width=5, font=("Times New Roman", 14))
            else:  # Kõik muud nupud lisavad oma teksti arvutusse
                button = tk.Button(self.root, text=text, command=lambda t=text: self.add_to_calculation(t), width=5, font=("Times New Roman", 14))
            button.grid(row=row, column=col)  # Paigutame nupu õigesse ritta ja veergu

    def add_to_calculation(self, symbol):
        # Lisame sümboli arvutusse ja uuendame ekraani
        self.calculation += str(symbol)
        self.text_result.delete(1.0, "end")  # Tühjendame ekraani
        self.text_result.insert(1.0, self.calculation)  # Kuvame uuendatud arvutuse

    def evaluate_calculation(self):
        # Kontrollib kas saab teha tehte ja kuvab tulemuse või veateate
        try:
            self.calculation = str(eval(self.calculation))  # Kasutame eval() arvutuse hindamiseks
            self.text_result.delete(1.0, "end")  # Tühjendame ekraani
            self.text_result.insert(1.0, self.calculation)  # Kuvame tulemuse
        except:
            self.clear_field()  # Kui arvutus ebaõnnestub, tühjendame ekraani
            self.text_result.insert(1.0, "Error")  # Kuvame veateate

    def clear_field(self):
        # Tühjendame arvutuse ja ekraani
        self.calculation = ""
        self.text_result.delete(1.0, "end")

    def calculate_square_root(self):
        # Arvutame ruutjuure
        try:
            result = math.sqrt(float(eval(self.calculation)))  # Hindame avaldise ja arvutame ruutjuure
            self.calculation = str(result)  # Uuendame arvutust
            self.text_result.delete(1.0, "end")  # Tühjendame ekraani
            self.text_result.insert(1.0, self.calculation)  # Kuvame tulemuse
        except:
            self.clear_field()  # Kui arvutus ebaõnnestub, tühjendame ekraani
            self.text_result.insert(1.0, "Error")  # Kuvame veateate

if __name__ == "__main__":
    root = tk.Tk()  # Loome peamise tkinter akna
    calc = Calculator(root)  # Loome kalkulaatori objekti
    root.mainloop()  # Käivitame rakenduse põhitsükli