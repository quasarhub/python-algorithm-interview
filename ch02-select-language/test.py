from dataclasses import dataclass

@dataclass  # __init__(self, width, height) 대신 유용하게 쓸 수 있음.
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height


rect = Rectangle(3, 4)
print(rect.area())        # 12
