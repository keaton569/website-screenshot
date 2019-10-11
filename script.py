import urllib.request
import os
import csv
import time

with open('fullList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Processed {row} lines.')
            line_count += 1
        else:
            try:
                urllib.request.urlretrieve(f'{row[6]}', f'{row[5]}.jpg')
                line_count += 1
                
                #wait 7 secs so we dont overload the server
                #slow sites will produce a thum.io image instead of the website thumbnail
                time.sleep(7)
                
            except urllib.error.HTTPError as e:
                print("error: ", e)
    print(f'Processed {line_count} lines.')
