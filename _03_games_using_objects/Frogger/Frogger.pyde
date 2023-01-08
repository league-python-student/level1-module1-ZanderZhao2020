
def setup():
    # 1. Use the size function to set the size of your sketch
    size(800, 600)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    global bg, frog
    bg = loadImage("froggerBackground.png")
    frog = loadImage("frog.png")
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    bg.resize(800, 600)
    frog.resize(50, 50)
    
    global frog_x, frog_y
    frog_x = 0
    frog_y = 0
    global car
    car = Car(0, 200, 50, 5)
    global car2, car3, car4, car5
    car2 = Car(0, 271, 50, 9)
    car3 = Car(0, 342, 50, 13)
    car4 = Car(0, 391, 50, 17)
    car5 = Car(0, 452, 50, 25)
    
def draw():
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    image(frog, frog_x, frog_y)
    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    # global frog_x, frog_y
    global frog_x, frog_y
    
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    global car, car2, car3, car4, car5
    car.update()
    car.draw()
    car2.update()
    car2.draw()
    car3.update()
    car3.draw()
    car4.update()
    car4.draw()
    car5.update()
    car5.draw()
    
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    if intersects(car) or intersects(car2) or intersects(car3) or intersects(car4) or intersects(car5):
        frog_x = 0
        frog_y = 0
    
    # 9. Create more car objects of different lengths, speed, and size

def keyPressed():
    global frog_x, frog_y
    if key == CODED:
        if keyCode == UP:
            # Frog Y position goes up
            frog_y -= 5
        elif keyCode == DOWN:
            # Frog Y position goes down
            frog_y += 5
        elif keyCode == RIGHT:
            # Frog X position goes right
            frog_x += 5
        elif keyCode == LEFT:
            # Frog X position goes left
            frog_x -= 5
class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
def intersects(car):
    global frog_y, frog_x
    if frog_y > car.y and frog_y < car.y + 50 and frog_x > car.x and frog_x < car.x + car.size:
        return True;
    else:
        return False;
