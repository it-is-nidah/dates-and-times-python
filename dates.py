#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today is ",today)


  # print out the date's individual components
  print("Date's components; ",today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag", "Sonntag"]
  print("Today's weekday # is",today.weekday(), "which is",days[today.weekday()])


  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  heute = datetime.now()
  print("current date and time is", heute)
  
  # Get the current time
  t = datetime.time(datetime.now())
  print(" current time is", t)
 

  
if __name__ == "__main__":
  main();
  