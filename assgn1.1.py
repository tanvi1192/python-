name = raw_input("Enter your name.")
name1 = name.title()
dob_date = raw_input("Enter the date from your date of birth.")
dob_month = raw_input("Enter the month from your date of birth.")
dob_month1 = dob_month.title()
dob_year = raw_input("Enter the year from your date of birth.")
import time
current_year = int(time.strftime("%Y"))

birth_year = int(dob_year)
gender = raw_input("Enter your gender.")
height = raw_input("Enter your height in cm.")
weight = raw_input("Enter your weight in kg.")

print "Your name is %s. Your date of birth is %s %s %s . Your age is %s." % (name1, dob_date, dob_month1, dob_year, current_year - birth_year)
print "You are a %s of weight %s kg and height %s cm." % (gender, weight, height)