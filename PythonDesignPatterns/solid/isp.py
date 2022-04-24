"""
Interface Segregation Principle
"""
# Should split these interfaces into different interfaces to remove dependencies from one another
from abc import abstractclassmethod, abstractmethod

# BAD
class Machine:
  def print(self, document):
    raise NotImplementedError
  def fax(self, document):
    raise NotImplementedError
  def scan(self, document):
    raise NotImplementedError


class MultiFunctionPrinter(Machine):
  def print(self, document):
    pass
  def fax(self, document):
    pass
  def scan(self, document):
    pass


class OldFashionedPrinter(Machine):
  def print(self, document):
    #OK
    pass
  def fax(self, document):
    #Does not have feature
    pass
  def scan(self, document):
    pass


# GOOD
class Printer:
  @abstractmethod
  def print(self, document):
    pass


class Scanner:
  @abstractmethod
  def scan(self, document):
    pass


class Fax:
  @abstractmethod
  def fax(self, document):
    pass


class MyPrinter(Printer):
    def print(self, document):
      print(document)


class Photocopier(Printer, Scanner):
  def print(self, document):
    pass

  def scan(self, document):
    pass


class MultiFunctionDevice(Printer, Scanner):
  @abstractmethod
  def print(self, document):
    pass

  @abstractmethod
  def scan(self, document):
    pass


class MultiFunctionMachine(MultiFunctionDevice):
  def __init__(self, printer, scanner):
    self.scanner = scanner
    self.printer = printer


  def print(self, document):
    self.printer.print(document)


  def scan(self, document):
    self.scannner.scan(document)
