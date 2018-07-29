
class User:
    def __init__(self, _id):
        self.user_id = _id
        self.menu()

    def menu(self):
        loop = True
        while loop:
            option = input("Wybierz opcję działania: D-dodaj nowy projekt, P-pokaż projekty, U-usuń projekt, Z-zarządzaj wybranym projektem, Q-wyjście: ")
            while option == "":
                option = input(
                    "Wybierz opcję działania: D-dodaj nowy projekt, P-pokaż projekty, U-usuń projekt, Z-zarządzaj wybranym projektem, Q-wyjście: ")
            if option =="D":
                print("Dodawanie projektu: ")
#                 # kod dodawania projektu
            elif option == "P":
                # pokazanie listy projektów
                print("Lista Projektów\n")
                # self.showProjects( self.user_id)
            elif option == "Q":
                loop = False
            else:
                print("Nieznana opcja!")

    # self.c.execute("SELECT * FROM logowanie where login=%s and haslo=%s", (login, passwrd))
    # LogRes = self.c.fetchall()
    # if (len(LogRes) == 1):
    #     print("zalogowano")
    #     self.menu(LogRes[0][5])
    # else:
    #     print("błędne hasło")
    #
    #


    #
    #
    # def showProjects(self):
    #     Login.