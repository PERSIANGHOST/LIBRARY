#1404/ 7/ 24
#2025/ October/ 16
"""
============================================
Version : 1.3.0
============================================

📦 Features (English):
1. Code Refactored into Class Structure:
    └── All extraction functions (emails, phones, URLs) are now inside a single class (DataExtractor)
    └── Improved modularity and readability for future updates

--------------------------------------------
2. Automatic Folder Creation:
    └── Automatically creates 'outputs' folder if it doesn’t exist

--------------------------------------------
3. File Naming by Current Date:
    └── Output files are named with the current date (e.g., data_20251005.json)
    └── Helps organize saved data by extraction date

--------------------------------------------
4. User Choice for Output Format:
    └── User can choose between JSON, CSV, or BOTH
    └── Invalid input defaults to 'both' automatically

--------------------------------------------
5. Extraction Summary Report:
    └── Displays total counts of emails, phones, and URLs
    └── Shows full path of the saved folder

--------------------------------------------
6. Improved Regex Accuracy and Case Insensitivity:
    └── Cleaner regex patterns with re.IGNORECASE for better matches

--------------------------------------------
7. Overall Code Optimization:
    └── Cleaner structure and indentation
    └── Ready for next step (v2.0.0) with web scraping support

============================================
ویژگی‌ها (فارسی):
1. بازنویسی کد در قالب کلاس:
    └── تمام توابع استخراج (ایمیل، شماره، آدرس وب) داخل یک کلاس واحد (DataExtractor) قرار گرفتند  
    └── ساختار کد منظم‌تر و آماده توسعه‌های بعدی شد  

--------------------------------------------
2. ایجاد خودکار پوشه خروجی:
    └── اگر پوشه‌ی outputs وجود نداشته باشد، به‌صورت خودکار ساخته می‌شود  

--------------------------------------------
3. نام‌گذاری فایل‌ها بر اساس تاریخ روز:
    └── فایل‌های خروجی با تاریخ روز ذخیره می‌شوند (مثلاً data_20251005.json)  
    └── برای نظم بهتر در فایل‌های ذخیره‌شده  

--------------------------------------------
4. انتخاب نوع خروجی توسط کاربر:
    └── کاربر می‌تواند بین JSON، CSV یا هر دو گزینه انتخاب کند  
    └── در صورت ورود گزینه نامعتبر، به‌طور پیش‌فرض «both» انتخاب می‌شود  

--------------------------------------------
5. نمایش خلاصه عملیات استخراج:
    └── پس از ذخیره، گزارشی از تعداد ایمیل‌ها، شماره‌ها و آدرس‌ها نمایش داده می‌شود  
    └── مسیر کامل پوشه خروجی نیز نشان داده می‌شود  

--------------------------------------------
6. بهبود دقت Regex:
    └── عبارات منظم تمیزتر شده و حساسیت به حروف بزرگ/کوچک حذف شده است  

--------------------------------------------
7. بهینه‌سازی کلی کد:
    └── ساختار کد ساده‌تر و خواناتر شده  
    └── آماده برای نسخه‌ی بعدی (v2.0.0) شامل web scraping  
============================================
"""
    # TODO1 = search book by keyword (Title and author)
    # TODO2 = Combining user login and registration
    # TODO3 = add searsh by Title or Author substring
    # TODO4 = Editing books by admins
    # TODO5 = Ability to login with password for regular users
    # TODO6 = Advanced tagging and filtering by tag
    # TODO7 = Sorting books
    # TODO8 = Advanced reporting
    # TODO9 = File communications and backups

###############################
from colorama import Fore, Style, init    #
import json                                            #
import csv                                             #
import os                                             #
#############################
os.makedirs("data", exist_ok=True)
# ==================================================
def line(char1="=", length1 =50):
    return Fore.RED + char1 * length1 + Style.RESET_ALL + "\n"
# ========================
def l_line(char2="-",length2=20):
    return Fore.RED + char2 * length2 + Style.RESET_ALL + "\n"
# ========================
def s_line(char3="*", length=30):
    return char3 * length + "\n"
# ==================================================
def red(text): # EROR
    return Fore.RED + text + Style.RESET_ALL + "\n"
# ========================
def green(text): # RESULT
    return Fore.GREEN + text + Style.RESET_ALL + "\n"
# ========================
def yellow(text): # GUIDE
    return Fore.YELLOW + text + Style.RESET_ALL + "\n"
# ========================
def cyan(text): # QUESTION
    return Fore.CYAN + text + Style.RESET_ALL + "\n"
# ========================
def blue(text): # MENU
    return Fore.BLUE + text + Style.RESET_ALL + "\n"
# ========================
def black(text):
    return Fore.BLACK + text + Style.RESET_ALL + "\n"
# ========================
def magenta(text): # QUESTION MENU
    return Fore.MAGENTA + text + Style.RESET_ALL + "\n"
# ==========================================================================
class Library:
    """ کلاس مدیریت کتابخانه: اضافه کردن ,حذف ,نمایش ,جستجو و ذخیره کتاب """
    book_counter = 1000
    BOOK_JSON = "data/books_file.json"
    BOOK_CSV = "data/book_file.csv"
    nbt = "در حال خاضر کتابی در لیست نمیباشد ❗" # nbt = not book text
# ==================================================
    def __init__(self):
        """باز کردن/ساختن فایل (json و csv)"""
        try:
            with open(self.BOOK_JSON, "r", encoding="utf-8") as l_b_j:
                self.book = {int(k): v for k, v in json.load(l_b_j).items()}
        except FileNotFoundError:
            self.book = {}
# ========================
        try:
            with open(self.BOOK_CSV, "r", encoding="utf-8") as l_b_c:
                reading = csv.DictReader(l_b_c)
                for row in reading:
                    book_id = int(row["ID"])
                    self.book[book_id] = {
                        "Title": row["Title"],
                        "Author": row["Author"]
                        }
        # ========================
        except FileNotFoundError:
            pass
# ==================================================
    def save_books_json(self):
        with open(self.BOOK_JSON, "w", encoding="utf-8") as l_b_j:
            json.dump(self.book, l_b_j, ensure_ascii=False, indent=2)
# ==================================================
    def save_books_csv(self):
        with open(self.BOOK_CSV, "w", newline='', encoding="utf-8") as l_b_c:
            writer = csv.DictWriter(l_b_c, fieldnames=["ID", "Title", "Author"])
            writer.writeheader()
            for book_id, data in self.book.items():
                writer.writerow({"ID": book_id, **data})
# ==================================================
    def save_books(self):
        self.save_books_csv()
        self.save_books_json()
# ==================================================
    def add_book(self, title, author):
        """اضافه کردن و ذخیره کتاب ها در فایل csv و json"""
        if self.book:
            Library.book_counter = max(self.book.keys(), default=999) + 1
        book_id = Library.book_counter
        Library.book_counter += 1
        book_data = {
            "Title": title,
            "Author": author,
            # "Tags": tags
        }
        self.book[book_id]  = book_data
        self.save_books()
        # ========================
        print(green(f"\nکتاب با آی دی = {book_id}, نام = {title}, نویسنده = {author} اضافه شد ✅"))
        line()
        return book_id
# ==================================================
    def add_tags(self, book_id, tags):
        if book_id not in self.book:
            print(red(self.nbt))
            return 
        current_tags = self.book[book_id].get("Tags", [])
        # ========================
        for tag in tags:
            if tag not in current_tags:
                current_tags.append(tag)
        self.book[book_id]["Tags"] = current_tags
        self.save_books()
        print(green(f" تگ ها به کتاب {book_id} اضافه شدند ✅"))
# ==================================================
    def show_book(self, book_id, ):
        """جستجو کتاب با استفاده از آی دی"""
        if not self.book:
            print(red(self.nbt))
            line()
            return None
        # ========================
        if book_id in self.book:
            book_data = self.book[book_id]
            print(green(f"\nکتاب {book_id}: {book_data}" ))
            line()
            return book_data
        # ========================
        else:
            print(red(f"\n کتابی با آی دی {book_id} پیدا نشد ❗"))
            line()
            return None    
# ==================================================
    def show_books(self, ):
        """نمایش همه ی کتاب ها """
        if not self.book:
            print(red(self.nbt))
            line()
            return
        # ========================
        print(black( "\n📚 لیست کتاب‌ها:" ))
        for book_id, book_data in self.book.items():
            print(green( f"آی دی : {book_id} \n نام کتاب : {book_data['Title']} \n نویسنده : {book_data['Author']}\n تگ : {book_data.get('Tags', [ ])}"))
        line()
# ==================================================
    def delete_books(self, book_ids):
        """حذف کتاب ها با استفاده از آی دی"""
        for book_id in book_ids:
            if book_id in self.book:
                del self.book[book_id]
                print(green(f"کتاب با آی دی {book_id} با موفقیت حذف شد ✅"))
            # ========================
            else:
                print(red(f"\nکتاب با آی دی {book_id} پیدا نشد ❌" ))
        self.save_books()
        line()
# ==================================================
    def search_books(self, book_id):
        if not self.book:
            print(red(self.nbt))
            line()
            return None
        # ========================
        if book_id in self.book:
            print(green(f"\n کتاب مورد نظر پیدا شد : {self.book[book_id]}" ))
            line()
            return self.book[book_id]
        # ========================
        else:
            print(red("\n کتاب مورد نظر پیدا نشد ❌" ))
            line()
            return None
# ==========================================================================
class User:
    """
کلاس یوزر: اضافه کردن و حذف عضو
    """
    member_counter = 1000
    MEMBER_JSON = "data/members_file.json"
    MEMBER_CSV = "data/members_file.csv"
# ==================================================
    def __init__(self):
        try:
            with open(self.MEMBER_JSON, "r", encoding="utf-8") as u_m_j:
                self.member = {int(k): v for k, v in json.load(u_m_j).items()}
        except FileNotFoundError:
            self.member = {}
        # ========================
        try:
            with open(self.MEMBER_CSV, "r", encoding="utf-8") as u_m_c:
                reading = csv.DictReader(u_m_c)
                for row in reading:
                    member_id = int(row["ID"])
                    self.member[member_id] = {
                        "Name": row["Name"],
                        "Age":row["Age"],
                        "PhoneNumber": row["PhoneNumber"],
                        "Email":row["Email"]
                    }
        except FileNotFoundError:
            self.member = {}
# ==================================================
    def save_members_json(self):
        with open(self.MEMBER_JSON, "w", encoding="utf-8") as u_m_j:
            json.dump(self.member, u_m_j, ensure_ascii=False, indent=2)
# ==================================================
    def save_members_csv(self):
        with open(self.MEMBER_CSV, "w", newline='', encoding="utf-8") as u_m_c:
            writer = csv.DictWriter(u_m_c, fieldnames=["ID", "Name", "Age", "PhoneNumber", "Email"])
            writer.writeheader()
            for member_id, data in self.member.items():
                writer.writerow({"ID": member_id, **data})
# ==================================================
    def save_members(self):
        self.save_members_csv()
        self.save_members_json()
# ==================================================
    def add_member(self, full_name, age, phone, email):
        if not phone.isdigit() or len(phone) != 11 or not phone.startswith("09"):
            print(red("\n شماره تماس معتبر نیست ❌"))
            line()
            return None
        #====================
        if self.member:
            User.member_counter = max(self.member.keys(), default=999) + 1
        member_id = User.member_counter 
        User.member_counter += 1
        member_data = {"Name" : full_name , "Age":age, "PhoneNumber" : phone, "Email":email}
        self.member[member_id] = member_data
        self.save_members()
        print(green(f"\nشما با نام {full_name} و آی دی {member_id} عضو شدید ✅"))
        print(green("خوش آمدید 😉"))
        line()
        #====================
        return member_id
# ==================================================
    def delete_members(self, member_ids):
        for member_id in member_ids:
            if member_id in self.member:
                del self.member[member_id]
                print(green(f"\n عضوی با آی دی {member_id} با موفقیت حذف شد ✅" ))
            # ========================
            else:
                print(red(f"\nعضوی با آی دی {member_id} پیدا نشد ❌"))
        self.save_members()
        line()
# ==========================================================================
class Menu:
    def __init__(self, library, users):
        self.library = library
        self.users = users
        self.users_rule = None # "admin" or "user"
# ==================================================
    def login(self):
        print(green('📚 به کتابخانه دیجیتال "مسیر برتر" خوش آمدید 📚') + line())
        while True:
            print(blue("1. ورود ادمین\n2. ثبت نام کاربر\n3. ورود کاربر\n4. خروج\n"))
            choice = input(magenta("گزینه مورد نظر را وارد کنید : " + l_line()))
            if choice == "1":
                username = input(cyan("نام کاربری : "))
                password = input(cyan("رمز عبور : "))
            # ========================
                if username == "PERSIAN.GHOST" and password == "GHOST6037697578901412":
                    self.users_rule = "admin"
                    print(green("ورود ادمین موفقیت آمیز بود ✅"))
                    break
                # ========================
                else:
                    print(red("نام کاربری یا رمز نامعتبر است ❌"))
                    continue
            # ========================
            if choice == "2":
                print(yellow(" لطفا نام خود را کامل وارد کنید\nحداقل هشت حرف "))
                name = input(cyan(" نام کامل : "))
                if len(name) < 8 :
                    print(red("لطفا اسم را کامل وارد کنید ❗"))
                    line()
                    continue
                # ========================
                age = input(cyan("سن: "))
                if not age.isdigit() or int(age) <= 0:
                    print(red("سن معتبر نیست ❌" ))
                    line()
                    continue
                # ========================
                phone = input(cyan(" شماره تماس : "))
                if not phone.isdigit() or len(phone) != 11 or not phone.startswith("09"):
                    print(red("شماره تماس معتبر نیست ❌"))
                    line()
                    continue
                # ========================
                email = input(cyan("ایمیل: "))
                if '@' not in email or "." not in email:
                    print(red("ایمیل معتبر نیست ❌"))
                    line()
                    continue
                # ========================
                exists = False
                for m in self.users.member.values():
                    if m["PhoneNumber"] == phone:
                        print(red("این شماره قبلا ثبت شده ❗"))
                        exists = True
                        break
                # ========================
                    if m.get("Email") == email:
                        print(red("این ایمیل قبلا ثبت شده ❗"))
                        exists = True
                        break
                # ========================
                if not exists:
                    self.users.add_member(name, age, phone, email)
                    self.users_rule = "user"
                    print(green(f"{name} عزیز, ورود شما به کتابخانه دیجیتال موفقیت آمیز بود ✅\nخوش آمدید"))
                    line()
                    return                
            # ========================
            elif choice == "3":
                print(yellow("ورود کاربر 👤"))
                login_input = input(cyan("شماره تماس یا ایمیل خود را وارد کنید :"))
                # ========================
                found_user = None
                for m_id, m in self.users.member.items():
                    if m["PhoneNumber"] == login_input or m["Email"] == login_input:
                        found_user = m
                        break
                # ========================
                if found_user:
                    print(green(f"✅ ورود موفقیت آمیز بود {found_user['Name']} خوش آمدید"))
                    self.users_rule = "user"
                    line()
                    return
                # ========================
                else:
                    print(red("کاربری با این مشخصات پیدا نشد ❌"))
                    line()
            elif choice == "4":
                print(green("شما از برنامه خارج شدید"))
                print(yellow("خدا نگهدار"))
                exit()
            else:
                print(red("لطفا عدد معتبر وارد کنید ❗"))
# ==================================================
    def main_menu(self):
        while True:
            print(blue("\n--- منوی اصلی ---\n1. بخش کتاب ها\n2. بخش اعضا\n3. خروج"))
            choice = input(magenta("گزینه مورد نظر را وارد کنید: "))
# ========================
            if choice == "1":
                self.book_menu()
            elif choice == "2":
                self.member_menu()
            elif choice == "3":
                print(green("شما از برنامه خارج شدید"))
                print(yellow("خدا نگهدار"))
                exit()
            else:
                print(red("لطفا عدد معتبر وارد کنید ❗"))
# ==================================================
    def book_menu(self):
        while True:
            print(
                    black("\n--- منوی کتاب ها --- \n")
                    + l_line() #--------------------
                    + "1. اضافه کردن کتاب \n"
                    + l_line() #--------------------
                    + "2. مشاهده کتاب \n"
                    + l_line() #--------------------
                    + "3. نمایش همه ی کتاب ها \n"
                    + l_line() #--------------------
                    + "4. جستجو کتاب ها \n"
                    + l_line() #--------------------
                    + "5. حذف کتاب \n"
                    + l_line() #--------------------
                    + "6. بازگشت به منوی اصلی \n"
                    + l_line() #--------------------
                    + Style.RESET_ALL
                    )
            choice = input(magenta("گزینه مورد نظر را وارد کنید : "))
# ==============================================================                    #=============
            if choice == "1":
                if self.users_rule != "admin":
                    print(red("شما دسترسی لازم برای انجام این عملیات را ندارید ❌"))
                    continue
                title = input(cyan("نام کتاب : "))
                author = input(cyan("نام نویسنده : "))
                exists = any(b["Title"] == title and b["Author"] == author for b in self.library.book.values())
                # ========================
                if exists:
                    print(red("کتابی با این نام قبلا اضافه شده است ❗"))
                    line()
                # ========================
                else:
                    book_id = self.library.add_book(title, author)
# ============================================================
            elif choice == "2":
                book_id = int(input(cyan("آی دی کتاب مورد نظر را وارد کنید : ")))
                self.library.show_book(book_id)
# ============================================================
            elif choice == "3":
                self.library.show_books()
# ============================================================
            elif choice == "4":
                b_input = input(cyan("آی دی کتاب های مورد نظر را وارد کنید")+yellow("( با , جدا کنید) : "))
                try:
                    book_ids = [int(x.strip()) for x in b_input.split(",")]
                    for bid in book_ids:
                        self.library.search_books(bid)
                # ========================
                except ValueError:
                    print(red("لطفا یک عدد معتبر وارد کنید و فاصله گذاری را رعایت کنید ! " ))
# ============================================================
            elif choice == "5":
                if self.users_rule != "admin":
                    print(red("شما دسترسی لازم برای انجام این عملیات را ندارید ❌"))
                    continue
                # ========================
                b_input = input(cyan("آی دی کتاب مورد نظر را وارد کنید" ) + yellow("(با , جدا کنید) : "))
                try:
                    book_ids = [int(x.strip()) for x in b_input.split(",")]
                except ValueError:
                    print(red("لطفا عدد وارد کنید و لطفا فاصله گذاری را رعایت کنید" ))
                    continue
                # ========================
                confirm = input(yellow(f"آیا مطمئنید که میخواهید کتاب با آی دی {book_ids} را حذف کنید؟ (y/n): "))
                if confirm.lower() == "y":
                    self.library.delete_books(book_ids)
                else:
                    print(yellow("حذف لغو شد ❌"))
# ==============================================================
            elif choice == "6":
                    print(yellow("بازگشت به منوی اصلی"))
                    return
# ==============================================================
            else:
                print(red( "گزینه نامعتبر است ❌"))
                line()
# ==============================================================
    def member_menu(self):
        if self.users_rule != "admin":
            print(red("شما دسترسی لازم برای انجام این عملیات را ندارید ❌"))
            return
        print(blue("بخش اعضا"))
        while True:    
            print(
                    blue("\n----- منوی اعضا -----\n")
                    +l_line() #--------------------
                    +"1. حذف عضو\n"
                    +l_line() #--------------------
                    +"2. باز گشت به منوی اصلی\n"
                    +l_line() #--------------------
                    )
            choice = input(magenta("گزینه مورد نظر را وارد کنید : "))
# =============================================================
            if choice == "1":
                # ========================
                m_input = input (cyan("آی دی اعضای مورد نظر را وارد کنید : ") + yellow("(با , جدا کنید) : "))
                try:
                    member_ids = [int(y.strip()) for y in m_input.split(",")]
                except ValueError:
                    print(red("لطفا عدد وارد کنید و لطفا فاصله گذاری را رعایت کنید"))
                    continue
                # ========================
                confirm = input(yellow(f"آیا مطمئنید که میخواهید شخصی با آی دی {member_ids} را حذف کنید؟(y/n): "))
                if confirm.lower() == "y":
                    self.users.delete_members(member_ids)
                else:
                    print(yellow("عملیات حذف لغو شد ❌"))
                    line()
# =============================================================
            elif choice == "2":
                    print(yellow("بازگشت به منوی اصلی"))
                    return
# =============================================================        
            else:
                print(red("گزینه نامعتبر است ❌"))
                line()
# ==============================================================
if __name__ == "__main__":
    library = Library()
    users = User()
    menu = Menu(library, users)
    menu.login()
    menu.main_menu()
    print(yellow("برنامه با موفقیت به پایان رسید 🌸"))
