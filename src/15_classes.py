# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    lat = 0
    lon = 0

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    name = ""

    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return "name:%s lat:%s, lon:%s" % (self.name,self.lat, self.lon)

waypoint = Waypoint(5, 5, "sauce")
#print(waypointInst.name)


# nice, easy enough

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    difficulty = 0
    size = ""

    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return "name:%s difficulty:%s  size:%s lat:%s, lon:%s" % (self.name,self.difficulty,self.size,self.lat, self.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
catacombsWP = Waypoint(name="Catacombs", lat=41.70505, lon=-121.51521)
print(catacombsWP)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137,-121.41556,"Newberry Views",1.5,"two")

# Print it--also make this print more nicely
print(geocache)
