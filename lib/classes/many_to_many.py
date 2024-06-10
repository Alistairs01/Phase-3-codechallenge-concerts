class Band:
    def __init__(self, name, hometown):

        self.name = name
        self.hometown = hometown
        self._concerts = []    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if  isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise TypeError("Name must be a non-empty string.")
    @property
    def hometown(self):
        return self._hometown
    @hometown.setter
    def hometown(self, value):
        if hasattr(self, '_hometown'):
            raise AttributeError("Hometown cannot be changed once set")
        if isinstance(value, str) and len(value):
            self._hometown = value
        else:
            raise ValueError("Hometown must be a non-empty string.")
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
       
        self.date = date
        self.band = band
        self.venue = venue

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value):
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string.")

    @property
    def band(self):
        return self._band
    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be a Band object.")

    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be a Venue object.")
    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
       
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value):
            self._city = value
        else:
            raise ValueError("City must be a non-empty string.")

    def concerts(self):
        return self._concerts

    def add_concert(self, concert):
        self._concerts.append(concert)

    def bands(self):
        return list(set(concert.band for concert in self._concerts))
