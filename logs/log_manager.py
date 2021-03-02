from action import Action

class LogManager():
  _log_header = f"{'ACCION':30s} | {'DOCUMENTO':15s} | FECHA"
  _instance = None
  
  @staticmethod
  def get_instance():
    """[summary]

    Returns:
        [LogManager]: [description]
    """
    if not LogManager._instance:
      LogManager._instance = LogManager()
    return LogManager._instance

  def __init__(self):
    if LogManager._instance:
      raise Exception("This constructor only should be called once in get_instance")
    self.__actions = []

  def insert_action(self, action:str, document:str) -> None:
    self.__actions.append(Action(action, document))

  def get_log(self):
    separator = "\n" + "-" * len(self._log_header) + "\n"
    return self._log_header + separator + "\n".join(str(act) for act in self.__actions) + separator
