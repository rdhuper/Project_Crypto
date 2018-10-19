from time import strptime
#from datetime import strftime

date1 = "02-01-2018"
date2 = "02-10-2018"

startdate = strptime(date1, '%m-%d-%y')
print(startdate)
enddate = strptime(date2, '%m-%d-%y')
print(enddate)