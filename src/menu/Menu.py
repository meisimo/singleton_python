from datetime import date

from ..people.people_manager import PeopleManager

class Menu:

    def __init__(self):
        self.people_manager = PeopleManager()
        self.running = True

    def run(self):
        while self.running:
            self.display_menu()
            self.choose_option()

    def display_menu(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            MAXISOLUTIONS               "+'\033[0m')
        print("\x1b[1,32m"+"            "+ str(date.today()) +"     "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"1. Incluir Personal"+'\033[0m')
        print("\x1b[1,32m"+"2. Actualizar Estado"+'\033[0m')
        print("\x1b[1,32m"+"3. Excluir Personal"+'\033[0m')
        print("\x1b[1,32m"+"4. Consultar Listado"+'\033[0m')
        print("\x1b[1,32m"+"5. Imprimir Log"+'\033[0m')
        print("\x1b[1,32m"+"6. Salir"+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')

    def choose_option(self):
        opt = input("Elija la opción: ")
        if opt == "1":
            self.incluir_personal()
        elif opt == "2":
            self.actualizar_estado()
        elif opt == "3":
            self.excluir_persona()
        elif opt == "4":
            self.consultar_listado()
        elif opt == "5":
            self.imprimir_log()
        elif opt == "6":
            raise SystemExit

    def incluir_personal(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Incluir Personal            "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')

        name = input("Digite el nombre: ")
        document = input("Digite el documento: ")
        date_input = input("Ingrese la fecha dd/mm/yyyy: ")
        day, month, year = map(int, date_input.split("/"))
        date_parse = date(year, month, day)
        vaccunated = input("Estado (S/N): ") 

        self.people_manager.include_person(document, name, date_parse, vaccunated == "S")

        print("\x1b[1,32m"+"La persona se creo correctamente"+'\033[0m')


    def actualizar_estado(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Actualizar Estado           "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')

        document = input("Documento: ")
        state    = input("Nuevo Estado S/N: ")

        try:
            self.people_manager.update_person_vaccinated_status(document, state=="S")
        except KeyError:
            print(f"El documneot {document} no se encuentra en el registro")

    def excluir_persona(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Excluir Persona             "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')

        document = input("Documento: ")

        try:
            self.people_manager.exclude_person(document)
        except KeyError:
            print(f"El documneot {document} no se encuentra en el registro")
    
    def consultar_listado(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Consultar Listado          "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print(self.people_manager.get_people())

    def imprimir_log(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Imprimir Log                "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m') 
        print(self.people_manager.get_log())