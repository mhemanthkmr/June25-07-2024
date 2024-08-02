class Mobilephone :
    ram =8
    rom =128
    frontcamera =32
    backcamera =50
    color = "green"
    os ="android"
    display ="oled"
    battery =5000

    

    def __init__(self, ram, rom, frontcamera, backcamera, os, display, battery,color="not provided"):
        self.ram = ram
        self.rom = rom
        self.frontcamera = frontcamera
        self.backcamera = backcamera
        self.color = color
        self.os = os
        self.display = display
        self.battery = battery

   

    def displayconfiguration(self):
        print(f"RAM:", self.ram, "GB")
        print(f"ROM:", self.rom, "GB")
        print(f"Front Camera:", self.frontcamera, "MP")
        print(f"Back Camera:", self.backcamera, "MP")
        print(f"Color:", self.color)
        print(f"Operating System:", self.os)
        print(f"Display:", self.display)
        print(f"Battery:", self.battery, "mAh")
        
    def upgradeRAM (self,ram):
        self.ram =ram

mobile1 = Mobilephone(4,64,16,128,"ios","oled",4500)
mobile1.displayconfiguration()
mobile1.upgradeRAM(16)
mobile1.displayconfiguration()


#print(mobile1.rom)

#mobile2 = Mobileph8ne()
#print(mobile2.2om2