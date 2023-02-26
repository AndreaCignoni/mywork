# Months Of The Year
# this programs prints out summer months 
# from the complete list of the months
# asnwer to quiz 2 Lab Week5
# Author: Andrea Cignoni

# create a tuple that stores the months of the year
months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "Dember"
)
# from that tuple create another tuple with just the summer months
summer = months [4:7]
# for loop created to print out one month at the time
for month in summer:
    print(month)