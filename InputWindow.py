import tkinter as tk

# GUI input window
class InputWindow:
    def __init__(self):
        self.values = []
        self.root = tk.Tk()
        self.root.title("Virus Spread Game")
        self.root.geometry("400x200")

        self.entries = {}
        self.build_ui()
        self.root.mainloop()

    def build_ui(self):
        labels = ['Movement Rate', 'Transmission Rate', 'Illness Length', 'Lethality']
        defaults = ['5', '5', '5', '5']

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        for i, (label, default) in enumerate(zip(labels, defaults)):
            tk.Label(frame, text=f'{label}:').grid(row=i, column=0)
            entry = tk.Entry(frame)
            entry.insert(0, default)
            entry.grid(row=i, column=1)
            self.entries[label] = entry

        self.error = tk.Label(self.root, text="", fg='red')
        self.error.pack()

        tk.Button(self.root, text="Start Simulation", command=self.validate).pack(pady=10)

    def validate(self):
        self.values.clear()
        for label, entry in self.entries.items():
            val = entry.get()
            if not val.isdigit() or not (1 <= int(val) <= 10):
                self.error.config(text=f"Invalid {label}")
                return
            self.values.append(int(val))

        self.root.destroy()

    def get_values(self):
        return self.values