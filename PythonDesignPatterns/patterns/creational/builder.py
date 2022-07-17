"""
Builder Design Pattern

When piecewise object construction is complicated, provide
an API for doing it succinctly.

1) Piecewise construction
2) Builder provides an API for constructing an object
   step-by-step
"""
from urllib.request import HTTPPasswordMgrWithDefaultRealm


class HtmlElement:
  indent_size = 2

  def __init__(self, name='', text=''):
    self.name = name
    self.text = text
    self.elements = []

  def __str(self, indent):
    lines = []
    _indent = ' ' * (indent * self.indent_size)
    lines.append(f'{_indent}<{self.name}>')

    if self.text:
      indent1 = ' ' * ((indent + 1) * self.indent_size)
      lines.append(f'{indent1}{self.text}')

    for e in self.elements:
      lines.append(e.__str(indent + 1))
    
    lines.append(f'{_indent}</{self.name}>')
    return '\n'.join(lines)

  @staticmethod
  def create(name):
    return HtmlBuilder(name)


  def __str__(self):
    return self.__str(0)


class HtmlBuilder:
  def __init__(self, root_name):
      self.root_name = root_name
      self.__root = HtmlElement(root_name)


  def add_child(self, child_name, child_text):
    self.__root.elements.append(
      HtmlElement(child_name, child_text)
    )


  def add_child_fluent(self, child_name, child_text):
    self.__root.elements.append(
      HtmlElement(child_name, child_text)
    )
    return self


  def __str__(self):
    return str(self.__root)


# Invoke Builder - Method 1
builder = HtmlBuilder('ul')
# Invoke Builder - Method 2
builder = HtmlElement.create('ul')

# Add Children - Method 1
builder.add_child('li', 'hello')
builder.add_child('li', 'world')

# Add Children - Method 2
# builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')

print('Ordinary builder:')
print(builder)