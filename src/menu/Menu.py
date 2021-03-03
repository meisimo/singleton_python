from datetime import datetime
from ..people.people_manager import PeopleManager

class Menu:

    def __init__(self):
        self.people_manager = PeopleManager()
        self.running = True

    def run(self):
        while self.running:
            self.display_menu()
            self.choose_option()

    def _input_document(self):
        document = input("Documento: ")

        if len(document) < 1 or 15 < len(document):
            raise ValueError(f"El documento debe tener menos de 15 caractered. Documento insertado {document}")

        return document

    def _input_name(self):
        name = input("Nombre: ")

        if len(name) < 1 or 100 < len(name):
            raise ValueError(f"El nombre debe tener menos de 100 caractered. Nombre insertado {name}")

        return name

    def _input_date(self):
        date_input = input("Ingrese la fecha dd/mm/yyyy: ")

        try :
            date_parse = datetime.strptime(date_input, '%d/%m/%Y')
        except :
            raise ValueError(f"La fecha debe estar en el formato dd/mm/yyyy. Fecha ingresada {date_input}")

        return date_parse

    def _input_vaccinated(self):
        vaccinated = input("Estado de vacunacion (S/N): ")
        vaccinated = vaccinated.upper()

        if vaccinated != "S" and vaccinated != "N" :
            raise ValueError(f"El estado de vacunacion debe ser 'S' o 'N'. Estado ingresado {vaccinated}")

        return vaccinated == "S"

    def display_menu(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            MAXISOLUTIONS               "+'\033[0m')
        print("\x1b[1,32m"+"            "+ str(datetime.today()) +"     "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"1. Incluir Personal"+'\033[0m')
        print("\x1b[1,32m"+"2. Actualizar Estado"+'\033[0m')
        print("\x1b[1,32m"+"3. Excluir Personal"+'\033[0m')
        print("\x1b[1,32m"+"4. Consultar Listado"+'\033[0m')
        print("\x1b[1,32m"+"5. Imprimir Log"+'\033[0m')
        print("\x1b[1,32m"+"6. Salir"+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')


    def choose_option(self):
        opt = input("Elija la opcion: ")
        if opt == "1":
            self.include_person()
        elif opt == "2":
            self.update_state()
        elif opt == "3":
            self.exclude_person()
        elif opt == "4":
            self.get_people()
        elif opt == "5":
            self.get_log()
        elif opt == "6":
            raise SystemExit

    def include_person(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Incluir Personal            "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')

        try:
            name       = self._input_name()
            document   = self._input_document()
            date_parse = self._input_date()
            vaccunated = self._input_vaccinated()

            self.people_manager.include_person(document, name, date_parse, vaccunated)

            print("\x1b[1,32m"+"La persona se creo correctamente"+'\033[0m')
        except ValueError as e:
            print(e)

    def update_state(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Actualizar Estado           "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')


        try:
            document = self._input_document()
            state    = self._input_vaccinated

            self.people_manager.update_person_vaccinated_status(document, state)
        except KeyError:
            print(f"El documneot {document} no se encuentra en el registro")
        except ValueError as e:
            print(e)

    def exclude_person(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Excluir Persona             "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')


        try:
            document = self._input_document()
            self.people_manager.exclude_person(document)
        except KeyError:
            print(f"El documneot {document} no se encuentra en el registro")
        except ValueError as e:
            print(e)
    
    def get_people(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Consultar Listado          "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print(self.people_manager.get_people())

    def get_log(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Imprimir Log                "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m') 
        print(self.people_manager.get_log())