'''
Created on 1 Jul 2020

@author: Hoodlumdan
'''

from datetime import datetime

print(datetime.now().strftime('Todays date is the %d of %B %Y'))

birthday = '15 01 1992'
name = 'Daniel'

def birthday_info(date):
    try:
        parsed = datetime.strptime(date, '%d %m %Y')
    except ValueError:
        return('Date not formatted correctly. Format is "DD MM YYYY".') 
    else:
        year = datetime.now().year
        
        return name + ' was born on a ' + parsed.strftime('%A') + ' and is currently ' + str(year - parsed.year) + ' years old. It is ' + str((parsed.replace(year = year + 1) - datetime.now()).days) + ' days until their next birthday.'
    
print(birthday_info(birthday))