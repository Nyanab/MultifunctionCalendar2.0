#kode diketik oleh nabila⭐

#beberapa library
import calendar
from datetime import datetime as dt
from function import tanya_hari, tanya_bulan, tanya_tahun, tanya_btahun

#nanya pilihan
print("=================\n= Multifunction =\n=  Calendar🗓️    =\n=================")
print()
print("""type [1] to check this month calendar
type [2] to check month in custom year calendar
type [3] to check all month in this year calendar
type [4] to check all month in custom year calendar
type [5] to check day name on custom date
type [6] to check birthday countdown""")
tanya = input(">>")

print()

if tanya=="1":
  satiya = dt.now() 
  balon = int(satiya.strftime("%m")) 
  year = int(satiya.strftime("%y")) 
  print(calendar.month(year,balon))

elif tanya=="2":
  balon=0
  year=0
  balon=tanya_bulan(balon,"month you want to check:")
  year=tanya_tahun(year,"year you want to check:")
  print(f"\n{calendar.month(year,balon)}")

elif tanya=="3":
  #dari library calendar import * biar ke unlock fungsi calendar()
  from calendar import *
  satiya = dt.now() 
  year = int(satiya.strftime("20"+"%y")) 
  print(f"\n{calendar(year)}")

elif tanya=="4":
  #dari library calendar import * biar ke unlock fungsi calendar()
  from calendar import *
  #nanya thn
  year=0
  year=tanya_tahun(year,"year you want to check:")
  print(f"\n{calendar(year)}")

elif tanya=="5":
  #dictionary hari dari sudut pandang library 'calendar'
  days_dict = {
  0:"monday",
  1:"tuesday",
  2:"wednesday",
  3:"thursday",
  4:"friday",
  5:"saturday",
  6:"sunday"}
  #nanya poe, bulan, dan taon
  poe=0
  month=0
  year=0
  poe=tanya_hari(poe,"day you want to check:")
  month=tanya_bulan(month,"month you want to check:")
  year=tanya_tahun(year,"year you want to check:")
  name = calendar.weekday(year,month,poe)
  print(f"\nits {days_dict[name]}!")

elif tanya=="6":
  satiya = dt.now() 
  nowday = int(satiya.strftime("%d")) 
  nowmonth = int(satiya.strftime("%m"))
  nowyear = int(satiya.strftime("%y")) 
  #bulan di array ganjil berjumlah 31 hari, genap 30 hari
  #di array gada februari soalnya harinya 29/28, tapi di cek kok di loop
  odd = [1,3,5,7,8,10,12,13,15,17,19,20,22,24]
  even = [4,6,9,11,16,18,21,23]
  leapmonth = [2,12] #array gk berguna btw
  days = 0 #var jumlah hari
  dayss = 0 #var sisa hari bulan ini
  age = 0 #var umur
  #ketika seseorang berulang tahun di tahun depan, akan ada kemungkinan tahun depan adalah tahun kabisat
  nextyear = nowyear + 1
  nextmonth = nowmonth + 1
  leap = nowyear%4==0
  nextleap = nextyear%4==0
  #nanya tanggal, bulan, dan tahun ultah
  bday=0
  bmonth=0
  byear=0
  bday=tanya_hari(bday,"your birthday date:")
  bmonth=tanya_bulan(bmonth,"your birthday month:")
  byear=tanya_btahun(byear,"your birthday year (optional→Enter):")
  if byear!="":
    byear=int(byear)
  #month countdown
  month = bmonth - nowmonth
  #menghitung sisa hari bulan ini
  if nowday==bday and nowmonth==bmonth or nowmonth==bmonth:
    pass
  elif nowmonth in odd:
    dayss = 31-nowday
  elif nowmonth in even:
    dayss = 30-nowday
  elif leap==False and nowmonth==2:
    dayss = 28-nowday
  elif leap==True and nowmonth==2:
    dayss = 29-nowday
  days+=dayss
  if month<0:
    #ulang tahun tahun depan
    if byear!="":
      age = 2000+nextyear-byear
    x=0 #var hari bulan sekarang ke bulan di ujung tahun
    y=0 #var hari awal bulan ke bulan ultah
    for i in range(nextmonth,13):
      if leap==True and i==2:
        x+=29
      elif i==2:
        x+=28
      elif i in odd:
        x+=31
      elif i in even:
        x+=30
      i+=1
    for i in range(1,bmonth):
      if nextleap==True and i==2:
        y+=29
      elif i==2:
        y+=28
      elif i in odd:
        y+=31
      elif i in even:
        y+=30
      i+=1
    days+=x+y+bday
    print(f"\nyour birthday is {days} days left")
    if days<365 and days>354:    
      print("ah, your birthday is a few days ago?\nhappy belated birthday!🎉")
  elif month==0:
    #ulang tahun bulan ini di tahun yang sama atau ulang tahun bulan ini di tahun depan
    if bday<nowday:
      #menambah hari satu tahun(365/366) jika tanggal ulang tahun<tanggal hari ini (ulang tahun udh lewat)
      if byear!="":
        age = 2000+nextyear-byear
      x=nowday-bday
      if nextleap==True:
        days+=366-x
      else:
        days+=365-x
      print("\nyour birthday is",days,"days left")
      if days<365 and days>354:
        print("ah, your birthday is a few days ago?\nhappy belated birthday!🎉")
    else:
      if byear!="":
        age = 2000+nowyear-byear
      x=bday-nowday
      days+=x
      print("\nyour birthday is",days,"days left")
      if days<=14 and days>=2:
        print("it's almost your birthday,\nhappy erlier birthday for you!🎉")
      elif days==1:
        print("tomorrow is your birthday!\nhappy erlier birthday for you!🎉")        
      elif days==0:
        print("today is your birthday!\nhappy birthday!🎉")
  elif month>1:
    #ulang tahun tahun ini
    if byear!="":
      age = 2000+nowyear-byear
    for i in range(nextmonth,bmonth):
      if leap==True and i==2:
        days+=29
      elif i==2:
        days+=28
      elif i in odd:
        days+=31
      elif i in even:
        days+=30
    days+=bday
    print(f"\nyour birthday is {days} days left")
    if days<=14 and days >=2:
      print("it's almost your birthday,\nhappy erlier birthday for you!🎉")
    elif days==1:
      print("tomorrow is your birthday!\nhappy erlier birthday for you!🎉")        
  #kenapa ulang tahun bulan depan gak bareng [elif month>1:]? kan tinggal dijadiin [elif month>=1:]. Soalnya ada kemungkinan sekarang tanggal 31 dan ulang tahunnya tanggal 1 bulan depan.
  elif month==1:
    #ulang tahun bulan depan
    if byear!="":
      age = 2000+nowyear-byear
    days+=bday
    print(f"\nyour birthday is {days} days left")
    if days<=14 and days >=2:
      print("it's almost your birthday,\nhappy erlier birthday for you!🎉")
    elif days==1:
      print("tomorrow is your birthday!\nhappy erlier birthday for you!🎉")
  if bday==29 and bmonth==2:
    print("wow such a rare day you will celebrate your birthday,\nhappy erlier birthday for you!🎉")
  if byear!="":
    print(f"you will be {age} years old on your next birthday!")

else:
  #ketika ada kesalahan pengetikan dll
  print("something wrong, check your\nnumber and try again")

print("\n=================\n\na program by Nabila")
#code by nabila⭐