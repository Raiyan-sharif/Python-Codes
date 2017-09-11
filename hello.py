import  sqlite3
db=sqlite3.connect("information.db")
def CreateTable():
    db.row_factory = sqlite3.Row
    db.execute("CREATE TABLE if not EXISTS Admin(Name text,Age int)")
    db.commit()
def Add(Name,Age):
    db.row_factory = sqlite3.Row
    db.execute("CREATE TABLE if not EXISTS Admin(Name text,Age int)")
    db.execute("INSERT INTO Admin(Name,Age) VALUES (?,?)", (Name, Age))
    db.commit()
    print("Record is added")

def ListAdmin():
    print("Data fatched from the database")
    cursor=db.execute("SELECT  * from Admin")
    for row in cursor:
        print("Name:{},Age:{}".format(row["Name"],row["Age"]))

def main():
    CreateTable()
    IndexOp=int(input("Select Option 1- Add:\n2- List Admin:"))
    if(IndexOp==1):
        Name=input("Enter name")
        Age=int(input("Enter Age:"))
        Add(Name,Age)
    elif(IndexOp==2):
        ListAdmin()

if __name__=="__main__":main()
