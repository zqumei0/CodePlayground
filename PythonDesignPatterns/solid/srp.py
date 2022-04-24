"""
Single Responsibility Principle - Separation of Concerns
"""
class Journal:
  """
  Journal object that stores entries.
  """

  def __init__(self):
    self.entries = []
    self.count = 0


  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}: {text}')


  def remove_entry(self, index):
    del self.entries[index]


  def __str__(self):
    return '\n'.join(self.entries)


class PersistenceManager:
  """
  Write to file is separated from Journal object with PersistenceManager Object.
  """
  
  @staticmethod
  def save_to_file(journal, filename):
    file = open(filename, 'w')
    file.write(str(journal))
    file.close()
