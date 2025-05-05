from Disease import Disease
from Simulation import Simulation
from InputWindow import InputWindow
from Person import Person

# Main entry point
def main():
    input_window = InputWindow()
    params = input_window.get_values()
    if len(params) != 4:
        print("Simulation canceled.")
        return

    disease = Disease(*params)
    Simulation(disease)

if __name__ == "__main__":
    main()
