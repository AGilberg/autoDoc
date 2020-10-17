#!/usr/bin/python3
from datetime import date, timedelta
from tkinter import *
from tkinter import messagebox, StringVar, Entry
import shutil
import os

# program is compiled to single executable file, so this gets the right runtime-path
path = os.path.dirname(sys.executable)

weekday = {
        'mandag': 1,
        'tirsdag': 2,
        'onsdag': 3,
        'torsdag': 4,
        'fredag': 5,
        'lørdag': 6,
        'søndag': 7
        }

dirs = { 
        '01': '01 Januar',
        '02': '02 Februar',
        '03': '03 Mars',
        '04': '04 April',
        '05': '05 Mai',
        '06': '06 Juni',
        '07': '07 Juli',
        '08': '08 August',
        '09': '09 September',
        '10': '10 Oktober',
        '11': '11 November',
        '12': '12 Desember'
        }

selectedDays = []

def getAllDays(year, day):
    d = date(year, 1, 1)
    d += timedelta(days = 6 - d.weekday()+day)
    while d.year == year:
        yield d
        d += timedelta(days = 7)

def btnHandle():
    for key in dirs:
        os.mkdir(path+'/'+dirs[key])
    cnt = 0
    try:
        for day in selectedDays[-1]:
            for date in getAllDays(int(year.get()), weekday[day]):
                cnt += 1
                shutil.copy2(
                        path + '/Mal.docx', 
                        path + '/' + dirs[str(date)[5:7]] + '/'  + day + ' ' + str(date) + '.docx'
                        )
    except:
        messagebox.showinfo('NB!', 'Noe gikk galt')
        return
    
    messagebox.showinfo('Suksess!', str(cnt) + ' skjemaer er opprettet')
    window.destroy()

def handleSelect(e):
    selectedDays.append([listBox.get(idx) for idx in listBox.curselection()])

window = Tk()
info1 = Text(window, height=1, width=22)
info1.insert(INSERT, 'Skriv inn kalenderår: ')
year = StringVar()
chooseYear = Entry(window, textvariable=year, width=4)
info2 = Text(window, height=1, width=14)
info2.insert(INSERT, 'Velg ukedager:')

info1.pack()
info1.config(state=DISABLED)
chooseYear.pack()
info2.pack()
info2.config(state=DISABLED)
listBox = Listbox(window, selectmode = "multiple")

for key, val in weekday.items():
    listBox.insert(val, key)

listBox.pack()
btn = Button(window, text='Opprett skjemaer', bd='5', command = btnHandle)
btn.pack(side = 'bottom')
listBox.bind('<<ListboxSelect>>', handleSelect)
window.mainloop()
