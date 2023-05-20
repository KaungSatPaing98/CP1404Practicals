class Band:
    """Class representing a band with musicians."""

    def __init__(self, name):
        """Initialize a Band instance with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make the band play by having each musician play their instrument."""
        print(self.name)
        for musician in self.musicians:
            musician.play()

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"


class Musician:
    """Class representing a musician."""

    def __init__(self, name, instruments=None):
        """Initialize a Musician instance with a name and a list of instruments."""
        self.name = name
        self.instruments = instruments if instruments is not None else []

    def add_instrument(self, instrument):
        """Add an instrument to the musician."""
        self.instruments.append(instrument)

    def play(self):
        """Make the musician play each instrument."""
        if self.instruments:
            for instrument in self.instruments:
                print(f"{self.name} is playing: {instrument}")
        else:
            print(f"{self.name} needs an instrument!")

    def __str__(self):
        """Return a string representation of the musician and their instruments."""
        instrument_strings = [str(instrument) for instrument in self.instruments]
        return f"{self.name} ({', '.join(instrument_strings)})"


class Instrument:
    """Class representing a musical instrument."""

    def __init__(self, name, cost):
        """Initialize an Instrument instance with a name and a cost."""
        self.name = name
        self.cost = cost

    def __str__(self):
        """Return a string representation of the instrument and its cost."""
        return f"{self.name} : ${self.cost:.2f}"
