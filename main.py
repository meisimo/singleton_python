from datetime import date

class Menu:

    def __init__(self):
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
            print("Actualizar Estado")
        elif opt == "3":
            print("Excluir Personal")
        elif opt == "4":
            print("Consultar Listado")
        elif opt == "5":
            print("Imprimir Log")
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


    def actualizar_estado(self):
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')
        print("\x1b[1,32m"+"            Actualizar Estado           "+'\033[0m')
        print("\x1b[1,32m"+"----------------------------------------"+'\033[0m')




menu = Menu()
menu.run()
