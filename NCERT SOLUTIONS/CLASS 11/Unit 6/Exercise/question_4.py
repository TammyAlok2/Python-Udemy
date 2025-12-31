# 4. Write a program to check if the year entered by the 
# user is a leap year or not

year = int(input("Enter the year"))

def check_leap_year(year):
    if year % 4 == 0 & year % 100 ==0:
        print(f"The given year {year} is leap year")
        
    elif year % 400 == 0:
        print(f"The given year {year} is leap year")
        
check_leap_year(year)
            

