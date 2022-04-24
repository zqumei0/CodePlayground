"""
Liskov Substitution Principle

You should be able to substitute a base type for a subtype.
"""
class Rectangle:
  def __init__(self, width, height):
    self._height = height
    self._width = width


  def __str__(self):
    return f'Width: {self.width}, height: {self.height}'


  @property
  def area(self):
    return self._width * self._height


  @property
  def width(self):
    return self._width


  @width.setter
  def width(self, value):
    self._width = value


  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, value):
    self._height = value


class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)


  @Rectangle.width.setter
  def width(self, value):
    self._width = self._height = value


  @Rectangle.height.setter
  def height(self, value):
    self._width = self._height = value


def use_it(rectangle):
  w =rectangle.width
  rectangle.height = 10
  expected_area = int(w*10)
  print(f'Expected: {expected_area}\nActual: {rectangle.area}')

rectangle = Rectangle(2, 3)
use_it(rectangle)

# Breaks LSP - Square should have worked with Reactangle properties
square = Square(5)
use_it(square) 