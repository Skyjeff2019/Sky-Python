
weekends = { 'Jan': [6,7,13,14,20,21,27,28],
    'Feb': [3,4,10,11,17,18,24,25],
    'Mar': [3,4,10,11,17,18,24,25,31],
    'Apr': [1,7,8,14,15,21,22,28,29],
    'May': [5,6,12,13,19,20,26,27],
    'Jun': [2,3,9,10,16,17,23,24,30],
    'Jul': [1,7,8,14,15,21,22,28,29],
    'Aug': [4,5,11,12,18,19,25,26],
    'Sep': [1,2,8,9,15,16,22,23,29,30],
    'Oct': [6,7,13,14,20,21,27,28],
    'Nov': [3,4,10,11,17,18,24,25],
    'Dec': [1,2,8,9,15,16,22,23,29,30]}



usermonth= input("what month is your birthday? Please use the abrivation for your month. Example: January-->Jan ")

if usermonth in weekends:
    userday = int(input("what day of the month were you born?"))
    if userday in weekends[usermonth]:
        print("Your birthday is on a weekend")
        print(str(usermonth) + '/' + (str(userday) + '/' + (str(2018))))
    else:
        print("Your birthday is not on a weekend")
        print(str(usermonth) + '/' + (str(userday) + '/' + (str(2018))))



