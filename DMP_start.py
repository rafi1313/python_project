import pymysql
from User import User


class Login:
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', 'SqlAccount!23', 'DMP', charset='utf8')
        self.c = self.conn.cursor()
        print('połączenie ustanowione!')
        self.menu()

    def menu(self):
        print("Witamy Cię w Programie zarządzania rysunkami DMP:\n")
        loop = True
        while loop:
            option = input("Wybierz opcję: Z-zaloguj, N-nowy użytkownik,Q-wyjście:").upper()
            while option == "":
                option = input("Wybierz opcję działania: Z-zaloguj, N-nowy użytkownik,Q-wyjście: ").upper()
            if option == "Q":
                loop = False
            elif option == "N":
                login = input("Podaj login dla nowego użutkowsnika: ")
                password = input("Podaj hasło dla nowego użytkownika: ")
                self.c.execute(
                    "INSERT INTO USERS (login_users, pass_users) values ('" + login + "', '" + password + "');")
                self.logIn(login, password)
            elif option == "Z":
                login = input("Podaj login: ")
                password = input("Podaj hasło: ")
                self.logIn(login,password)
            elif option == "Q":
                loop = False
            else:
                print("Brak takiej opcji!")

    def logIn(self, _login, _password):

        self.c.execute("SELECT * FROM USERS WHERE login_users = '" + _login + "' AND pass_users = '" + _password + "';")
        logRes = self.c.fetchall()
        if len(logRes) == 1:
            print("Zalogowano!")
            # print(logRes)
            logRes_id = logRes[0]
            currentUser = User(logRes[0][0])
        else:
            print("Niepoprawne login lub/i hasło!")

# start programu
start = Login()

