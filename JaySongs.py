import pymysql
import sys
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='jaycoh',
)
def add():
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    genre = input("Enter what kind of song: ")
    duration = input("Enter time duration: ")
 
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO songs (`title`, `artist`, `genre`, `duration`) VALUES (%s, %s, %s, %s)"
            try:
                cursor.execute(sql, (title, artist, genre, duration))
                print("New Song List Successfully Added")
            except:
                print("Hey! Something went wrong..")
                
        connection.commit()
    finally:
        print ("\n")
        return

def read():
    print ("DATA\n")
    try:
        with connection.cursor() as cursor:
            sql = "select * from songs"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            print("Id\tTitle\t\t\tArtist\t\t\tGenre\t\t\tDuration")
            print("---------------------------------------------------------------------------")
            for row in results :
                print(str(row[0]) + "\t" + row[1] + "\t\t" + (row[2]) + "\t\t" + row[3] + "\t\t\t" , row[4])

        connection.commit()
    finally:
        print ("")
        return
def update():
    read()
    print("")
    id = input("Enter the id of the song to update: ")
    title = input("Enter new title: ")
    artist = input("Enter new artist name: ")
    genre = input("Enter new genre: ")
    duration = input("Enter new duration: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE songs SET `title`=%s, `artist`=%s , `genre`=%s, `duration`=%s WHERE `id` = %s"
            try:
                cursor.execute(sql, (title, artist, genre, duration, id))
                print("Successfully Updated...")
            except:
                print("Hey! Something went wrong..")
 
        connection.commit()
    finally:
        print ("")
        return
def delete():
    read()
    print("")
    id = input("Enter the id of the song to delete: ")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM songs WHERE id = %s"
            try:
                cursor.execute(sql, (id))
                print("Successfully Deleted...")
            except:
                print("Hey! Something went wrong..")
 
        connection.commit()
    finally:
        print ("")
        return
def search():
    print("\n")
    id = input("Enter the song id you want to search: ")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from songs WHERE id = %s"
            try:
                cursor.execute(sql, (id))
                result = cursor.fetchall()
                print("Id\tTitle\t\t\tArtist\t\t\tGenre\t\t\tDuration")
                print("---------------------------------------------------------------------------")
                for row in result:
                    print(str(row[0]) + "\t" + row[1] + "\t\t" + (row[2]) + "\t\t" + row[3] + "\t\t\t" , row[4])
            except:
                print("Hey! Something went wrong..")

        connection.commit()
    finally:
        print("")
        return
def logoff():
    sys.exit(0)

choice = 1
while choice:
    print ("***JAY SONG LIST***\n\n")
    print ("[1] = Create a new data\n")
    print ("[2] = Read data\n")
    print ("[3] = Update data\n")
    print ("[4] = Delete data\n")
    print ("[5] = Search data\n")
    print ("[6] = Exit\n")

    choice = input("Choices: ")

    if choice == "1":
        add()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        search()
    elif choice == "6":
        logoff()
        
    else:
        print ("Invalid Input!\n")
        choice = 1
