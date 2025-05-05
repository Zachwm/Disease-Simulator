from Person import Person

import tkinter as tk
import random

# Simulation controller
class Simulation:
    def __init__(self, disease, num_people=100):
        self.disease = disease
        self.people = []
        self.root = tk.Tk()
        self.root.title('Virus Spread Simulation')
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(self.root, width=1280, height=720)
        self.canvas.pack()

        self.setup_people(num_people)
        self.move_people()

        self.root.mainloop()

    def setup_people(self, count):
        for i in range(count):
            x = random.randint(10, 1270)
            y = random.randint(10, 710)
            dx = random.choice([-1, 1]) * self.disease.movement
            dy = random.choice([-1, 1]) * self.disease.movement
            infected = (i == 0)
            person = Person(self.canvas, x, y, dx, dy, infected)
            self.people.append(person)

    def move_people(self):
        for person in self.people:
            person.move()

        self.handle_collisions()
        self.root.after(20, self.move_people)

    def handle_collisions(self):
        for i, p1 in enumerate(self.people):
            for j, p2 in enumerate(self.people):
                if i >= j:
                    continue

                dist = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
                if dist <= Person.RADIUS * 1.5:
                    self.process_interaction(p1, p2)

    def process_interaction(self, p1, p2):
        color1 = p1.get_color()
        color2 = p2.get_color()

        infectious_states = ['red']
        susceptible_states = ['white']

        for p in (p1, p2):
            if p.get_color() == 'red':
                if random.random() < self.disease.lethality / 100:
                    p.update_color('black')
                elif random.random() < self.disease.illness_length / 100:
                    p.update_color('blue')

        # Spread infection
        if (
            (color1 in infectious_states and color2 in susceptible_states) or
            (color2 in infectious_states and color1 in susceptible_states)
        ):
            if random.random() < self.disease.transmission / 10:
                if color1 == 'white':
                    p1.update_color('red')
                if color2 == 'white':
                    p2.update_color('red')
