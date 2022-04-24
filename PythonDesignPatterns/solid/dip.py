"""
Dependency Inversion Principle

High-level modules should not depend upon low-level ones - use abstractions.
"""
from abc import abstractclassmethod, abstractmethod
from enum import Enum

class Relationship(Enum):
  PARENT = 0
  CHILD = 1
  SIBLING = 2


class Person:
  def __init__(self, name):
    self.name = name


class RelationshipBrowser:
  @abstractmethod
  def find_all_children_of(self,name): pass


class Relationships(RelationshipBrowser):
  """
  Low-Level Module
  """
  def __init__(self):
    self.relations = []


  def add_parent_and_child(self, parent, child):
    self.relations.append(
      (parent, Relationship.PARENT, child)
    )
    self.relations.append(
      (child, Relationship.CHILD, parent)
    )

  def find_all_children_of(self, name):
    """
    Fixes principle since a change in self.relations would require dev to change to this method.
    This allows Research() to not have to go through a code change.
    """
    for relation in self.relations:
      if relation[0].name == name and relation[1] == Relationship.PARENT:
        yield relation[2].name


class Research:
  """
  High-Level Module
  """
  def __init__(self, relationships):
    relations = relationships.relations
    # BREAKS principle since there is a dependency on the low level relations being a list
    for relation in relations:
      if relation[0].name == 'John' and relation[1] == Relationship.PARENT:
        print(f'John has a child called {relation[2].name}')

  def __init__(self, browser):
    for person in browser.find_all_children_of('John'):
      print(f'John has a child called {person}.')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)