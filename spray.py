import sys
import datetime
from datetime import timedelta
import os

# Edit this if you want to change the message. The default says "BiN MiCRO$oFT!". :-P
row0 = 	[1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1];
row1 = 	[1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1];
row2 = 	[1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1];
row3 = 	[1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,1];
row4 = 	[1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1];
row5 = 	[1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0];
row6 = 	[1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1];

x = range(52)

row0str = ""
row1str = ""
row2str = ""
row3str = ""
row4str = ""
row5str = ""
row6str = ""

for n in x:
	if row0[n] == 1:
		row0str = row0str + "X"
	else:
		row0str = row0str  + " "

	if row1[n] == 1:
		row1str = row1str + "X"
	else:
		row1str = row1str  + " "

	if row2[n] == 1:
		row2str = row2str + "X"
	else:
		row2str = row2str  + " "

	if row3[n] == 1:
		row3str = row3str + "X"
	else:
		row3str = row3str  + " "

	if row4[n] == 1:
		row4str = row4str + "X"
	else:
		row4str = row4str  + " "

	if row5[n] == 1:
		row5str = row5str + "X"
	else:
		row5str = row5str  + " "

	if row6[n] == 1:
		row6str = row6str + "X"
	else:
		row6str = row6str  + " "

white=u'\u2588'
black=' '

row0str = row0str.replace('X', white).replace(' ', black)
row1str = row1str.replace('X', white).replace(' ', black)
row2str = row2str.replace('X', white).replace(' ', black)
row3str = row3str.replace('X', white).replace(' ', black)
row4str = row4str.replace('X', white).replace(' ', black)
row5str = row5str.replace('X', white).replace(' ', black)
row6str = row6str.replace('X', white).replace(' ', black)

print(row0str)
print(row1str)
print(row2str)
print(row3str)
print(row4str)
print(row5str)
print(row6str)

def last_saturday():
    today = datetime.date.today()

    last_seven_dates_from_yesterday = {}
    mod_count = -1
    for i in range(7):
        tdelta = datetime.timedelta(mod_count)
        mod_count -= 1
        date = today + tdelta
        last_seven_dates_from_yesterday[date.weekday()] = date

    answer=last_seven_dates_from_yesterday[5]
    return answer

def this_row(row_num):
    switch={
    	0: row0,
    	1: row1,
    	2: row2,
    	3: row3,
    	4: row4,
    	5: row5,
    	6: row6
	}
    return switch.get(row_num,'Choose one of the following operator:+,-,*,/,%')

rowpos = 6
colpos = 51

days_per_year = range(364)
for n in days_per_year:

	#print "> rowpos = " + str(rowpos) + ", colpos = " + str(colpos)

	#print this_row(rowpos)[colpos]

	dateting = (last_saturday() - timedelta(days=n)).ctime()
	#print dateting

	create_commit_command = 'GIT_COMMITTER_DATE="' + dateting + ' -0900" git commit --author="Grafiti Actual <teltepilmi@tozya.com>" --allow-empty --date="' + dateting + ' -0900" -m \':P\''
	if this_row(rowpos)[colpos] == 1:
		print create_commit_command
		os.system(create_commit_command)

	rowpos -= 1

	if rowpos == -1:
		rowpos = 6
		colpos -= 1
