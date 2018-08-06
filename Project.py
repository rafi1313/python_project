

class Project:
    def __init__(self, _project_id):
        self.user_id = _project_id
        self.menu()

    def menu(self):
        loop = True
        while loop:
            self.availableOptions()
            option = input("Wybierz opcję").upper()
            while option == "":
                option = input("Wybierz opcję").upper()
            if option == "D":
                self.addDrawing()
            elif option == "U":
                print("opcja U")
                self.deleteDrawing()
            elif option == "P":
                print("opcja P")
                self.showDrawings()
            elif option == "Z":
                print("opcja Z")
                self.showPaidDrawings()
            elif option == "N":
                print("opcja N")
                self.showUnpaidDrawings()
            elif option == "M":
                print("opcja M")
                self.modifyDrawingData()
            elif option == "F":
                print("opcja F")
                self.findDrawing()
            elif option == "W":
                print("opcja W")
                self.selectDrawingsByDate()
            elif option == "Q":
                loop = False
            else:
                print("Nieznana opcja!")

    def availableOptions(self):
        print("Dostępne opcje:")
        print("D - dodaj nowy rysunek")
        print("U - usuń rysunek")
        print("P - Pokaż wszystkie rysunki")
        print("Z - Pokaż listę rozliczonych rysunków")
        print("N - Pokaż listę nierozliczonych rysunków")
        print("M - modyfikuj dane o rysunku")
        print("F - szukaj rysunku")
        print("W - wybierz rysunki po dacie")
        print("Q-wyjście")

    def showDrawings(self):
        print("Lista rysunków.")

    def addDrawing(self):
        print("Dodawanie rysunku")

    def deleteDrawing(self):
        print("Usuwanie rysunku")

    def showPaidDrawings(self):
        print("Lista rozliczonych rysunków")

    def showUnpaidDrawings(self):
        print("Lista nierozliczonych rysunków")

    def modifyDrawingData(self):
        print("Modyfikacja rysunku")

    def findDrawing(self):
        print("Wyszukiwanie rysunku")

    def selectDrawingsByDate(self):
        print("wybierz rysunki po dacie")