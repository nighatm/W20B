import mariadb
import dbcreds

################################################(LOGIN) #########################################################

def log_in(username, password):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user= dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database= dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias=?, password=?", [username, password,])
        hacker=cursor.fetchall()
        if cursor.count == 1:
            for hacker in hackers:
                print("Welcome.." + hacker[0])
                return True
        else:
            return False
    except mariadb.ProgrammingError:
        print("You have a programming error, check your code!")
    except mariadb.OperationalError:
        print("A connection error!")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
################################################(SIGNUP) #########################################################
def signup(username, password):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user= dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database= dbcreds.database)
        cursor = conn.cursor()
        if(len(password) < 6):
            print("Password has to be 6  digits/characters long or more..")
        else:
            cursor.execute("INSERT INTO hackers(alias, password) VALUES(?,?)", [username, password])
            conn.commit()

        if cursor.rowcount == 1:
            print("Congrats, hacker registered")
            print("-----------------------------")
        else:
            print("oops! hacker not created")

    except mariadb.ProgrammingError:
        print("You have a programming error, check your code!")
    except mariadb.OperationalError:
        print("A connection error!")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()

##############################################(INSERT DATA)###########################################################


def insert_data(username, content):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user= dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database= dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ?", [username, ])
        userid=cursor.fetchone()
        cursor.execute("INSERT INTO exploits(content, user_id) VALUES(?,?)", [content, userid[0]])
        conn.commit()

        if(cursor.rowcount==1):
            print("Exploit created")
            print("---------------")
        else:
            print("oops..Exploit not created")
    except mariadb.ProgrammingError:
        print("You have a programming error, check your code!")
    except mariadb.OperationalError:
        print("A connection error!")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
#############################################(GET SINGLE POST)############################################################3
def get_exploit(username):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user= dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database= dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ?", [username, ])
        userid=cursor.fetchone()
        cursor.execute("SELECT * FROM exploits WHERE user_id = ?", [userid[0], ])
        exploits = cursor.fetchall()
        for exploit in exploits:
            print("Here are your exploits: " + str(exploits))
            print("------------------------------")
        if (cursor.rowcount == 0):
            print("No exploit found")

    except mariadb.ProgrammingError:
        print("You have a programming error, check your code!")
    except mariadb.OperationalError:
        print("A connection error!")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
#########################################(GET ALL POSTS) #####################################################
def get_allexploits(username):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user= dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database= dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ?", [username, ])
        hackers=cursor.fetchall()

        for hacker in hackers:
            cursor.execute("SELECT * FROM exploits WHERE user_id = ?", [hacker[0], ])
            hackers= cursor.fetchall()
            print("Here are other hacker's exploits: " +str(hacker))
        if (cursor.rowcount == 0):
            print("No exploit found")

    except mariadb.ProgrammingError:
        print("You have a programming error, check your code!")
    except mariadb.OperationalError:
        print("A connection error!")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()

#######################################(EXIT METHOD)#####################################################3
# def exit_code():
#     while True:
#         check = input("To continue or not.. enter Y for (yes) or N for (no): ")
#         if (check == "Y" or "y"):
#             return False
#         elif (check == "N" or "n"):
#             return True
#             # break
#             # sys.exit()
#             # sys.quit()
#             # for some reason none of my exit code funtion worked! have tried bunch of different stuff 

  

    