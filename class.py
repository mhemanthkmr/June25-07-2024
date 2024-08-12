class mobilephone:
    def __init__(self,camera,color):
        self.color = color
        self.camera = camera
        
    def display(self):
        print (f"color:{self.color} & camera:{self.camera}")
class owner (mobilephone):
    def owner(self):
        print("my phone")
    pass
    
obj1 = owner("green",64)
obj1.display()

class cell:
    # ram =4
    # rom =64 
    # f_camera=64
    # b_camera=128
    # color ="black"
    # os ="android"
    # display = "OLED"
    # battery =5000
    
    def __init__(self,ram,rom,f_camera,b_camera,color,os,display,battery):
        self.ram = ram
        self.rom = rom
        self.f_camera = f_camera
        self.b_camera = b_camera
        self.color = color
        self.os = os
        self.display = display
        self.battery = battery



    def displayconfigurations(self):
        print(f"RAM: {self.ram} GB")
        print(f"ROM: {self.rom} GB")
        print(f"Front Camera: {self.f_camera} MP")
        print(f"Back Camera: {self.b_camera} MP")
        print(f"Color: {self.color}")
        print(f"Operating System: {self.os}")
        print(f"Display: {self.display}")
        print(f"Battery: {self.battery} mAh")
     
    def upgradeRAMandCOLOR(self,ram,color):
        self.ram =ram
        self.color=color

# mobilephone1 =mobile()
# print(mobilephone1.color)
# mobilephone2 =mobile()
# print(mobilephone2.rom)
cell1=cell(4,64,64,128,"red","iOs","LCD",5000)
cell1.displayconfigurations()
cell1.upgradeRAMandCOLOR(12,"white")
cell1.displayconfigurations()

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        pass
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a  * self.b
    def divide(self):
        return self.a  / self.b
    
calc =calculator(8,9)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.divide())

calc =calculator(34,78)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.divide())

