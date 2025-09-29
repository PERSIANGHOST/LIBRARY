# 1404/ 6/ 24
# 2025/ september/ 15
from colorama import Fore, Style, init
init() 

def line(char1="=", length1 =50):
    print(Fore.RED + char1 * length1 + Style.RESET_ALL)

def l_line(char2="-",length2=20):
    print(Fore.RED + char2 * length2 + Style.RESET_ALL)

class Library:
    book_counter = 1000

    def __init__(self):
        self.book = {}
    

    def add_book(self, title, author):
        book_id = Library.book_counter
        Library.book_counter += 1
        book_data = {"Title": title, "Author": author, "Available": True}
        self.book[book_id] = book_data
        print(f"\nکتاب با آی دی = {Fore.GREEN}{book_id}{Style.RESET_ALL}, نام = {title}, نویسنده = {author} اضافه شد ✅")
        line()
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

class User:
    member_counter = 1000

    def __init__(self):
        self.member = {}

    def add_member(self, name, N_phone):
        member_id = User.member_counter 
        User.member_counter += 1
        member_data = {"Name" : name , "Phone number" : N_phone}
        self.member[member_id] = member_data
        print(f"\nشما با نام {name} و آی دی {Fore.GREEN}{member_id}{Style.RESET_ALL} عضو شدید ✅")
        print("خوش آمدید 😉")
        line()
        return member_id

    def delete_member(self, member_id):
        if member_id in self.member:
            del self.member[member_id]
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
            l_line()
            print("1. اضافه کردن کتاب")
            l_line()
            print("2. مشاهده کتاب ")
            l_line()
            print("3. نمایش همه ی کتاب ها")
            l_line()
            print("4. حذف کتاب")
            l_line()
            print("5. اضافه کردن عضو")
            l_line()
            print("6. حذف عضو")
            l_line()
            print("7. خروج")
            l_line()

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
                book_id = int(input(" آی دی کتاب مورد را وارد کنید : "))
                self.library.delete_book(book_id)
            #====================
            elif choice == "5":
                name = input(" نام: ")
                phone = input(" شماره تماس : ")
                self.users.add_member(name, phone)
            #====================
            elif choice == "6":
                member_id = int(input(" آی دی مورد نظر را وارد کنید : "))
                self.users.delete_member(member_id)
                #====================
            elif choice == "7":
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
