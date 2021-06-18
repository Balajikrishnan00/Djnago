import os,datetime
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

name=input('Enter yourname:')
date=datetime.datetime.now()
hour=date.strftime('%S','%H')
#if hour<12:
#    print('Good morning',name)
#else:
#    print('good AfterNoon',name)
print(hour)
