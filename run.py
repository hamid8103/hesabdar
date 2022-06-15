from calendar import Calendar
import time
import tkinter as tk
from tkinter.constants import E, FALSE, W
from tkinter import  HORIZONTAL, StringVar, Tk, ttk, messagebox
import database as db
import datetime as dt
from tkcalendar import *


# other functions

list_of_widjets = []


def remake_window(width, height, *objects):
    root.geometry(f"{width}x{height}")
    for object in objects:
        try:
            object.destroy()
        except:
            pass


def not_entered():
    messagebox.showwarning("Warning", ".ابتدا وارد شوید")


def add_widjet_to_list(lst):
    for widjet in lst:
        list_of_widjets.append(widjet)
# other functions


# Enter part

root = tk.Tk()
root.configure(background="#FFFF8B")
root.option_add('*tearOff', FALSE)
root.geometry("300x300")
root.title("حسابدار")
enter_allow = False

user = None

# register


def register():
    if (ent_username.get() == "") or (ent_password.get() == ""):
        messagebox.showwarning(
            "Empty", ".نام کاربری یا رمز عبور نمی تواند خالی باشد")
    else:
        username = ent_username.get()
        password = ent_password.get()
        information = db.select_user_inf(username)
        if (" " not in username) and (" " not in password):
            if information != None:
                if information[0] != username and information[1] != password:
                    db.user_reports_table(username)
                    db.sql_insert_user("users_informations", [
                        username, password])
                    messagebox.showinfo(
                        "register info", ".ثبت نام شما با موفقیت انجام شد. از قسمت ورود وارد شوید")
                else:
                    messagebox.showinfo(
                        "User Exist", ".شما قبلاً ثبت نام کردید. از قسمت ورود وارد شوید")
            else:
                db.user_reports_table(username)
                db.sql_insert_user("users_informations", [username, password])
                messagebox.showinfo(
                    "register info", ".ثبت نام شما با موفقیت انجام شد. از قسمت ورود وارد شوید")
        else:
            messagebox.showwarning(
                "Empty", ".نام کاربری یا رمز عبور نمی تواند فضای خالی داشته باشد")

# register

# main window
def main():
    sum_income=db.sum_EorI(user,"I")
    lbl_sum_income=tk.Label(master=root,text=":مجموع درآمد")
    lbl_sum_income.grid(column=1,row=0,pady=10,sticky=E)
    lbl_sum_income_show=tk.Label(master=root,text=sum_income)
    lbl_sum_income_show.grid(column=0,row=0,padx=30,pady=10)
    sum_expenses=db.sum_EorI(user,"E")
    lbl_sum_expenses=tk.Label(master=root,text=":مجموع مخارج")
    lbl_sum_expenses.grid(column=1,row=1,pady=10,sticky=E)
    lbl_sum_expenses_show=tk.Label(master=root,text=sum_expenses)
    lbl_sum_expenses_show.grid(column=0,row=1,padx=30,pady=10)
    list_of_widjets_main=[lbl_sum_income_show,lbl_sum_expenses,lbl_sum_expenses_show,lbl_sum_income]
    add_widjet_to_list(list_of_widjets_main)
# main window

# enter


def enter():
    if (ent_username.get() == "") or (ent_password.get() == ""):
        messagebox.showwarning(
            "Empty", ".نام کاربری یا رمز عبور نمی تواند خالی باشد")
    elif (" " in ent_username.get()) or (" " in ent_password.get()):
        messagebox.showwarning(
            "Empty", ".نام کاربری یا رمز عبور نمی تواند فضای خالی داشته باشد")
    else:
        username = ent_username.get()
        password = ent_password.get()
        information = db.select_user_inf(username)
        if information != None:
            if information[0] == username and information[1] != password:
                messagebox.showwarning(
                    "Wrong Password", ".رمز عبور اشتباه وارد شده است")
            elif information[0] == username and information[1] == password:
                try:
                    db.user_reports_table("users_informations", username)
                except:
                    pass
                global user
                user = username
                messagebox.showinfo("Welcome", ".ورود موفقیت آمیز بود")
                remake_window(500, 700, lbl_username, lbl_password,
                              ent_password, ent_username, btn_enter, btn_register)
                main()
               

            else:
                messagebox.showinfo("undefinde user", "نام کاربری یافت نشد")
        else:
            messagebox.showinfo("undefinde user", "نام کاربری یافت نشد")
# enter


lbl_username = tk.Label(master=root, text=":نام کاربری")
lbl_username.grid(column=1, row=0, sticky=E, pady=30)
ent_username = tk.Entry(master=root)
ent_username.grid(column=0, row=0, padx=30)
lbl_password = tk.Label(master=root, text=":رمزعبور")
lbl_password.grid(column=1, row=1, sticky=E)
ent_password = tk.Entry(master=root)
ent_password.grid(column=0, row=1, padx=30)
btn_register = tk.Button(master=root, text="ثبت نام", command=register)
btn_register.grid(column=0, row=2, padx=30, pady=10, sticky=W)
btn_enter = tk.Button(master=root, text="ورود", command=enter)
btn_enter.grid(column=0, row=2, padx=30, sticky=E)

# Enter part


# Top Menu

# change_color_option

def change_color():
    def submit():
        try:
            root["background"] = combo_colors.get()
        except:
            messagebox.showerror("error", "رنگ وارد شده صحیح نیست")

    color_list = ["red", "yellow", "blue", "black",
                  "white", "purple", "green", "cyan"]

    if user != None:
        remake_window(500, 700, *list_of_widjets)
        combo_colors = ttk.Combobox(master=root, values=color_list)
        combo_colors.grid(column=0, row=0, padx=30, pady=25)
        lbl_color = tk.Label(master=root, text=":رنگ مورد نظر را انتخاب کنید")
        lbl_color.grid(column=1, row=0, sticky=E)
        btn_color = tk.Button(master=root, text="تایید", command=submit)
        btn_color.grid(column=0, row=1, sticky=E, padx=30)
        list_of_widjets_changecolor = [combo_colors, lbl_color, btn_color]
        add_widjet_to_list(list_of_widjets_changecolor)

    else:
        not_entered()

# change_color_option


# add option

def add_option():

    def date_picker(lbl):
        date_picker = Tk()
        today = dt.datetime.now()
        cal = Calendar(master=date_picker, selectmode='day',
                       year=today.year, month=today.month,
                       day=today.day)
        cal.grid(column=0, row=0, padx=20, pady=10)

        def return_date():
            lbl["text"] = cal.get_date()
            date_picker.destroy()
        btn = tk.Button(master=date_picker, text="ok", command=return_date)
        btn.grid(column=0, row=1, pady=10)
        date_picker.mainloop()

    def add_income_report():
        # EorI, grouptype,price, date , description
        EorI = "I"
        grouptype = combo_income.get()
        price = ent_price_income.get()
        if price.isdigit() == False:
            return messagebox.showwarning("error", "قیمت باید به عدد وارد شود")
        date = lbl_show_date_income["text"]
        discription = discriptions_textbox_income.get("1.0", "end-1c")
        list_entities = [EorI, grouptype, price, date, discription]
        x = 0
        for i in range(len(list_entities)-1):
            if x != 0:
                break
            if list_entities[i] == "":
                x += 1
        if x == 0:
            db.sql_insert_reports(user, list_entities)
            messagebox.showinfo("successful", "با موفقیت ثبت شد")
            combo_income.set("")
            ent_price_income.delete(0, "end")
            lbl_show_date_income.config(text="")
            discriptions_textbox_income.delete("1.0", "end-1c")
        else:
            messagebox.showwarning("emtpy", "تمامی فیلدها را پر کنید")

    def add_expenses_report():
        # EorI, grouptype,price, date , description
        EorI = "E"
        grouptype = combo_expenses.get()
        price = ent_price_expenses.get()
        if price.isdigit() == False:
            return messagebox.showwarning("error", "قیمت باید به عدد وارد شود")
        date = lbl_show_date_expenses["text"]
        discription = discriptions_textbox_expenses.get("1.0", "end-1c")
        list_entities = [EorI, grouptype, price, date, discription]
        x = 0
        for i in range(len(list_entities)-1):
            if x != 0:
                break
            if list_entities[i] == "":
                x += 1
        if x == 0:
            db.sql_insert_reports(user, list_entities)
            messagebox.showinfo("successful", "با موفقیت ثبت شد")
            combo_expenses.set("")
            ent_price_expenses.delete(0, "end")
            lbl_show_date_expenses.config(text="")
            discriptions_textbox_expenses.delete("1.0", "end-1c")
        else:
            messagebox.showwarning("emtpy", "تمامی فیلدها را پر کنید")

    if user != None:
        remake_window(500, 700, *list_of_widjets)
        list_of_income = ["حقوق", "سود سرمایه گذاری", "دریافت وام یا قرض", "دریافت طلب",
                          "فروش دارایی", "رهن یا اجاره", "دریافت خسارت یا دیه", "هدیه", "جایزه یا قرعه کشی"]
        list_of_expenses = ["خوراک", "رفت و آمد و هزینه خودرو", "پوشاک", "پرداخت قبض یا شارژ", "سلامت و درمان", "خرید دارایی", "سرمایه گذاری",
                            "پرداخت قسط", "پرداخت بدهی", "بهداشت و آرایش", "آموزش و تحضیلات", "مسکن", "هدیه", "سفر", "قرض", "خسارت و دیه", "خیریه یا وجوه اسلامی", "خانواده"]

        # income
        lbl_add_income = tk.Label(master=root, text="اضافه کردن دریافتی ها",
                                  font="BNazanin 16 bold", fg="green")
        lbl_add_income.grid(column=1, row=0, pady=10, columnspan=1, sticky=E)
        lbl_price_income = tk.Label(
            master=root, text=":مبلغ", font="BNazanin 12 bold")
        lbl_price_income.grid(column=1, row=1, pady=10, sticky=E)
        ent_price_income = tk.Entry(master=root)
        ent_price_income.grid(column=0, row=1)
        lbl_add_income2 = tk.Label(
            master=root, text=":دسته بندی", font="BNazanin 12 bold")
        lbl_add_income2.grid(column=1, row=2, pady=10, sticky=E)
        combo_income = ttk.Combobox(master=root, values=list_of_income)
        combo_income.grid(column=0, row=2, padx=40, sticky=E)
        lbl_date_income = tk.Label(
            master=root, text=":تاریخ", font="BNazanin 12 bold")
        lbl_date_income.grid(column=1, row=3, pady=10, sticky=E)
        btn_calpick_income = tk.Button(
            master=root, text="انتخاب تاریخ", font="BMitra 10 bold", bg="#FF9900", activebackground="#C07200", width=10, command=lambda: date_picker(lbl_show_date_income))
        btn_calpick_income.grid(column=0, row=3, padx=25, sticky=W)
        lbl_show_date_income = tk.Label(master=root, font="BNazanin 12 bold")
        lbl_show_date_income.grid(column=0, row=3, padx=25, sticky=E)
        lbl_discribtion_income = tk.Label(
            master=root, text=":توضیحات", font="BNazanin 12 bold")
        lbl_discribtion_income.grid(column=1, row=4, sticky=E)
        discriptions_textbox_income = tk.Text(master=root, width=20, height=2)
        discriptions_textbox_income.grid(column=0, row=4, pady=10)
        btn_add_income = tk.Button(
            master=root, text="ثبت", width=10, font="BMitra 14 bold", bd=3, bg="#66FF33", activebackground="#2AB000", command=add_income_report)
        btn_add_income.grid(column=0, row=5, pady=20)
        # income

        # expenses
        lbl_add_expenses = tk.Label(master=root, text="اضافه کردن مخارج",
                                    font="BNazanin 16 bold", fg="red")
        lbl_add_expenses.grid(column=1, row=6,  columnspan=1, sticky=E)
        lbl_price_expenses = tk.Label(
            master=root, text=":مبلغ", font="BNazanin 12 bold")
        lbl_price_expenses.grid(column=1, row=7, pady=10, sticky=E)
        ent_price_expenses = tk.Entry(master=root)
        ent_price_expenses.grid(column=0, row=7)
        lbl_add_expenses2 = tk.Label(
            master=root, text=":دسته بندی", font="BNazanin 12 bold")
        lbl_add_expenses2.grid(column=1, row=8, pady=10, sticky=E)
        combo_expenses = ttk.Combobox(master=root, values=list_of_expenses)
        combo_expenses.grid(column=0, row=8, padx=40, sticky=E)
        lbl_date_expenses = tk.Label(
            master=root, text=":تاریخ", font="BNazanin 12 bold")
        lbl_date_expenses.grid(column=1, row=9, pady=10, sticky=E)
        btn_calpick_expenses = tk.Button(
            master=root, text="انتخاب تاریخ", font="BMitra 10 bold", bg="#FF9900", activebackground="#C07200", width=10, command=lambda: date_picker(lbl_show_date_expenses))
        btn_calpick_expenses.grid(column=0, row=9, padx=25, sticky=W)
        lbl_show_date_expenses = tk.Label(master=root, font="BNazanin 12 bold")
        lbl_show_date_expenses.grid(column=0, row=9, padx=25, sticky=E)
        lbl_discribtion_expenses = tk.Label(
            master=root, text=":توضیحات", font="BNazanin 12 bold")
        lbl_discribtion_expenses.grid(column=1, row=10, sticky=E)
        discriptions_textbox_expenses = tk.Text(
            master=root, width=20, height=2)
        discriptions_textbox_expenses.grid(column=0, row=10, pady=10)
        btn_add_expenses = tk.Button(
            master=root, text="ثبت", width=10, font="BMitra 14 bold", bd=3, bg="#FF3333", activebackground="#D20000", command=add_expenses_report)
        btn_add_expenses.grid(column=0, row=11, pady=20)
        # expenses

        list_of_widjets_add = [lbl_add_expenses, lbl_price_expenses, ent_price_expenses, lbl_add_expenses2, combo_expenses, lbl_date_expenses,
                               lbl_add_income, lbl_price_income, ent_price_income, lbl_add_income2, combo_income, lbl_date_income, btn_calpick_income, lbl_show_date_income, lbl_discribtion_income, discriptions_textbox_income, btn_add_income,
                               btn_calpick_expenses, lbl_show_date_expenses, lbl_discribtion_expenses, discriptions_textbox_expenses, btn_add_expenses]
        add_widjet_to_list(list_of_widjets_add)

    else:
        not_entered()

# add option

# user settings


def user_settings():
    def change_pass():
        if ent_US_old_pass.get() != "" and ent_US_new_pass.get() != "" and ent_US_repeat_new_pass.get() != "":
            if " " not in (ent_US_old_pass.get() and ent_US_new_pass.get()):
                information = db.select_user_inf(user)
                if ent_US_old_pass.get() == information[1]:
                    if ent_US_repeat_new_pass.get() == ent_US_new_pass.get():
                        db.sql_update("users_informations", user,
                                      ent_US_new_pass.get())
                        messagebox.showinfo(
                            "successful", "رمزعبور با موفقیت تغییر یافت")
                        for widjet in [ent_US_new_pass, ent_US_repeat_new_pass, ent_US_old_pass]:
                            widjet.delete(0, "end")
                    else:
                        messagebox.showinfo(
                            "error", "رمز عبور جدید با تکرار آن یکسان نیست")
                else:
                    messagebox.showinfo("error", "رمز فعلی اشتباه است")
            else:
                messagebox.showinfo(
                    "error", "فیلدها نمی توانند دارای فضای خالی باشند")
        else:
            messagebox.showinfo("error", "فیلدها نمی توانند خالی باشند")

    if user != None:
        remake_window(500, 700, *list_of_widjets)
        lbl_US = tk.Label(master=root, text="تغییر رمزعبور",
                          font="BNazanin 16 bold")
        lbl_US.grid(column=1, row=0, pady=10, sticky=E)
        lbl_US_username = tk.Label(master=root, text=f"{user} کاربر")
        lbl_US_username.grid(column=1, row=1, pady=10, sticky=E)
        lbl_US_old_pass = tk.Label(master=root, text="رمزعبور فعلی")
        lbl_US_old_pass.grid(column=1, row=2, pady=10, sticky=E)
        ent_US_old_pass = tk.Entry(master=root, width=20)
        ent_US_old_pass.grid(column=0, row=2, padx=30)
        lbl_US_new_pass = tk.Label(master=root, text="رمزعبور جدید")
        lbl_US_new_pass.grid(column=1, row=3, pady=10, sticky=E)
        ent_US_new_pass = tk.Entry(master=root, width=20)
        ent_US_new_pass.grid(column=0, row=3)
        lbl_US_repeat_new_pass = tk.Label(
            master=root, text="تکرار رمزعبور جدید")
        lbl_US_repeat_new_pass.grid(column=1, row=4, pady=10, sticky=E)
        ent_US_repeat_new_pass = tk.Entry(master=root, width=20)
        ent_US_repeat_new_pass.grid(column=0, row=4)
        btn_submit = tk.Button(
            master=root, text="تایید", width=10, font="BMitra 14 bold", command=change_pass)
        btn_submit.grid(column=0, row=5, pady=10)
        list_of_widjets_US = [lbl_US, lbl_US_username,
                              lbl_US_new_pass, lbl_US_repeat_new_pass, lbl_US_old_pass, ent_US_new_pass, ent_US_old_pass, ent_US_repeat_new_pass, btn_submit]
        add_widjet_to_list(list_of_widjets_US)
    else:
        not_entered()

# user settings

# search


def search():
    def date_picker(lbl):
        date_picker = Tk()
        today = dt.datetime.now()
        cal = Calendar(master=date_picker, selectmode='day',
                       year=today.year, month=today.month,
                       day=today.day)
        cal.grid(column=0, row=0, padx=20, pady=10)

        def return_date():
            lbl["text"] = cal.get_date()
            date_picker.destroy()
        btn = tk.Button(master=date_picker, text="ok", command=return_date)
        btn.grid(column=0, row=1, pady=10)
        date_picker.mainloop()

    def loading():
        pb = ttk.Progressbar(root, orient=HORIZONTAL,
                             length=100, mode='determinate')
        pb.grid(pady=10)
        pb.start()
        for i in range(20):
            root.update_idletasks()
            pb['value'] += 5
            time.sleep(0.05)
        pb.destroy()

    def date_search():
        report_result_base_EorI = []
        report_result_base_date = []
        report_result_base_price = []
        report_result_base_group = []
        loading()

        # EorI search

        if var.get() == "I":
            report_result_base_EorI.append(db.select_report(user, "EorI", "I"))
        else:
            report_result_base_EorI.append(db.select_report(user, "EorI", "E"))

        # EorI search

        # dete search

        if lbl_show_date_start["text"]!="" and lbl_show_date_end["text"]!="":
            if " " not in(lbl_show_date_start["text"] and lbl_show_date_end["text"]):
                stdate = list(map(int, lbl_show_date_start["text"].split("/")))
                date_start = dt.date(stdate[2], stdate[0], stdate[1])
                eddate = list(map(int, lbl_show_date_end["text"].split("/")))
                date_end = dt.date(eddate[2], eddate[0], eddate[1])
                delta = dt.timedelta(days=1)
                while date_start <= date_end:
                    day = date_start.day
                    month = date_start.month
                    year = date_start.year
                    date = f"{month}/{day}/{year}"
                    for data in report_result_base_EorI:
                        for i in data:
                            if date in i:
                                report_result_base_date.append(i)
                    date_start += delta
            else:
                messagebox.showinfo(
                    "error", "فیلدها نمی توانند دارای فضای خالی باشند")
        else:
            messagebox.showinfo("error", "فیلدها نمی توانند خالی باشند")


        # dete search

        # price search
        if ent_price_start.get()!="" and ent_price_end.get()!="":
            if " " not in(ent_price_start.get() and ent_price_end.get()):
                if ent_price_start.get().isdigit() == False or ent_price_end.get().isdigit() == False:
                    return messagebox.showwarning("error", "قیمت باید به عدد وارد شود")
                else:
                    start_price = int(ent_price_start.get())
                    end_price = int(ent_price_end.get())
                    while start_price <= end_price:
                        for data in report_result_base_EorI:
                            for i in data:
                                if start_price in i:
                                    report_result_base_price.append(i)
                        start_price += 1
            else:
                messagebox.showinfo(
                    "error", "فیلدها نمی توانند دارای فضای خالی باشند")
        else:
            messagebox.showinfo("error", "فیلدها نمی توانند خالی باشند")

        # price search

        # group search
        if lbl_show_group["text"]!="" :
            if " " not in lbl_show_group["text"]:
                wanted_group = lbl_show_group["text"]
                if wanted_group != "همه":
                    for data in report_result_base_EorI:
                        for i in data:
                            if wanted_group in i:
                                report_result_base_group.append(i)
                else:
                    report_result_base_group = report_result_base_date
                
                report_final_list = []
                t = 1
                for x in report_result_base_date:
                    for y in report_result_base_price:
                        for z in report_result_base_group:
                            if x == y == z:
                                report_final_list.append(x)
                                t += 1
                window=Tk()
                window.title("نتیجه جست و جو")
                window.geometry("700x700")
                tk.Label(
                    master=window, text="توضیحات  /  تاریخ  /  مبلغ  /  دسته بندی").grid(column=0, row=0,padx=10,pady=10)
                j = 1
                for report in report_final_list:
                    i = 0
                    for item in report:
                        if item != "E" and item != "I":
                            tk.Label(master=window, text=item).grid(
                                column=i, row=j, pady=10, padx=10)
                            i += 1
                    j += 1
                window.mainloop()
                
            else:
                messagebox.showinfo(
                    "error", "فیلدها نمی توانند دارای فضای خالی باشند")
        else:
            messagebox.showinfo("error", "فیلدها نمی توانند خالی باشند")

        # group search

        

    def show_combo():
        window = Tk()
        window.geometry("200x200")
        window.title("حسابدار")
        list_of_income = ["همه", "حقوق", "سود سرمایه گذاری", "دریافت وام یا قرض", "دریافت طلب",
                          "فروش دارایی", "رهن یا اجاره", "دریافت خسارت یا دیه", "هدیه", "جایزه یا قرعه کشی"]
        list_of_expenses = ["همه", "خوراک", "رفت و آمد و هزینه خودرو", "پوشاک", "پرداخت قبض یا شارژ", "سلامت و درمان", "خرید دارایی", "سرمایه گذاری",
                            "پرداخت قسط", "پرداخت بدهی", "بهداشت و آرایش", "آموزش و تحضیلات", "مسکن", "هدیه", "سفر", "قرض", "خسارت و دیه", "خیریه یا وجوه اسلامی", "خانواده"]
        if var.get() == "I":
            combo_income = ttk.Combobox(master=window, values=list_of_income)
            combo_income.grid(pady=10, padx=30)
        else:
            combo_expenses = ttk.Combobox(
                master=window, values=list_of_expenses)
            combo_expenses.grid(pady=10, padx=30)

        def return_combo_selected():
            if var.get() == "I":
                lbl_show_group["text"] = combo_income.get()
            else:
                lbl_show_group["text"] = combo_expenses.get()
            window.destroy()
        tk.Button(master=window, text="ok", width=10,
                  command=return_combo_selected).grid(pady=10, padx=30)
        window.mainloop()

    if user != None:
        remake_window(500, 700, *list_of_widjets)
        lbl_search = tk.Label(master=root, text="جستوجو",
                              font="BNazanin 16 bold")
        lbl_search.grid(column=1, row=0, pady=10, sticky=E)
        lbl_search_EorI = tk.Label(
            master=root, text=":جستوجو بین", font="BNazanin 13")
        lbl_search_EorI.grid(column=1, row=1, pady=10, rowspan=2, sticky=E)
        var = StringVar()
        rbtn_search1 = tk.Radiobutton(
            root, text="دریافتی ها", font="BMitra 14 bold", bd=3, bg="#66FF33", selectcolor="#2AB000", activebackground="#2AB000", width=15, value="I", variable=var, indicatoron=0)
        rbtn_search1.grid(column=0, row=1, padx=30, pady=5, sticky=W)
        rbtn_search1.select()
        rbtn_search2 = tk.Radiobutton(
            root, text="مخارج", width=15, font="BMitra 14 bold", bd=3, bg="#FF3333", selectcolor="#D20000", activebackground="#D20000", value="E", variable=var, indicatoron=0)
        rbtn_search2.grid(column=0, row=2, padx=30, pady=5, sticky=W)
        lbl_date_start = tk.Label(master=root, text="از تاریخ")
        lbl_date_start.grid(column=1, row=3, pady=10, sticky=E)
        btn_datepick_search = tk.Button(
            master=root, text="انتخاب تاریخ", font="BMitra 10 bold", bg="#FF9900", activebackground="#C07200", width=8, command=lambda: date_picker(lbl_show_date_start))
        btn_datepick_search.grid(column=0, row=3, padx=30, sticky=W)
        lbl_show_date_start = tk.Label(master=root, font="BNazanin 12 bold")
        lbl_show_date_start.grid(column=0, row=3, padx=30, sticky=E)
        lbl_date_end = tk.Label(master=root, text="تا تاریخ")
        lbl_date_end.grid(column=1, row=4, pady=10, sticky=E)
        btn_datepick_search2 = tk.Button(
            master=root, text="انتخاب تاریخ", font="BMitra 10 bold", bg="#FF9900", activebackground="#C07200", width=8, command=lambda: date_picker(lbl_show_date_end))
        btn_datepick_search2.grid(column=0, row=4, padx=30, sticky=W)
        lbl_show_date_end = tk.Label(master=root, font="BNazanin 12 bold")
        lbl_show_date_end.grid(column=0, row=4, padx=30, sticky=E)
        lbl_price_start = tk.Label(master=root, text="از مبلغ")
        lbl_price_start.grid(column=1, row=5, pady=10, sticky=E)
        ent_price_start = tk.Entry(master=root, width=20)
        ent_price_start.grid(column=0, row=5)
        lbl_price_end = tk.Label(master=root, text="تا مبلغ")
        lbl_price_end.grid(column=1, row=6, pady=10, sticky=E)
        ent_price_end = tk.Entry(master=root, width=20)
        ent_price_end.grid(column=0, row=6)
        lbl_group = tk.Label(master=root, text="دسته بندی")
        lbl_group.grid(column=1, row=7, pady=10, sticky=E)
        btn_group = tk.Button(master=root, text="انتخاب", command=show_combo)
        btn_group.grid(column=0, row=7, padx=30, sticky=W)
        lbl_show_group = tk.Label(master=root)
        lbl_show_group.grid(column=0, row=7, padx=30, sticky=E)
        btn_search = tk.Button(master=root, text="جستوجو", width=10, font="BMitra 10 bold",
                               bg="#FF9900", activebackground="#C07200", command=date_search)
        btn_search.grid(column=0, pady=10)

        list_of_widjets_search = [btn_datepick_search2,btn_group, lbl_search, lbl_search_EorI, rbtn_search1, rbtn_search2, lbl_date_start, btn_datepick_search, lbl_show_date_start, lbl_date_end,
                                  btn_datepick_search, lbl_show_date_end, lbl_price_start, ent_price_start, lbl_price_end, ent_price_end, lbl_group, lbl_show_group, btn_search]

        add_widjet_to_list(list_of_widjets_search)
    else:
        not_entered()


# search

menubar = tk.Menu(master=root)
root["menu"] = menubar
menue_reports = tk.Menu(master=menubar)
menue_seting = tk.Menu(master=menubar)
menubar.add_cascade(menu=menue_reports, label="گزارشات")
menubar.add_cascade(menu=menue_seting, label="تنظیمات")
menue_reports.add_command(label="اضافه کردن گزارش", command=add_option)
menue_reports.add_command(label="جستوجوی گزارشات", command=search)
menue_seting.add_command(label="تنظیمات کاربری", command=user_settings)
menue_seting.add_command(label="تنظیمات برنامه", command=change_color)

# Top Menu




root.mainloop()
