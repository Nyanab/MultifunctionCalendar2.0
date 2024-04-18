#function nanya hari
def tanya_hari(hari,kalimat):
  hari = int(input(kalimat))
  while hari>31:
    hari = int(input("day is greater than 31\nplease enter again:"))
  return hari

#function nanya bulan
def tanya_bulan(bulan,kalimat):
  bulan = int(input(kalimat))
  while bulan>12:
    bulan = int(input("month is greater than 12\nplease enter again:"))
  return bulan

#function nanya tahun
def tanya_tahun(tahun,kalimat):
  tahun = int(input(kalimat))
  while tahun>9999:
    tahun = int(input("year is greater than 9999\nplease enter again:"))
  return tahun

#function nanya tahun ultah
#istimewa karna bisa diskip pertanyaannya :D
def tanya_btahun(btahun,kalimat):
  btahun = input(kalimat)
  while btahun!="" and int(btahun)>9999:
    btahun = input("year is greater than 9999\nplease enter again:")
  return btahun