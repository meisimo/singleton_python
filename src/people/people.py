from .person import Person

class People():
  _instance = None

  @staticmethod
  def get_instance():
    if not People._instance:
      People._instance = People()
    return People._instance

  def __init__(self):
    if People._instance:
      raise Exception("This constructor only should be called once in get_instance")
    self.__people = {}

  def get_person(self, document):
    """[summary]

    Args:
        document ([str]): [description]

    Returns:
      (Person): person
    """
    return self.__people[document]

  def get_people(self):
    return self.__people.values()
    
  def insert_person(self, document, name, birthday, vaccinated):
    """Insert a person in the people map

    Args:
        document ([str]): [description]
        name ([str]): [description]
        birthday ([datetime.date]): [description]
        vaccinated ([bool]): [description]
    """
    self.__people[document] = Person(document, name, birthday, vaccinated)

  def remove_person(self, document):
    """Remove a person in from the people map

    Args:
        document ([str]): [description]
    """
    del self.__people['document']
