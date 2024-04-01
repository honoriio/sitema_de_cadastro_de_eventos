import tkinter as tk

class MinhaInterfaceGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("Minha Interface Gráfica")

        self.label = tk.Label(self.master, text="Olá, mundo!")
        self.label.pack()

def main():
    root = tk.Tk()
    app = MinhaInterfaceGrafica(root)
    root.mainloop()

if __name__ == "__main__":
    main()
