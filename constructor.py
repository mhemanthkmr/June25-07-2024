class Laptop:
    def __init__(self, screensize, displaysurface, resolution_x, resolution_y, ppi, touchtechnology, multitouch):
        self.screensize = screensize
        self.displaysurface = displaysurface
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.ppi = ppi
        self.touchtechnology = touchtechnology
        self.multitouch = multitouch

    def configuration(self):
        print(f"screensize: {self.screensize}")
        print(f"displaysurface: {self.displaysurface}")
        print(f"resolution (x): {self.resolution_x}")
        print(f"resolution (y): {self.resolution_y}")
        print(f"ppi: {self.ppi}")
        print(f"touchtechnology: {self.touchtechnology}")
        print(f"multitouch: {self.multitouch}")
class Hp(Laptop):
    pass

lap = Laptop(13.3, 'Glossy', 3200, 325, 1800, 'capactive', 'yes')
lap.configuration()
hplap = Hp(15.3, 'Glossy', 3500, 375, 1900, 'capactive', 'yes')
hplap.configuration()