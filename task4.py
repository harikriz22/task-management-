import sqlite3
conn = sqlite3.connect("task_management1.db")
cursor = conn.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS user(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     username VARCHAR UNIQUE,
     password TEXT
    )
    ''')


cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            task_name VARCHAR(20),
            task_des TEXT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
        ''')

conn.close()

def register():
    conn = sqlite3.connect("task_management1.db")
    cursor = conn.cursor()
    username = input("enter username:-")
    password = input("enter password:-")

    cursor.execute('''
        INSERT INTO user(username,password)
            VALUES(?,?)
        ''',(username,password))

    conn.commit()
    print("user registered")


def login():
    conn = sqlite3.connect("task_management1.db")
    cursor = conn.cursor()

    username = input("enter username :")
    password = input("enter password :")

    cursor.execute('''
        SELECT id FROM user WHERE username = ? AND password = ?

        ''',(username,password))

    user = cursor.fetchone()
    if user:
        print("logged in successfully")
        return user[0]
    else:
        print("no such user ")



def addtask(user_id):
    conn = sqlite3.connect("task_management1.db")
    cursor = conn.cursor()
    tname = input("enter task name: - ")
    tdes = input("enter task des : - ")

    cursor.execute('''
            INSERT INTO Tasks(task_name,task_des,user_id)
            VALUES(?,?,?)
    ''',(tname,tdes,user_id))
    conn.commit()


def viewtasks():
    conn = sqlite3.connect("task_management1.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Tasks
        ''')
    tasks = cursor.fetchall()#retrives a list of data from the last executed querry  
    if tasks:
        print("tasks found 😂")
        for i in tasks:
            print(i[1])
    else:
        print("no current tasks 😒")

def  findtask():
    conn = sqlite3.connect("task_management1.db")
    cursor = conn.cursor()
    t_id = int(input("enter task id : "))
    cursor.execute('''
        SELECT * FROM Tasks WHERE id = ?
        ''',(t_id,))
    task = cursor.fetchone()
    print(task)
    if task:
        print("task found 🤗")
        print(f"task - {task[1]} des - {task[2]}")
    else:
        print("no such tasks ❌")

def updatetasks():
    conn = sqlite3.connect("task_management1.db")
    cursor = conn.cursor()
    t_id = int(input("enter task id : "))
    tname = input("enter taskname:-")
    tdes = input("enter taskdes:-")
    cursor.execute('''
        UPDATE Tasks set task_name = ? , task_des = ? WHERE id = ?
    ''',(tname,tdes,t_id))
    conn.commit()
    print("task updated")

def deletetasks():
    conn = sqlite3.connect("task_management1.db")
    cursor = conn.cursor()
    t_id = int(input("enter task id : "))
    ch = input("Are you sure you want tode delete this task\nY/N").lower()
    if ch == "y":   
        cursor.execute('''

            DELETE FROM Tasks WHERE id = ?
            ''',(t_id,))
        conn.commit()
        print("task delete!!!!!")
    else:
        print("task not deleted")



def dash():
    print("Welcome !!!")
    while True:
        ch = int(input("please select an option :\n1.Register\n2.Login :-"))
        if ch == 1:
            register()
        elif ch == 2:
            user_id = login() 
            if user_id:
                main1(user_id)

        elif ch == 3:
            break
        else:
            print("invalid option")

    

def main1(user_id):
    print("Welcome to task management system")
    while True:
        print("choose your option")
        ch = int(input("1.Add tasks\n2.View task\n3.find tasks\n4.update tasks\n5.delete task\n6.exit :-"))
        if ch == 1:
            addtask(user_id)
        elif ch == 2:
            viewtasks()
        elif ch == 3:
            findtask()
        elif ch == 4:
            updatetasks()
        elif ch == 5:
            deletetasks()
        elif ch == 6 :
            break
        else:
            print("invalid option")

dash()