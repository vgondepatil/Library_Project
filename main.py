
import datetime

all_studs = []
all_books = []
all_issued = []

class StudentInfo:
    senroll = None
    sname = None
    sclass = None
    smob = None
    semail = None
    def accept_stud_info(self):
        self.senroll = input("Enter Enrollment Number : ")
        self.sname = input("Enter Student Name : ")
        self.sclass = input("Enter Student Class : ")
        self.smob = input("Enter Student Mobile Number : ")
        self.semail = input("Enter Student Email : ")
class BookInfo:
    bnum = None
    btitle = None
    bauthor = None
    bpublication = None
    def accept_book_info(self):
            self.bnum = input("Enter Book Number : ")
            self.btitle = input("Enter Book Title : ")
            self.bauthor = input("Enter Book Author : ")
            self.bpublication = input("Enter Book Publication : ")
class IssueInfo:
    bknum = None
    stenroll = None
    idate = None
    rdate = None
    def accept_issue_info(self):
            self.bknum = input("Enter Book number to Issue : ")
            self.stenroll = input("Enter Student Enrollment number to Issue : ")
            self.idate = str(datetime.date.today())
            self.rdate = None
def issue_book():
    i1 = IssueInfo()
    i1.accept_issue_info()
    all_issued.append(i1)
    print("Book Issued..>!")
def return_book():
    ret_bk = input("Enter Book number, which you want to return : ")
    for ob in all_issued:
        if ob.bknum == ret_bk and ob.rdate == None:
                ob.rdate = str(datetime.date.today())
def not_ret_books():
    # i check in issued_books[]
    # and the book where rdate = None will be my answer
    for ob in all_issued:
            if ob.rdate==None:
                     print(ob.bknum, "\t", ob.stenroll, "\t", ob.idate)
def add_new_student():
    s1 = StudentInfo()
    s1.accept_stud_info()
    all_studs.append(s1)
    print("New student added...!")
def add_new_book():
    b1 = BookInfo()
    b1.accept_book_info()
    all_books.append(b1)
    print("New Book added...!")
def search_book():
    pass
def search_stud():
    pass
def book_history():
    count = 0
    bkno = input("Enter Book number, whose history you want to print : ")
    for ob in all_issued:
        if ob.bknum == bkno:
             count = count + 1
def stud_history():
    pass
def send_remainer():
    pass

# main area starts from here
while True:
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Check for not returned books")
    print("4 - Add new Student")
    print("5 - Add new Book")
    print("6 - Search Book Info")
    print("7 - Search Student Info")
    print("8 - Book History")
    print("9 - Student History")
    print("0 - Send return remainders")
    print("* - EXIT")
    ch = input("Provide your choice : ")
    if ch=="1":
        issue_book()
    elif ch=="2":
        return_book()
    elif ch=="3":
        not_ret_books()
    elif ch=="4":
        add_new_student()
    elif ch=="5":
        add_new_book()
    elif ch=="6":
        search_book()
    elif ch=="7":
        search_stud()
    elif ch=="8":
        book_history()
    elif ch=="9":
        stud_history()
    elif ch=="0":
        send_remainer()
    elif ch=="*":
        exit(0)
