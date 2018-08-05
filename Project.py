

class Project:
    def __init__(self, _project_id):
        self.user_id = _project_id
        self.menu()
    def menu(self):
        loop = True
        optionsList = "Wybierz opcję działania: D-dodaj nowy projekt, " \
                      "P-pokaż projekty, " \
                      "U-usuń projekt, Z-zarządzaj wybranym projektem, " \
                      "R - Pokaż wszystkie rysunki, " \
                      "Z - Pokaż listę rozliczonych rysunków, " \
                      "N - Pokaż listę nierozliczonych rysunków, " \
                      "Q-wyjście: "
        while loop:
            option = input(optionsList)
            while option == "":
                option = input(optionsList)
            if option =="D":
                print("opcja D")
            elif option =="D":
                print("opcja D")
            elif option =="D":
                print("opcja D")