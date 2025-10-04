#1404/ 7/ 11
#2025/ October/ 3
"""
version : 1.1.1
Features :
1. Book and Member Counters Fixed:
---book_counter and member_counter now correctly find the latest ID in use and 
    increment it to avoid duplicate IDs.
2. Improved Message Display:
---Added clear and colored messages when adding books/members.
---Display messages when searching 
    or showing a book/member are more user-friendly and colored.
---or showing a book/member are more user-friendly and colored.
3. Delete Multiple Books/Members at Once:
---User can now input multiple IDs separated by commas (e.g., 1,2,3) for deletion.
---Proper error handling if an ID does not exist.
4. Input Validation:
---Non-numeric input in search and deletion triggers a warning message.
---Member phone numbers are validated to be 11 digits and start with 09.
5. Consistent Saving:
---Books and members are saved in both JSON and CSV formats.
6. Menu Style and Readability:
---Added colored lines (line() and l_line()) for a more structured and readable menu.
7. Colored Menu and Separators:
---Added color formatting to menu items and separator lines for better readability.
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
        if self.book:
            Library.book_counter = max(self.book.keys()) + 1
        book_id = Library.book_counter
        Library.book_counter += 1
        book_data = {"Title": title, "Author": author, "Available": True}
        self.book[book_id]  = book_data
        self.save_books()
        #====================
        print(
                Fore.GREEN
                + f"\nکتاب با آی دی = {book_id}, نام = {title}, نویسنده = {author} اضافه شد ✅"
                + Style.RESET_ALL
                )
        line()
        #====================
        return book_id

    def show_book(self, book_id):
        if not self.book:
            print(
                Fore.RED
                + "\nدر حال خاضر کتابی در لیست نمیباشد ❗"
                + Style.RESET_ALL
                    )
            line()
            return None
        
        if book_id in self.book:
            book_data = self.book[book_id]
            print(
                Fore.GREEN
                +f"\nکتاب {book_id}: {book_data}" 
                + Style.RESET_ALL
                    )
            line()
            return book_data
        else:
            print(
                Fore.RED
                + f"\n کتابی با آی دی {book_id} پیدا نشد ❗"
                +Style.RESET_ALL
                    )
            line()
            return None    

    def show_books(self):
        if not self.book:
            print(
                    Fore.RED 
                    + "\n📕 هیچ کتابی در لیست موجود نیست ❗"
                    + Style.RESET_ALL
                    )
            line()
            return

        print(Fore. BLACK
                + "\n📚 لیست کتاب‌ها:" 
                + Style.RESET_ALL
                )
        for book_id, book_data in self.book.items():
            status = "✅ موجود" if book_data["Available"] else "❌ امانت داده شده"
            print(
                Fore.GREEN
                + f"آی دی : {book_id} \n نام کتاب : {book_data['Title']} \n نویسنده : {book_data['Author']} \n وضعیت: {status}"
                + Style.RESET_ALL
                    )
        line()

    def delete_books(self, book_ids):
        for book_id in book_ids:
            if book_id in self.book:
                del self.book[book_id]
                print(
                    Fore.GREEN
                    +f"کتاب با آی دی {book_id} با موفقیت حذف شد ✅"
                    + Style.RESET_ALL
                        )
            else:
                print(
                    Fore.RED
                    +f"\nکتاب با آی دی {book_id} پیدا نشد ❌" 
                    + Style.RESET_ALL
                        )
        self.save_books()
        line()

    def search_books(self, book_id):
        if not self.book:
            print(
                Fore.RED
                + "\nدر حال خاضر کتابی در لیست نمیباشد ❗"
                + Style.RESET_ALL
                )
            line()
            return None
        
        if book_id in self.book:
            print(
                Fore.GREEN
                + f"\n کتاب مورد نظر پیدا شد : {self.book[book_id]}" 
                +Style.RESET_ALL
                )
            line()
            return self.book[book_id]
        else:
            print(
                Fore.RED
                + "\n کتاب مورد نظر پیدا نشد ❌" 
                + Style.RESET_ALL
                    )
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

    def add_member(self, name, phone):
        if not phone.isdigit() or len(phone) != 11 or not phone.startswith("09"):
            print(
                Fore.RED
                +"\n شماره تماس معتبر نیست ❌"
                +Style.RESET_ALL
                    )
            line()
            return None
        #====================
        if self.member:
            User.member_counter = max(self.member.keys()) + 1
        member_id = User.member_counter 
        User.member_counter += 1
        member_data = {"Name" : name , "PhoneNumber" : phone}
        self.member[member_id] = member_data
        self.save_members()
        print(Fore.GREEN
                + f"\nشما با نام {name} و آی دی {member_id} عضو شدید ✅"
                + Style.RESET_ALL
                )
        print(
                Fore.GREEN
                + "خوش آمدید 😉"
                + Style.RESET_ALL
                )
        line()
        #====================
        return member_id
    
    
    def delete_members(self, member_ids):
        for member_id in member_ids:
            if member_id in self.member:
                del self.member[member_id]
                print(
                    Fore.GREEN
                    +f"\n عضوی با آی دی {member_id} با موفقیت حذف شد ✅" 
                    + Style.RESET_ALL
                        )
            else:
                print(
                    Fore.RED 
                    +f"\nعضوی با آی دی {member_id} پیدا نشد ❌"
                    + Style.RESET_ALL
                        )
        self.save_members()
        line()

class Menu:
    def __init__(self, library, users):
        self.library = library
        self.users = users

    def main_menu(self):
        while True:
            print(
                Fore.BLACK
                + "\n--- منوی اصلی ---"
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "1. اضافه کردن کتاب"
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "2. مشاهده کتاب "
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "3. نمایش همه ی کتاب ها"
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "4. جستجو کتاب ها "
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "5. حذف کتاب"
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "6. اضافه کردن عضو"
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "7. حذف عضو"
                + Style.RESET_ALL
                    )
            l_line() #--------------------
            print(
                Fore.BLACK
                + "8. خروج"
                + Style.RESET_ALL
                    )
            l_line() #--------------------

            choice = input(
                                    Fore.BLACK 
                                    + "گزینه مورد نظر را وارد کنید : "
                                    + Style.RESET_ALL
                                    )

            if choice == "1":
                title = input(
                                    Fore.CYAN
                                    + "نام کتاب : "
                                    + Style.RESET_ALL
                                    )
                author = input(
                                        Fore.CYAN
                                        + "نام نویسنده : "
                                        + Style.RESET_ALL
                                        )
                self.library.add_book(title, author)
            #====================
            elif choice == "2":
                book_id = int(input(
                                                Fore.CYAN
                                                + "آی دی کتاب مورد نظر را وارد کنید : "
                                                + Style.RESET_ALL)
                                                )
                self.library.show_book(book_id)
            #====================
            elif choice == "3":
                self.library.show_books()
            #====================
            elif choice == "4":
                try:
                    book_id = int(input(
                                                    Fore.CYAN
                                                    +" آی دی کتاب مورد نظر را وارد کنید : "
                                                    + Style.RESET_ALL)
                                                    )
                    self.library.search_books(book_id)
                except ValueError:
                    print(
                            Fore.RED 
                            + " لطفا یک عدد معتبر وارد کنید ! " 
                            + Style.RESET_ALL
                            )
            #====================
            elif choice == "5":
                b_input = input   (
                                            Fore.CYAN
                                            + "(جدا شده با ,) آی دی کتاب های مورد نظر را وارد کنید : "
                                            + Style.RESET_ALL
                                            )
                try:
                    book_id = [int(x.strip()) for x in b_input.split(",")]
                    self.library.delete_books(book_id)
                except ValueError:
                        print(
                                Fore.RED 
                                + "لطفا عدد وارد کنید و لطفا فاصله گذاری را رعایت کنید" 
                                + Style.RESET_ALL
                                )
            #====================
            elif choice == "6":
                name = input(
                                        Fore.CYAN
                                        +" نام: "
                                        + Style.RESET_ALL
                                        )
                phone = input(
                                        Fore.CYAN
                                        + " شماره تماس : "
                                        + Style.RESET_ALL
                                        )
                self.users.add_member(name, phone)
            #====================
            elif choice == "7":
                m_input = input (
                                            Fore.CYAN
                                            +"(جدا شده با)(,)) آی دی اعضای مورد نظر را وارد کنید : "
                                            + Style.RESET_ALL
                                            )
                try:
                    member_id = [int(y.strip()) for y in m_input.split(",")]
                    self.users.delete_members(member_id)
                except ValueError:
                        print( 
                                Fore.RED 
                                + "لطفا عدد وارد کنید و لطفا فاصله گذاری را رعایت کنید"
                                + Style.RESET_ALL
                                )
                #====================
            elif choice == "8":
                print(
                        Fore.BLUE
                        + "خدا نگهدار"
                        + Style.RESET_ALL
                        )
                break
            #====================
            else:
                print(
                        Fore.RED 
                        + "گزینه نامعتبر است ❌"
                        + Style.RESET_ALL
                        )
                line()

library = Library()
users = User()
#====================
menu = Menu(library, users)
#====================
menu.main_menu()

