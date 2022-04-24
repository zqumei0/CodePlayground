"""
Open-Closed Principle

Classes should be open for extension but closed for modification.
"""
from enum import Enum


class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3


class Size(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3


class Product:
  def __init__(self, name, color, size):
    self.name = name
    self.color = color
    self.size = size


# Objects should not be modifiable only extendable (make objects scalable).
# Below is incorrect way to filter by different properties
class ProductFilter:
  def filter_by_color(self, products, color):
    for product in products:
      if product.color == color: yield product


  def filter_by_size(self, products, size):
    for product in products:
      if product.size == size: yield product


# Proper way to use OCP to make design more scalable
class Specification:
  """
  Base Class for Specification that will be used for filtering
  """
  def is_satisfied(self, item):
    """Pass because it is meant to be overloaded"""
    pass

  # OVERLOADS & binary operator to run AndSpecification to make it easier.
  def __and__(self, other):
    return AndSpecification(self, other)


class Filter:
  """
  Base Class for filters.
  """
  def filter(self, items, spec):
    """Pass because it is meant to be overloaded"""
    pass


class ColorSpecification(Specification):
  """
  Specification for Color property used in filters
  """
  def __init__(self, color):
    self.color = color


  def is_satisfied(self, item):
      return item.color == self.color


class SizeSpecification(Specification):
  """
  Specification for Size property used in filters
  """
  def __init__(self, size):
    self.size = size

  def is_satisfied(self, item):
      return item.size == self.size


class AndSpecification(Specification):
  """
  And Specification for combining specifications for filters
  """
  def __init__(self, *args):
    self.args = args


  def is_satisfied(self, item):
    return all(
      map(
        lambda spec: spec.is_satisfied(item), self.args
      )
    )


class BetterFilter(Filter):
  """
  Propert way for filtering using OCP
  """
  def filter(self, items, spec):
    for item in items:
      if spec.is_satisfied(item):
        yield item


if __name__ == '__main__':
  apple = Product('Apple', Color.GREEN, Size.SMALL)
  tree = Product('Tree', Color.GREEN, Size.LARGE)
  house = Product('House', Color.BLUE, Size.LARGE)

  print('Green products: (old method)')
  products = [apple, tree, house]
  product_filter = ProductFilter()
  for product in product_filter.filter_by_color(products, Color.GREEN):
    print(f' - {product.name} is green.')
  

  better_filter = BetterFilter()
  green = ColorSpecification(Color.GREEN)

  print('Green products: (new method)')
  for product in better_filter.filter(products, green):
    print(f' - {product.name} is green.')


  print('Large blue items:')
  large = SizeSpecification(Size.LARGE)
  blue = ColorSpecification(Color.BLUE)
  # Non-overload method
  # large_blue = AndSpecification(large, blue)
  # Overload method
  large_blue = large & blue
  for product in better_filter.filter(products, large_blue):
    print(f' - {product.name} is large and blue.')