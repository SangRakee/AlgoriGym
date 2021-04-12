month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
week=['SUN','MON','TUE','WED','THU', 'FRI', 'SAT']

x,y=map(int,input().split())

day=0
for i in range(x):
    day+=month[i]
day+=y
print(week[day%7])
