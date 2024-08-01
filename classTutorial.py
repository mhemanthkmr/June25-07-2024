class MobilePhone:
    def __init__(self, ram, rom, backCamera, color, os, display, battery, frontCamera = "Not Provided"):
        self.ram = ram
        self.rom = rom
        self.frontCamera = frontCamera
        self.backCamera = backCamera
        self.color = color
        self.os = os
        self.display = display
        self.battery = battery

    def displayConfigurations(self):
        print(f"RAM: {self.ram}GB")
        print(f"ROM: {self.rom}GB")
        print(f"Front Camera: {self.frontCamera}MP")
        print(f"Back Camera: {self.backCamera}MP")
        print(f"Color: {self.color}")
        print(f"Operating System: {self.os}")
        print(f"Display: {self.display}")
        print(f"Battery: {self.battery}mAh")
    
    def upgradeRAMandROM(self,ram,rom) :
        self.ram = ram
        self.rom = rom



mobile1 = MobilePhone(4,64,128,"Red","Ios","OLED",4300)
mobile1.displayConfigurations()
mobile1.upgradeRAM(8)
mobile1.displayConfigurations()


