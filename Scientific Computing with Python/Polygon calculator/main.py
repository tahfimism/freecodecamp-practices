class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, n):
        self.width = n
    
    def set_height(self, n):
        self.height = n
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height)*2

    def get_diagonal(self):
        return  ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        return ("*" * self.width + "\n") * self.height
        
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
    def set_side(self, side):
        self.width = self.height = side
    
    def set_width(self, side):
        self.width = self.height = side

    def set_height(self, side):
        self.width = self.height = side

    def __str__(self):
        return f"Square(side={self.width})"