from tkinter import *
import tkinter as tk
import random

disease_stats = []

def main():
    user_input()
    simulation(disease_stats)

def user_input():
    # this function creates the User Interface allowing for input
    # and saves it to a list available globaly

    root = tk.Tk()
    root.geometry("400x200")
    root.title('Virus Spread Game')

    intro = tk.Label(root, text='Enter any integer 1-10')
    intro.pack(pady=10)

    frame = tk.Frame(root)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    movement_label = tk.Label(frame, text='Movement Rate:  ')
    movement_label.grid(row=0, column=0)
    movement_rate = tk.Entry(frame)
    movement_rate.insert(0, '5')
    movement_rate.grid(row=0, column=1)

    Transmission_label = tk.Label(frame, text='Transmission Rate:  ')
    Transmission_label.grid(row=1, column=0)
    Transmission_rate = tk.Entry(frame)
    Transmission_rate.insert(0, '5')
    Transmission_rate.grid(row=1, column=1)

    length_label = tk.Label(frame, text='Illness Length: ')
    length_label.grid(row=3, column=0)
    illness_length = tk.Entry(frame)
    illness_length.insert(0, '5')
    illness_length.grid(row=3, column=1)

    lethality_label = tk.Label(frame, text='Lethality: ')
    lethality_label.grid(row=4, column=0)
    lethality = tk.Entry(frame)
    lethality.insert(0, '5')
    lethality.grid(row=4, column=1)

    frame.pack()

    def validate():
        disease_stats.clear()
        count = 0

        v1 = movement_rate.get()
        v2 = Transmission_rate.get()
        v3 = illness_length.get()
        v4 = lethality.get()

        disease = [v1, v2, v3, v4]
        errors = ['invalid movement rate', \
                 'invalid transmission rate', \
                 'invalid illness length', \
                 'invalid lethality']

        print()

        for item in disease:
            count += 1
            if item.isdigit():
                if int(item) >= 1 and int(item) <= 10:
                    disease_stats.append(int(item))
                    if len(disease_stats) == 4:
                        print('Saved')
                        root.destroy()
                else:
                    error.config(text=errors[count - 1])
            else:
                error.config(text=errors[count - 1])
        

    enter_btn = tk.Button(root, text='save and run', command=validate)
    enter_btn.pack(pady=10)

    error = tk.Label(root, text='')
    error.pack()

    root.mainloop()
    
    
def simulation(disease):
    # saves the users inputs to be used in the simulation
    # checking if there are 5 digits saved

    if len(disease) != 4:
        print('Input not saved')
    else:
        MOVEMENT_INDEX = 0
        TRANSMISSION_INDEX = 1
        ILLNESS_LENGTH_INDEX  = 2
        LETHALITY_INDEX = 3

        # Define the parameters for the people
        movement_speed = disease[MOVEMENT_INDEX]
        transmission_rate = disease[TRANSMISSION_INDEX]
        illness_length = disease[ILLNESS_LENGTH_INDEX]
        lethality = disease[LETHALITY_INDEX]
        people = 100
        color = 'red'
    
        # creates the simulation
        root = tk.Tk()
        root.geometry("1280x720")
        root.title('Virus Spread Simulation')
        root.resizable(False, False)

        c = Canvas(root, width=1280, height=720)
        c.pack()

        circles = []

        # Create the people
        for _ in range(people):
            x = random.randint(10, 1270)
            y = random.randint(10, 710)
            dx = random.choice([-1, 1]) * movement_speed
            dy = random.choice([-1, 1]) * movement_speed
            circle = c.create_oval(x - 10, y - 10, x + 10, y + 10, fill=color)
            color = 'white'
            circles.append((circle, x, y, dx, dy))

        # Moves people
        def move_circles():
            for i, (circle, x, y, dx, dy) in enumerate(circles):
                x += dx
                y += dy
                if x - 10 < 0 or x + 10 > 1280:
                    dx *= -1
                if y - 10 < 0 or y + 10 > 720:
                    dy *= -1

                # Deals with the collisions of people
                for j, (other_circle, other_x, other_y, _, _) in enumerate(circles):
                    if i != j:
                        distance = ((x - other_x) ** 2 + (y - other_y) ** 2) ** 0.5
                        if distance <= 15:
                            dx *= -1
                            dy *= -1

                            # logic behind spreading the disease
                            if c.itemcget(circle, 'fill') == 'red' or c.itemcget(other_circle, 'fill') == 'red':
                                    if c.itemcget(circle, 'fill') != 'black' and c.itemcget(other_circle, 'fill') != 'black':
                                        if c.itemcget(circle, 'fill') != 'blue' and c.itemcget(other_circle, 'fill') != 'blue':
                                            if random.random() < transmission_rate / 10:
                                                c.itemconfig(circle, fill='red')
                                                c.itemconfig(other_circle, fill='red')

                            # logic behind recovering or dying to disease
                            if c.itemcget(circle, 'fill') == 'red':
                                if random.random() < lethality / 100:
                                    c.itemconfig(circle, fill='black')
                                if random.random() < illness_length / 100:
                                    c.itemconfig(circle, fill='blue')
                            if c.itemcget(other_circle, 'fill') == 'red':
                                if random.random() < lethality / 100:
                                    c.itemconfig(other_circle, fill='black')
                                if random.random() < illness_length / 100:
                                    c.itemconfig(other_circle, fill='blue')

                c.move(circle, dx, dy)
                circles[i] = (circle, x, y, dx, dy)

            c.after(20, move_circles)

        move_circles()
        root.mainloop()
    

if __name__ == '__main__':
    main()