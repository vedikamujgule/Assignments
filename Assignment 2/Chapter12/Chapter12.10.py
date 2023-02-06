# (Tkinter: four cars) Write a program that simulates four cars racing, as shown in
# Figure 12.22. You should define a subclass of Canvas to display a car.


from tkinter import * 
class RaceCar(Canvas):
    
    def __init__(self, master, width, height):
        Canvas.__init__(self, master, width=width, height=height)
        self.sleepTime = 100
        self.x = 10
        self.y = 50
        self.displayCar()

    def displayCar(self):
        # Create Cars shape here
        self.delete("car")
        self.create_rectangle(self.x, self.y - 20, self.x + 50, self.y - 10, tags="car")
        self.create_polygon(self.x + 10, self.y - 20, self.x + 20, self.y - 30,
                            self.x + 30, self.y - 30, self.x + 40, self.y - 20, tags="car")
        self.create_oval(self.x + 30, self.y - 10, self.x + 40, self.y, tags="car")
        self.create_oval(self.x + 10, self.y - 10, self.x + 20, self.y, tags="car")

def main():
    while True:
        for car in cars:
            if car.x < int(car["width"]):
                car.displayCar()
                car.x += 4
            else:
                car.x = 0
            car.after(20)  
            car.update()


window = Tk()  
window.title("Racing Cars")
width = 250
height = 48

cars = []
for i in range(4):
    cars.append(RaceCar(window, width=width, height=height))
    cars[i].pack()
main()
