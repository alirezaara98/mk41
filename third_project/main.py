'''from datetime import date, timedelta

def calender_func(date1, date2, day):
    day +=1
    if day == 7:
        day = 0
    start_date = date.fromisoformat(date1)
    end_date = date.fromisoformat(date2)
    different = end_date - start_date

    date_list = [start_date + timedelta(days=x) for x in range(different.days+1)]

    for our_date in date_list :
        if our_date.strftime('%w') == str(day):
             yield (our_date.strftime('%d%B%Y'))

rslt = calender_func('2020-02-18','2020-05-02',3)

for data in rslt:
    print(data)'''




def hanoi(start,temp,finish,n):
    if n == 1:
        print("{} --> {}".format(start,finish))
        return
    hanoi(start,finish,temp,n-1)
    print("{} --> {}".format(start,finish))
    hanoi(temp,start,finish,n-1)
# test 1
#hanoi('A','B','C',4)
# test 2
#hanoi('A','B','C',3)
# test 3
#hanoi('A','B','C',2)
# test 4
#hanoi('A','B','C',1)