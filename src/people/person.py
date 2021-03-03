class Person():
  def __init__(self, document, name, birthday, vaccinated):
    """Person

    Args:
        document (str): [description]
        name (str): [description]
        birthday (datetime.date): [description]
        vaccinated (bool): [description]
    """

    self._document   = document
    self._name       = name
    self._birthday   = birthday
    self._vaccinated = vaccinated

  def update_vaccinated_status(self, vaccinated):
    """[summary]

    Args:
        vaccinated (bool): [description]
    """
    self._vaccinated = vaccinated

  def __str__(self):
    return self._name + " / " + self._document + " / " + self._birthday.strftime("%d/%m/%Y") + " / " + ("S" if self._vaccinated else "N")
