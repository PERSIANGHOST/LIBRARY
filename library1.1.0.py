#1404/7/ 6
#2025/september/ 28
"""
version : 1.1.0
Features :
- save in json and csv files
- search books by ID
"""
from colorama import Fore, Style, init
init() 
import json
import csv

def line(char1="=", length1 =50):
    print(Fore.RED + char1 * length1 + Style.RESET_ALL)

def l_line(char2="-",length2=20):
    print(Fore.RED + char2 * length2 + Style.RESET_ALL)

class Library:
    book_counter = 1000
    BOOK_JSON = "books_file.json"
    BOOK_CSV = "book_file.csv"

    def __init__(self):
        try:
            with open(self.BOOK_JSON, "r", encoding="utf-8") as l_b_j:
                self.book = {int(k): v for k, v in json.load(l_b_j).items()}
        except FileNotFoundError:
            self.book = {}

        try:
            with open(self.BOOK_CSV, "r", encoding="utf-8") as l_b_c:
                reading = csv.DictReader(l_b_c)
                for row in reading:
                    book_id = int(row["ID"])
                    self.book[book_id] = {
                        "Title": row["Title"],
                        "Author": row["Author"],
                        "Available": row["Available"] == "True"
                    }
        except FileNotFoundError:
            pass

    def save_books_json(self):
        with open(self.BOOK_JSON, "w", encoding="utf-8") as l_b_j:
            json.dump(self.book, l_b_j, ensure_ascii=False, indent=2)

    def save_books_csv(self):
        with open(self.BOOK_CSV, "w", newline='', encoding="utf-8") as l_b_c:
            writer = csv.DictWriter(l_b_c, fieldnames=["ID", "Title", "Author", "Available"])
            writer.writeheader()
            for book_id, data in self.book.items():
                writer.writerow({"ID": book_id, **data})

    def save_books(self):
        self.save_books_csv()
        self.save_books_json()

    def add_book(self, title, author):
        book_id = Library.book_counter
        if self.book:
            Library.book_counter = max(self.book.keys()) + 1
        book_data = {"Title": title, "Author": author, "Available": True}
        self.book[book_id]  = book_data
        self.save_books()
        #====================
        print(f"\nکتاب با آی دی = {Fore.GREEN}{book_id}{Style.RESET_ALL}, نام = {title}, نویسنده = {author} اضافه شد ✅")
        line()
        #====================
        return book_id

    def show_book(self, book_id):
        if book_id in self.book:
            book_data = self.book[book_id]
            print(
                Fore.YELLOW  
                +f"\nکتاب {book_id}: {book_data}" 
                + Style.RESET_ALL
                    )
            line()
            return book_data
        else:
            print("\nدر حال خاضر کتابی در لیست نمیباشد ❗")    
            line()
            return None    

    def show_books(self):
        if not self.book:
            print("\n📕 هیچ کتابی در لیست موجود نیست ❗")
            line()
            return

        print(Fore.CYAN + "\n📚 لیست کتاب‌ها:" + Style.RESET_ALL)
        for book_id, book_data in self.book.items():
            status = "✅ موجود" if book_data["Available"] else "❌ امانت داده شده"
            print(
                Fore.YELLOW
                + f"آی دی : {book_id} \n نام کتاب : {book_data['Title']} \n نویسنده : {book_data['Author']} \n وضعیت: {status}"
                + Style.RESET_ALL
                    )
        line()

    def delete_book(self, book_id):
        if book_id in self.book:
            del self.book[book_id]
            self.save_books()
            print(
                Fore.CYAN  
                +f"\nکتاب با آی دی {book_id} حذف شد ✅" 
                + Style.RESET_ALL
                    )
            line()
        else:
            print(
                Fore.CYAN 
                +f"\nکتاب با آی دی {book_id} پیدا نشد ❌" 
                + Style.RESET_ALL
                    )
            line()

    def search_books(self, book_id):
        if book_id in self.book:
            print(Fore.GREEN + f"\n کتاب مورد نظر پیدا شد : {self.book[book_id]}" +Style.RESET_ALL)
            line()
            return self.book[book_id]
        else:
            print(Fore.RED + "\n کتاب مورد نظر پیدا نشد ❌" + Style.RESET_ALL)
            line()
            return None
    
class User:
    member_counter = 1000
    MEMBER_JSON = "members_file.json"
    MEMBER_CSV = "members_file.csv"

    def __init__(self):
        try:
            with open(self.MEMBER_JSON, "r", encoding="utf-8") as u_m_j:
                self.member = {int(k): v for k, v in json.load(u_m_j).items()}
        except FileNotFoundError:
            self.member = {}

        try:
            with open(self.MEMBER_CSV, "r", encoding="utf-8") as u_m_c:
                reading = csv.DictReader(u_m_c)
                for row in reading:
                    member_id = int(row["ID"])
                    self.member[member_id] = {
                        "Name": row["Name"],
                        "PhoneNumber": row["N_phone"]
                    }
        except FileNotFoundError:
            pass

    def save_members_json(self):
        with open(self.MEMBER_JSON, "w", encoding="utf-8") as u_m_j:
            json.dump(self.member, u_m_j, ensure_ascii=False, indent=2)

    def save_members_csv(self):
        with open(self.MEMBER_CSV, "w", newline='', encoding="utf-8") as u_m_c:
            wrier = csv.DictWriter(u_m_c, fieldnames=["ID", "Name", "PhoneNumber"])
            wrier.writeheader()
            for member_id, data in self.member.items():
                wrier.writerow({"ID": member_id, **data})

    def save_members(self):
        self.save_members_csv()
        self.save_members_json()

    def add_member(self, name, N_phone):
        member_id = User.member_counter 
        if self.member:
            User.member_counter = max(self.member.keys()) + 1
        member_data = {"Name" : name , "PhoneNumber" : N_phone}
        self.member[member_id] = member_data
        self.save_members()
        print(f"\nشما با نام {name} و آی دی {Fore.GREEN}{member_id}{Style.RESET_ALL} عضو شدید ✅")
        print("خوش آمدید 😉")
        line()
        #====================
        return member_id
    
    def delete_member(self, member_id):
        if member_id in self.member:
            del self.member[member_id]
            self.save_members()
            print(
                Fore.CYAN  
                +f"\n عضوی با آی دی {member_id} حذف شد ✅" 
                + Style.RESET_ALL
                    )
            line()
        else:
            print(
                Fore.CYAN 
                +f"\nعضوی با آی دی {member_id} پیدا نشد ❌"
                + Style.RESET_ALL
                    )
            line()

class Menu:
    def __init__(self, library, users):
        self.library = library
        self.users = users

    def main_menu(self):
        while True:
            print("\n--- منوی اصلی ---")
            l_line() #--------------------
            print("1. اضافه کردن کتاب")
            l_line() #--------------------
            print("2. مشاهده کتاب ")
            l_line() #--------------------
            print("3. نمایش همه ی کتاب ها")
            l_line() #--------------------
            print("4. جستجو کتاب ها ")
            l_line() #--------------------
            print("5. حذف کتاب")
            l_line() #--------------------
            print("6. اضافه کردن عضو")
            l_line() #--------------------
            print("7. حذف عضو")
            l_line() #--------------------
            print("8. خروج")
            l_line() #--------------------

            choice = input("گزینه مورد نظر را وارد کنید : ")

            if choice == "1":
                title = input("نام کتاب : ")
                author = input("نام نویسنده : ")
                self.library.add_book(title, author)
            #====================
            elif choice == "2":
                book_id = int(input("آی دی کتاب مورد نظر را وارد کنید : "))
                self.library.show_book(book_id)
            #====================
            elif choice == "3":
                self.library.show_books()
            #====================
            elif choice == "4":
                try:
                    book_id = int(input(" آی دی کتاب مورد نظر را وارد کنید : "))
                    self.library.search_books(book_id)
                except ValueError:
                    print(Fore.RED + " لطفا یک عدد معتبر وارد کنید ! " + Style.RESET_ALL)
            #====================
            elif choice == "5":
                book_id = int(input(" آی دی کتاب مورد را وارد کنید : "))
                self.library.delete_book(book_id)
            #====================
            elif choice == "6":
                name = input(" نام: ")
                phone = input(" شماره تماس : ")
                self.users.add_member(name, phone)
            #====================
            elif choice == "7":
                member_id = int(input(" آی دی مورد نظر را وارد کنید : "))
                self.users.delete_member(member_id)
                #====================
            elif choice == "8":
                print("خدا نگهدار")
                break
            #====================
            else:
                print("گزینه نامعتبر است ❌")
                line()

library = Library()
users = User()
#====================
menu = Menu(library, users)
#====================
menu.main_menu()
