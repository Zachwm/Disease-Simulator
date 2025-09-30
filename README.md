# Disease Spread Simulator

This was a fun project I built to learn how to create a GUI using `tkinter`, and to explore basic simulation logic. The program simulates the spread of a disease through a population of moving individuals, using parameters like movement speed, transmission rate, illness duration, and lethality.

## Features

- Graphical user interface for input
- Simple physics-based simulation using `Canvas`
- Visual feedback: healthy, infected, recovered, and dead individuals
- Randomized interactions and outcomes based on user-defined disease properties

## How It Works

1. The program starts with a GUI that lets you enter the following values (range 1–10):
   - **Movement Rate**: how fast individuals move
   - **Transmission Rate**: how easily the disease spreads
   - **Illness Length**: chance of recovery per frame
   - **Lethality**: chance of death per frame

2. Once values are submitted, the simulation starts:
   - 100 individuals move randomly around the canvas.
   - On collision, disease may spread based on the transmission rate.
   - Infected individuals can either recover (turn blue) or die (turn black) depending on the other two settings.

## Requirements

- Python 3
