import calendar
try:
  yil = int(input("Yilni kiriting: "))
  print(calendar.calendar(yil))
except:
  print("Noto'g'ri yil kiritilgan")
