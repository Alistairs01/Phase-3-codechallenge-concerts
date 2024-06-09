class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(hometown, str) or len(hometown) == 0:
            raise ValueError("Hometown must be a non-empty string.")
        self.name = name
        self.hometown = hometown
        self._concerts = []

    def concerts(self):
        return self._concerts

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        venue.add_concert(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]


class Concert:
    def __init__(self, date, band, venue):
        if not isinstance(date, str) or len(date) == 0:
            raise ValueError("Date must be a non-empty string.")
        if not isinstance(band, Band):
            raise ValueError("Band must be an instance of Band.")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be an instance of Venue.")
        self.date = date
        self.band = band
        self.venue = venue

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        if self.hometown_show():
            return f"Hello {self.venue.city}! We're {self.band.name} and we're home!"
        else:
            return f"Hello {self.venue.city}! We're {self.band.name} and we're from {self.band.hometown}."


class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(city, str) or len(city) == 0:
            raise ValueError("City must be a non-empty string.")
        self.name = name
        self.city = city
        self._concerts = []

    def concerts(self):
        return self._concerts

    def add_concert(self, concert):
        self._concerts.append(concert)

    def bands(self):
        return list(set(concert.band for concert in self._concerts))
