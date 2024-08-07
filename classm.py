class mobilePhone:
    def __init__(self,RAM,ROM,color,Display,Frontcamera,Backcamera,OS,Battery):
        self.RAM=RAM
        self.ROM=ROM
        self.color=color
        self.Display=Display
        self.Frontcamera=Frontcamera
        self.Backcamera=Backcamera
        self.OS=OS
        self.Battery=Battery
    def display(self):
        print(f'RAM:{self.RAM}GB')
        print(f'ROM:{self.ROM}GB')
        print(f'color:{self.color}')
        print(f'Display:{self.Display}')
        print(f'Frontcamera:{self.Frontcamera}HP')
        print(f'Backcamera:{self.Backcamera}HP')
        print(f'OS:{self.OS}')
        print(f'Battery:{self.Battery}')
mobile1=mobilePhone(4,64,"blue","OLED",56,78,"IOS",4300)
mobile1.display()
        
mobile2=mobilePhone(8,62,"red","OLED",53,88,"OS",5200)  
mobile2.display()  
        