import pymysql
from DBConnect import DBConnect
from Project import Project

class User:
    def __init__(self, _id):
        self.user_id = _id
        self.db = DBConnect()
        # print("user ID: "+str(self.user_id))
        self.conn = pymysql.connect('localhost', 'root', 'SqlAccount!23', 'DMP', charset='utf8')
        self.c = self.conn.cursor()
        self.menu()

    def availableOptions(self):
        print("Dostępne opcje:")
        print("D-dodaj nowego klienta")
        print("K-pokaż klientów")
        print("P-pokaż projekty")
        print("A-dodaj projekt")
        # print("U-usuń projekt")
        print("M-zarządzaj wybranym projektem")
        print("R - Pokaż wszystkie rysunki")
        print("Z - Pokaż listę rozliczonych rysunków")
        print("N - Pokaż listę nierozliczonych rysunków")
        print("Q-wyjście")

    def menu(self):

        loop = True

        while loop:
            self.availableOptions()
            option = input("Wybierz opcję: ").upper()
            while option == "":
                option = input("Wybierz opcję: ").upper()
            if option == "D":
                self.addClient()
            elif option == "K":
                self.showClients()
            elif option == "P":
                self.showProjects()
            elif option == "A":
                self.addProject()
            # elif option == "U":
            #     self.deleteProject()
            elif option == "R":
                self.showDrawings()
            elif option == "M":
                self.manageProject()
            elif option == "Z":
                self.showPaidDrawings()
            elif option == "N":
                self.showUnpaidDrawings()
            elif option == "Q":
                loop = False
            else:
                print("Nieznana opcja!")

    def addClient(self):
        print("Dodawanie klienta: ")
        clientName = input("Podaj nazwę klienta [pole obowiązkowe]: ")
        while clientName == "":
            clientName = input("Podaj nazwę klienta [pole obowiązkowe]: ")
        clientFirstName = input("Podaj imię klienta [pole opcjonalne]: ")
        clientLastName = input("Podaj nazwisko klienta [pole opcjonalne]: ")
        clientPhoneNumber = input("Podaj numer telefonu klienta [pole opcjonalne]: ")
        clientEmail = input("Podaj adres email klienta [pole obowiązkowe]: ")
        while clientEmail == "":
            clientEmail = input("Podaj adres email klienta [pole obowiązkowe]: ")

        query = "INSERT INTO CUSTOMERS (customers_name, first_name, last_name, phone_number, email, id_Users)" \
                " values ('" + clientName + "', '" + clientFirstName + "', '" + clientLastName + "', " + \
                clientPhoneNumber.replace(" ", "") + ", '" + clientEmail + "'," + str(self.user_id) + ")"

        self.c.execute(query)
        self.conn.commit()

    def showProjects(self):
        print("Lista projektów\n")
        query = "select id_projects, project_name, customers_name, project_date, project_deadline,rate_per_drawing " \
                "from projects" \
                " as p join customers as c on (c.id_customers= p.id_customers) " \
                "where id_users = " + str(self.user_id) + " order by project_name"
        self.c.execute(query)
        result = self.c.fetchall()

        print('|%3s|%20s|%20s|%20s|%20s|%20s' % (
            "ID", "Nazwa projektu", "Nazwa klienta", "start projektu", "termin projektu", "stawka za A0 [PLN]"))
        for row in result:
            print('|%3i|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5]))


    def showClients(self):
        # pokazanie listy projektów
        print("Lista klientów\n")
        query = "select * from customers where id_users = " + str(self.user_id) + " order by customers_name"
        self.c.execute(query)
        result = self.c.fetchall()
        print('|%3s|%20s|%20s|%20s|%12s|%20s' % (
        "ID", "Nazwa klienta", "Imię klienta", "Nazwisko klienta", "nr telefonu", "adres e-mail"))
        for row in result:
            print('|%3i|%20s|%20s|%20s|%12s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5]))

    def addProject(self):
        # pokazanie listy projektów
        self.showClients()

        client = input("Wybierz ID klienta do dodania projektu: ")
        while client == "":
            print("Musisz wybrać ID klienta")
            client = input("Wybierz ID klienta do dodania projektu: ")
        projectName = input("Podaj nazwę projektu: ")
        while projectName == "":
            print("Musisz podać nazwę projektu!")
            projectName = input("Podaj nazwę projektu: ")
        projectDate = input("Podaj datę przyjęcia projektu [YYYY-MM-DD]: ")
        projectDeadline = input("Podaj termin wykonania projektu [YYYY-MM-DD]: ")
        projectRate = input("Podaj stawkę za A0: ")
        self.c.execute("SET FOREIGN_KEY_CHECKS=0")
        insertQueryToProjects = "INSERT INTO projects (project_name, rate_per_drawing, project_date, " \
                                "project_deadline, id_customers) values ('" + projectName + "', " + projectRate +\
                                ", '"+projectDate+"', '"+projectDeadline+"', " + str(self.user_id)+")"

        self.c.execute(insertQueryToProjects)
        self.conn.commit()

        query = "INSERT INTO projects_has_users (Users_id_Users, customers_id_customers) " \
                "values (" + str(self.user_id) + ", " + client + ")"
        self.c.execute(query)
        self.conn.commit()
        print("Dodano projekt!")
        print(" ")

    # def deleteProject(self):
    #     print("1")

    def manageProject(self):
        self.showProjects()
        selectedProject = input("Podaj ID projektu do zarządzania: ")
        projectManage = Project(selectedProject, self.user_id)
        projectManage.menu()

    def showDrawings(self):
        drawingsQuery = "select d.id_drawings, drawing_name, drawing_num, width, height, individual_rate,project_name" \
                        " from drawings as d left join projects as p on (d.id_projects=p.id_projects) " \
                        "join projects_has_users as phu on (phu.projects_id_projects = p.id_projects) " \
                        "where Users_id_Users = "+ str(self.user_id) + ";"
        result = self.db.fetchAll(drawingsQuery)
        print('|%3s|%40s|%20s|%20s|%20s|%20s|%20s' %
              ("ID", "Nazwa rysunku", "Numer rysunku", "Szerokość rys.", "Wysokość rys.", "stawka za A0 [PLN]", "Nazwa projektu"))
        for row in result:
            print('|%3i|%40s|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def showUnpaidDrawings(self):
        drawingsQuery = "select d.id_drawings, drawing_name, drawing_num, width, height, individual_rate,project_name" \
                        " from drawings as d left join projects as p on (d.id_projects=p.id_projects) " \
                        "join projects_has_users as phu on (phu.projects_id_projects = p.id_projects) " \
                        "where (Users_id_Users = " + str(self.user_id) + " AND paid =0);"
        result = self.db.fetchAll(drawingsQuery)
        print('|%3s|%40s|%20s|%20s|%20s|%20s|%20s' %
              ("ID", "Nazwa rysunku", "Numer rysunku", "Szerokość rys.", "Wysokość rys.", "stawka za A0 [PLN]",
               "Nazwa projektu"))
        for row in result:
            print('|%3i|%40s|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    def showPaidDrawings(self):
        drawingsQuery = "select d.id_drawings, drawing_name, drawing_num, width, height, individual_rate,project_name" \
                        " from drawings as d left join projects as p on (d.id_projects=p.id_projects) " \
                        "join projects_has_users as phu on (phu.projects_id_projects = p.id_projects) " \
                        "where (Users_id_Users = " + str(self.user_id) + " AND paid =1);"
        result = self.db.fetchAll(drawingsQuery)
        print('|%3s|%40s|%20s|%20s|%20s|%20s|%20s' %
              ("ID", "Nazwa rysunku", "Numer rysunku", "Szerokość rys.", "Wysokość rys.", "stawka za A0 [PLN]",
               "Nazwa projektu"))
        for row in result:
            print('|%3i|%40s|%20s|%20s|%20s|%20s|%20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))