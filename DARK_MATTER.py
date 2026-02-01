

#Class DarkMeter:




    def __init__(self):
        self.dark_energy = 0

    def increase_dark_energy(self, amount):
        self.dark_energy += amount

    def decrease_dark_energy(self, amount):
        if self.dark_energy - amount >= 0:
            self.dark_energy -= amount
        else:
            self.dark_energy = 0

    def get_dark_energy(self):
        return self.dark_energy

