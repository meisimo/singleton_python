from datetime import datetime

class Action():

  def __init__(self, action:str, document:str):
    self.__date     = datetime.now()
    self.__action   = action
    self.__document = document
    
  def __str__(self):
    return f"{self.__action:30s} | {self.__document:15s} | {self.__date.strftime('%d/%m/%Y')}"