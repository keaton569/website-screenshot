import urllib.request
import os
import csv
import time

##USES THIS URL SCHEME INSIDE THE CSV FILE ---- IN THIS CASE COLUMN 4
##https://image.thum.io/get/width/300/noanimate/wait/3/[YOUR_URL]


##HEADERS IN CSV CHANGE WITH EACH GEO CAUSE IM LAZY
#################################################################

with open('US.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Processed {row} lines.')
            line_count += 1
        else:
            try:
                urllib.request.urlretrieve(f'{row[4]}', f'{row[0]}.jpg')
                line_count += 1
            except urllib.error.HTTPError as e:
                print(f'{row[0]}: '"error: ", e)
    print(f'Processed {line_count} lines.')

