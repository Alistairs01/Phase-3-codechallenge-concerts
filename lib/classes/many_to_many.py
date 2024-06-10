class Band:
    def __init__(self, name, hometown):
        """Instantiate a Band object with name and hometown"""
        self._name = None # making name mutable since it can be changed from none to a string
        self.name = name
        self._hometown = None
        self.hometown = hometown
        self._concerts = []

    @property
    def name(self):
       
        return self._name

    @name.setter
    def name(self, value):
        
        if not isinstance(value, str) or len(value) == 0:
            print("Name must be a non-empty string")
        else:
            self._name = value

    @property
    def hometown(self):
        
        return self._hometown

    @hometown.setter
    def hometown(self, value):
       
        if self._hometown is not None:
            print("Hometown cannot be changed once set")
        elif not isinstance(value, str) or len(value) == 0:
            print("Hometown must be a non-empty string")
        else:
            self._hometown = value

    #@property
    def concerts(self):
        """Getter for concerts"""
        return self._concerts if self._concerts else None

    #@property
    def venues(self):
        """Getter for venues"""
        return list(set(concert.venue for concert in self._concerts)) if self._concerts else None

    def add_concert(self, concert):
        """Add a concert to the band's list of concerts"""
        self._concerts.append(concert)

    def play_in_venue(self, venue, date):
        """Create a new concert for the band in the given venue on the given date"""
        return Concert(date, self, venue)

    def all_introductions(self):
        """Get introductions for all of the band's concerts"""
        if not self._concerts:
            return None
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = [] # list of all concerts /must have the all attribute
    def __init__(self, date, band, venue):
        """Instantiate a Concert object with date, band, and venue"""
        self._date = None
        self.date = date
        self._band = None
        self.band = band
        self._venue = None
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        """Getter for date"""
        return self._date

    @date.setter
    def date(self, value):
        """Setter for date"""
        if not isinstance(value, str) or len(value) == 0:
            print("Date must be a non-empty string")
        else:
            self._date = value
        

    @property
    def band(self):
        """Getter for band"""
        return self._band

    @band.setter
    def band(self, value):
        """Setter for band"""
        if not isinstance(value, Band):
            print("Band must be of type Band")
        else:
            if hasattr(self, "_band") and self._band:
                self._band._concerts.remove(self)
            self._band = value
            self._band.add_concert(self)

    @property
    def venue(self):
        """Getter for venue"""
        return self._venue

    @venue.setter
    def venue(self, value):
        """Setter for venue"""
        if not isinstance(value, Venue):
            print("Venue must be of type Venue")
        else:
            if hasattr(self, "_venue") and self._venue:
                self._venue._concerts.remove(self)
            self._venue = value
            self._venue.add_concert(self)

    def hometown_show(self):
        """Returns True if the concert is in the band's hometown, False otherwise"""
        return self.band.hometown == self.venue.city

    def introduction(self):
        """Returns the introduction for the concert"""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        """Instantiate a Venue object with name and city"""
        self._name = None
        self.name = name
        self._city = None
        self.city = city
        self._concerts = []

    @property
    def name(self):
        """Getter for name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name"""
        if not isinstance(value, str) or len(value) == 0:
            print("Name must be a non-empty string")
        else:
            self._name = value

    @property
    def city(self):
        """Getter for city"""
        return self._city

    @city.setter
    def city(self, value):
        """Setter for city"""
        if not isinstance(value, str) or len(value) == 0:
            print("City must be a non-empty string")
        else:
            self._city = value

    def add_concert(self, concert):
        """Add a concert to the venue's list of concerts"""
        self._concerts.append(concert)

    def concerts(self):
        """Getter for concerts"""
        return self._concerts if self._concerts else None

    def bands(self):
        """Getter for bands"""
        if not self._concerts:
            return None
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        """Get the concert on the given date"""
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
