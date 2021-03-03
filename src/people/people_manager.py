from .people import People
from ..logs.log_manager import LogManager

class PeopleManager():
  
  def include_person(self, document, name, birthday, vaccinated):
    People.get_instance().insert_person(document, name, birthday, vaccinated)
    LogManager.get_instance().insert_action('Incluir persona', document)

  def update_person_vaccinated_status(self, document, vaccinated):
    People.get_instance().get_person(document).update_vaccinated_status(vaccinated)
    LogManager.get_instance().insert_action('Actualizar vacunación', document)

  def exclude_person(self, document):
    People.get_instance().remove_person(document)
    LogManager.get_instance().insert_action('Remueve persona', document)

  def get_people(self):
    LogManager.get_instance().insert_action('Listar personas', '')
    return "NOMBRE / DOCUMENTO / CUMPLEAÑOS / VACUNADO \n" + "\n".join( str(p) for p in People.get_instance().get_people() )

  def get_log(self):
    return LogManager.get_instance().get_log()
    