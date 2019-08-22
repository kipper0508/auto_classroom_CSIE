#coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
import Tkinter
mainWin = Tkinter.Tk()
mainWin.title("資工借教室")
mainWin.geometry("800x600")

nameVariable = Tkinter.Label(mainWin, text="借用人名稱：")
nameVariable.place(x = 230, y = 30)
nameentry = Tkinter.Entry(mainWin, text="in_name")
nameentry.place(x = 230, y = 55)

phoneVariable = Tkinter.Label(mainWin, text="電話：")
phoneVariable.place(x = 230, y = 85)
phoneentry = Tkinter.Entry(mainWin, text="in_phone")
phoneentry.place(x = 230, y = 110)

classroomVariable = Tkinter.Label(mainWin, text="教室：")
classroomVariable.place(x = 230, y = 140)
classroomentry = Tkinter.Entry(mainWin, text="in_classroom")
classroomentry.place(x = 230, y = 165)

yearVariable = Tkinter.Label(mainWin, text="年：")
yearVariable.place(x = 230, y = 195)
yearentry = Tkinter.Entry(mainWin, text="in_year")
yearentry.place(x = 230, y = 220)

monthVariable = Tkinter.Label(mainWin, text="月：")
monthVariable.place(x = 380, y = 195)
monthentry = Tkinter.Entry(mainWin, text="in_month")
monthentry.place(x = 380, y = 220)

dateinVariable = Tkinter.Label(mainWin, text="日（開始）：")
dateinVariable.place(x = 230, y = 250)
dateinentry = Tkinter.Entry(mainWin, text="in_date_start")
dateinentry.place(x = 230, y = 275)

dateoutVariable = Tkinter.Label(mainWin, text="日（結束）：")
dateoutVariable.place(x = 380, y = 250)
dateoutentry = Tkinter.Entry(mainWin, text="in_date_end")
dateoutentry.place(x = 380, y = 275)

timeinVariable = Tkinter.Label(mainWin, text="開始時間（xx:00）：")
timeinVariable.place(x = 230, y = 305)
timeinentry = Tkinter.Entry(mainWin, text="in_time_start")
timeinentry.place(x = 230, y = 330)

timeoutVariable = Tkinter.Label(mainWin, text="結束時間（xx:00）：")
timeoutVariable.place(x = 380, y =305)
timeoutentry = Tkinter.Entry(mainWin, text="in_time_end")
timeoutentry.place(x = 380, y = 330)

idVariable = Tkinter.Label(mainWin, text="學號：")
idVariable.place(x = 230, y = 360)
identry = Tkinter.Entry(mainWin, text="id")
identry.place(x = 230, y = 385)

passwordVariable = Tkinter.Label(mainWin, text="密碼：")
passwordVariable.place(x = 380, y = 360)
passwordentry = Tkinter.Entry(mainWin, text="password")
passwordentry.place(x = 380, y = 385)

def click():
    name = nameentry.get();
    phone = phoneentry.get();
    classroom = classroomentry.get();
    year = yearentry.get();
    month = monthentry.get();
    datein = dateinentry.get();
    date_in = int(datein);
    dateout = dateoutentry.get();
    date_out = int(dateout);
    timein = timeinentry.get();
    timeout = timeoutentry.get();
    id = identry.get();
    password = passwordentry.get();

    driver = webdriver.Firefox()
    driver.get("https://classroom.csie.ncu.edu.tw/")
    driver.maximize_window()

    ID = driver.find_element_by_id("edit-name");
    ID.send_keys(id);


    passwordin = driver.find_element_by_id("edit-pass");
    passwordin.send_keys(password);

    button = driver.find_element_by_id("edit-submit");
    button.click();
    room = {
                "A203" : "6",
                "A204" : "7",
                "A205" : "8",
                "A206" : "9",
                "A207" : "11",
                "A208" : "12",
                "A209" : "13",
                "A210" : "14",
                "A211" : "15",
                "A212" : "16",
                "A301" : "17",
                "A302" : "18",
                "A303" : "25",
                "A306" : "26",
                "B217" : "27",
                "B223" : "23",
                "B226" : "21",
                "B323" : "24",
                "B326" : "22"
        };
    timestart = {
                "08:00" : "0",
                "09:00" : "1",
                "10:00" : "2",
                "11:00" : "3",
                "12:00" : "4",
                "13:00" : "5",
                "14:00" : "6",
                "15:00" : "7",
                "16:00" : "8",
                "17:00" : "9",
                "18:00" : "10",
                "19:00" : "11",
                "20:00" : "12",
                "21:00" : "13"
        };
    timeend = {
                "09:00" : "0",
                "10:00" : "1",
                "11:00" : "2",
                "12:00" : "3",
                "13:00" : "4",
                "14:00" : "5",
                "15:00" : "6",
                "16:00" : "7",
                "17:00" : "8",
                "18:00" : "9",
                "19:00" : "10",
                "20:00" : "11",
                "21:00" : "12",
                "22:00" : "13"
        };

    for i in range(date_in,date_out+1):
        driver.get("https://classroom.csie.ncu.edu.tw/appointment_form")
        namein = driver.find_element_by_id("edit-name");
        namein.send_keys(name);
        
        phonein = driver.find_element_by_id("edit-phone");
        phonein.send_keys(phone);

        classroomin = Select(driver.find_element_by_id("edit-classroom"));
        classroomin.select_by_value(room[classroom]);

        monthin = Select(driver.find_element_by_id("edit-date-month"));
        monthin.select_by_value(month);
        dayin = Select(driver.find_element_by_id("edit-date-day"));
        date = str(i);
        dayin.select_by_value(date);
        yearin = Select(driver.find_element_by_id("edit-date-year"));
        yearin.select_by_value(year);

        start = Select(driver.find_element_by_id("edit-start-period"));
        start.select_by_value(timestart[timein]);

        end = Select(driver.find_element_by_id("edit-end-period"));
        end.select_by_value(timeend[timeout]);

        button = driver.find_element_by_id("edit-submit");
        button.click();

buttonVariable = Tkinter.Button(mainWin,text="確認",command = click)
buttonVariable.place(x = 350, y = 450)

mainWin.mainloop()


