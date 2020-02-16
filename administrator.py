#5.8

uzytkownicy = ["Deziom", "Admin", "Alien", "Moris", "Chemik"]

for uzytkownik in uzytkownicy:
	if uzytkownik == 'Admin':
		print("\tWitaj, " + uzytkownik + "! Czy chcesz przejrzec dzisiejszy raport?")
	else:
		print("Witaj, " + uzytkownik + "! Dziękujemy, że ponownie się zalogowałeś")

#5.9

uzytkownicy = []

if uzytkownicy:
	for uzytkownik in uzytkownicy:
		if uzytkownik == 'Admin':
			print("\tWitaj, " + uzytkownik + "! Czy chcesz przejrzec dzisiejszy raport?")
		else:
			print("Witaj, " + uzytkownik + "! Dziękujemy, że ponownie się zalogowałeś")
else:
	print("Lista jest pusta!")

#5.10

current_users = ["Deziom", "Admin", "Alien", "Moris", "Chemik"]
new_users = ["DEZIOM", "Incb", "Luj", "Filia", "Xivan"]

for user in new_users:
	if user.title() in current_users:
		print(user + ", ta nazwa jest już zajęta!")
	else:
		print(user + ", ta nazwa jest wolna!")

#.5.11

liczby_porzadkowe = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for liczba in liczby_porzadkowe:
	if liczba == 1:
		print(str(liczba) + "st")
	elif liczba ==2:
		print(str(liczba) + "nd")
	elif liczba ==3:
		print(str(liczba) + "rd")
	else:
		print(str(liczba) + "th")
