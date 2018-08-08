from DBConnect import DBConnect


class Project:
    def __init__(self, _project_id, _user_id):
        self.project_id = _project_id
        self.user_id = _user_id
        self.db = DBConnect()
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
            #     self.deleteDrawing()
            elif option == "P":
                self.showDrawings()
            elif option == "Z":
                self.showPaidDrawings()
            elif option == "N":
                self.showUnpaidDrawings()
            elif option == "M":
                self.modifyDrawingData()
            elif option == "F":
                self.findDrawing()
            # elif option == "W":
            #     self.selectDrawingsByDate()
            elif option == "Q":
                loop = False
            else:
                print("Nieznana opcja!")

    def availableOptions(self):
        print("Dostępne opcje:")
        print("D - dodaj nowy rysunek")
        # print("U - usuń rysunek")
        print("P - pokaż wszystkie rysunki")
        print("Z - pokaż listę rozliczonych rysunków")
        print("N - pokaż listę nierozliczonych rysunków")
        print("M - modyfikuj dane o rysunku")
        print("F - szukaj rysunku")
        # print("W - wybierz rysunki po dacie")
        print("Q-wyjście")

    def showDrawings(self):
        print("Lista rysunków.")
        drawingsQuery = "select d.id_drawings, drawing_name, drawing_num, width, height, individual_rate,project_name" \
                        " from drawings as d left join projects as p on (d.id_projects=p.id_projects) " \
                        "join projects_has_users as phu on (phu.projects_id_projects = p.id_projects) " \
                        "where Users_id_Users = " + str(self.user_id) + ";"
        result = self.db.fetchAll(drawingsQuery)
        print('|%3s|%40s|%20s|%20s|%20s|%20s|%20s' %
              ("ID", "Nazwa rysunku", "Numer rysunku", "Szerokość rys.", "Wysokość rys.", "stawka za A0 [PLN]",
               "Nazwa projektu"))
        for row in result:
            print('|%3i|%40s|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def addDrawing(self):
        drawing_name = self.nonOptionalInput("Podaj nazwę rysunku: ")
        drawing_num = self.nonOptionalInput("Podaj numer rysunku: ")
        width = self.nonOptionalInput("Podaj szerokość rysunku: ")
        height = self.nonOptionalInput("Podaj wysokość rysunku: ")
        individual_rate = self.nonOptionalInput("Podaj indywidualną stawkę: ")
        paid = self.nonOptionalInput("Czy rysunek jest rozliczony? [Tak=>1|Nie=>0]: ")
        insertQuery = "INSERT INTO drawings (drawing_name, drawing_num, width, height, individual_rate, id_projects," \
                      " paid, id_Users) values ('" + drawing_name + "', '" + drawing_num + "', " + width + "" \
                    ", " + height + ", "+ individual_rate+", "+str(self.project_id)+", "+paid+", "+str(self.user_id)+")"
        self.db.execute(insertQuery)
        self.db.conn.commit()
        # id_drawings, drawing_name, drawing_num, width, height, individual_rate, id_projects, paid, id_Users
        # print("Dodawanie rysunku")

    # def deleteDrawing(self):
    #     print("Usuwanie rysunku")

    def showPaidDrawings(self):
        print("Lista rozliczonych rysunków")
        drawingsQuery = "select d.id_drawings, drawing_name, drawing_num, width, height, individual_rate,project_name" \
                        " from drawings as d left join projects as p on (d.id_projects=p.id_projects) " \
                        "join projects_has_users as phu on (phu.projects_id_projects = p.id_projects) " \
                        "where (Users_id_Users = " + str(self.user_id) + " AND " \
                        "paid =1 AND p.id_projects = " + str(self.project_id) + ");"
        result = self.db.fetchAll(drawingsQuery)
        print('|%3s|%40s|%20s|%20s|%20s|%20s|%20s' %
              ("ID", "Nazwa rysunku", "Numer rysunku", "Szerokość rys.", "Wysokość rys.", "stawka za A0 [PLN]",
               "Nazwa projektu"))
        for row in result:
            print('|%3i|%40s|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def showUnpaidDrawings(self):
        print("Lista nierozliczonych rysunków")
        drawingsQuery = "select d.id_drawings, drawing_name, drawing_num, width, height, individual_rate,project_name" \
                        " from drawings as d left join projects as p on (d.id_projects=p.id_projects) " \
                        "join projects_has_users as phu on (phu.projects_id_projects = p.id_projects) " \
                        "where (Users_id_Users = " + str(self.user_id) + " AND " \
                        "paid =0 AND p.id_projects = " + str(self.project_id) + ");"
        result = self.db.fetchAll(drawingsQuery)
        print('|%3s|%40s|%20s|%20s|%20s|%20s|%20s' %
              ("ID", "Nazwa rysunku", "Numer rysunku", "Szerokość rys.", "Wysokość rys.", "stawka za A0 [PLN]",
               "Nazwa projektu"))
        for row in result:
            print('|%3i|%40s|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def modifyDrawingData(self):
        print("Modyfikacja rysunku")
        self.showDrawings()
        drawingId = self.nonOptionalInput("Wybierz ID rysunku do modyfikacji: ")
        query = "Select id_drawings, drawing_name, drawing_num, width, height, individual_rate, id_projects," \
                " paid, id_Users from projects where id_drawings ="+drawingId+" "

        result = self.db.fetchAll(query)
        drawing_name = result[1]
        drawing_num = result[2]
        width = result[3]
        height = result[4]
        rate = result[5]
        paid = result[7]
        drawing_name= self.optionalInput("Podaj nową nazwę rysunku lub naciśnij ENTER, aby nie zmieniać: ",drawing_name)
        drawing_num = self.optionalInput("Podaj nowy numer rysunku lub naciśnij ENTER, aby nie zmieniać: ", drawing_num)
        width = self.optionalInput("Podaj nową szerokość lub naciśnij ENTER, aby nie zmieniać: ", height)
        height = self.optionalInput("Podaj nową wysokość lub naciśnij ENTER, aby nie zmieniać: ", width)
        rate = self.optionalInput("Podaj nową stawkę lub naciśnij ENTER, aby nie zmieniać: ", rate)
        paid= self.optionalInput("Podaj status [rozliczony=>1|nierozliczony=>0] lub naciśnij ENTER, aby nie zmieniać: ",paid)

        query = "UPDATE drawings SET drawing_name ='"+drawing_name+"', drawing_num = '"+drawing_num+"', width ="+\
                width+", height= "+height+", individual_rate="+rate+", paid="+paid+" where id_drawings="+drawingId+";"

        self.db.execute(query)
        print("Zmodyfikowano!")
        # id_drawings, drawing_name, drawing_num, width, height, individual_rate, id_projects, paid, id_Users

    def findDrawing(self):
        print("Wyszukiwanie rysunku")
        phrase = self.nonOptionalInput("Podaj frazę do wyszukania: ")
        findQuery = "Select * from drawings where drawing_name" \
                    " like '%" + phrase + "%' or drawing_num like '%" + phrase + "%' "
        result = self.db.fetchAll(findQuery)
        print('|%3s|%40s|%20s|%20s|%20s|%20s|%20s' %
              ("ID", "Nazwa rysunku", "Numer rysunku", "Szerokość rys.", "Wysokość rys.", "stawka za A0 [PLN]",
               "Nazwa projektu"))
        for row in result:
            print('|%3i|%40s|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    # def selectDrawingsByDate(self):
    #     print("wybierz rysunki po dacie")

    @staticmethod
    def nonOptionalInput(napis):
        result = input(napis)
        while result == "":
            result = input(napis)
        return result

    @staticmethod
    def optionalInput(napis, data):
        userInput = input(napis)
        if userInput != "":
            result = userInput
        else:
            result = data
        return result
