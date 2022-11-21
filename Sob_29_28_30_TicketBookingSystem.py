def TBS():

	if option == 1:
		print("Your ticket status is: Valid")
		exit(0)

	elif option == 2:
		people = int(input("\nEnter no. of Ticket you want : "))
		name_l = []
		age_l = []
		gender_l = []
		for p in range(people):
			name = str(input("\nName : "))
			name_l.append(name)
			age  = int(input("\nAge  : "))
			age_l.append(age)
			gender  = str(input("\nMale or Female : "))
			gender_l.append(gender)

		restart = str(input("\nDid you forgot someone? y/n: "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0
			print("\nTotal Ticket : ",people)
			for p in range(1,people+1):
				print("Ticket : ",p)
				print("Name : ", name_l[x])
				print("Age  : ", age_l[x])
				print("Gender : ",gender_l[x])
				x += 1

print("\n\nTicket Booking System\n")
restart = ('Y')

while restart != ('N','NO','n','no'):
	print("1.Check ticket status")
	print("2.Ticket Reservation")
	option = int(input("\nEnter your option : "))
	TBS()



