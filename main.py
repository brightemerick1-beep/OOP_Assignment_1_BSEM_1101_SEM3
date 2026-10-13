"""
Livestock Health & Tracking System
PROG211 - Object-Oriented Programming 1
Domain: Agriculture

DPG alignment: open-source, simple text interface (accessible),
no personal/sensitive data stored (only animal data), modular and reusable.
"""


class Animal:
    """Represents one animal on a farm."""

    # Tuple: fixed set of allowed health statuses (immutable)
    VALID_STATUSES = ("Healthy", "Sick", "Under Treatment", "Recovered")

    total_animals = 0  # class attribute shared by all Animal objects

    def __init__(self, animal_id, species, age_months, status="Healthy"):
        self.animal_id = animal_id
        self.species = species
        self.age_months = age_months
        self.status = status
        self.vaccinations = []  # list of (vaccine_name, date) tuples
        Animal.total_animals += 1

    # ---------- Instance methods ----------
    def update_record(self, new_status):
        """Update the health status of this animal."""
        if new_status in Animal.VALID_STATUSES:
            self.status = new_status
            print(f"  {self.animal_id} status updated to '{new_status}'.")
        else:
            print(f"  Invalid status. Choose from: {Animal.VALID_STATUSES}")

    def add_vaccination(self, vaccine, date):
        """Record a vaccination as a (vaccine, date) tuple."""
        self.vaccinations.append((vaccine, date))

    def display_info(self):
        """Print this animal's details."""
        print(f"  ID: {self.animal_id} | Species: {self.species} | "
              f"Age: {self.age_months} months | Status: {self.status}")
        for vaccine, date in self.vaccinations:
            print(f"      Vaccinated: {vaccine} on {date}")

    # ---------- Class methods ----------
    @classmethod
    def get_total_animals(cls):
        """Return how many animals have been created."""
        return cls.total_animals

    @classmethod
    def from_string(cls, text):
        """Create an Animal from a string like 'A001,Cow,24'."""
        animal_id, species, age = text.split(",")
        return cls(animal_id.strip(), species.strip(), int(age))

    # ---------- Static method ----------
    @staticmethod
    def is_valid_id(animal_id):
        """IDs must start with 'A' followed by digits, e.g. A001."""
        return (len(animal_id) > 1 and animal_id[0] == "A"
                and animal_id[1:].isdigit())


class Farm:
    """Manages a collection of animals, stored in a dictionary."""

    def __init__(self, name, location):
        self.name = name
        self.location = location  # general area only (privacy-respecting)
        self.animals = {}         # dictionary: animal_id -> Animal object

    def report(self):
        """Print a summary of animals by health status."""
        print(f"\nFarm report: {self.name} ({self.location})")
        for status in Animal.VALID_STATUSES:
            count = sum(1 for a in self.animals.values() if a.status == status)
            print(f"  {status}: {count}")


# ---------- Simple functions to add and display records ----------
def add_record(farm, animal):
    """Add an animal to the farm's dictionary."""
    if animal.animal_id in farm.animals:
        print(f"  Record {animal.animal_id} already exists.")
    else:
        farm.animals[animal.animal_id] = animal
        print(f"  Added {animal.animal_id} ({animal.species}).")


def display_records(farm):
    """Display every animal stored on the farm."""
    print(f"\nAll animals on {farm.name}:")
    if not farm.animals:
        print("  No records yet.")
    for animal in farm.animals.values():
        animal.display_info()


# ---------- Demonstration ----------
def main():
    farm = Farm("Green Valley Farm", "Bo District")

    print("Adding animals:")
    cow = Animal("A001", "Cow", 24)
    goat = Animal("A002", "Goat", 10)
    sheep = Animal.from_string("A003, Sheep, 14")  # class method
    add_record(farm, cow)
    add_record(farm, goat)
    add_record(farm, sheep)
    add_record(farm, cow)  # duplicate demo

    print("\nValid ID check (static method):")
    print("  A010 ->", Animal.is_valid_id("A010"))
    print("  X99  ->", Animal.is_valid_id("X99"))

    print("\nInteraction between objects:")
    cow.add_vaccination("Anthrax", "2026-09-01")
    goat.update_record("Sick")
    goat.update_record("Under Treatment")
    goat.update_record("Flying")  # invalid demo

    display_records(farm)
    farm.report()
    print(f"\nTotal animals created: {Animal.get_total_animals()}")


if __name__ == "__main__":
    main()