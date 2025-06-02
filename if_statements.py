"""
mark = 65
if mark >= 80:
    print("Grade A")
elif mark >= 70:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 50:
    print("Grade D")
else:
    print("Retake")


#Nested if

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
    has_ticket = input("Do you have a valid ticket? (yes/no): ")
    if has_ticket == "yes":
        print("You can watch the movie.")
    else:
        print("You cannot watch the movie without a valid ticket.")
else:
    print("You are not allowed to watch the movie because you are under 18.")
"""

#MATCH STATEMENT

day = 8
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Looking forward to the Weekend")
        
        
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
    
month = 3
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")