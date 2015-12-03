import csv
#import os
import urllib
#import dataconverters.xls
#from operator import itemgetter
# first run the extract
# os.system('. scripts/constituents.sh')
source = "http://cdiac.ornl.gov/ftp/trends/co2/vostok.icecore.co2?force_download=true"
#source = "http://cdiac.ornl.gov/ftp/ndp030/CSV-FILES/nation.1751_2011.csv?force_download=true"
in_path = 'cache/co2-ppm-vostok.csv'
out_path = 'data/co2-ppm-vostok.csv'
def execute():
    urllib.urlretrieve(source, in_path)
    records = []
    with open(in_path) as f:
        for line in f:
            if len(line.split("\t"))==4 :
                records.append(line.split("\t"))
        #reader = csv.reader(f)
        #records = list(reader)

    #header = records[0]
    #header[0], header[1] = header[1], header[0]
    header = ['Age of Ice', 'CO2 Concentration', 'Age of Air', 'Depth']
    #records = records[21:]
    #print records[0]
    #return
    for i in records:
        i[3] = i[3].strip()
        i[0],i[1] = i[1],i[0] #exchange age of ice with depth
        i[1],i[3] = i[3],i[1] #exchange depth with ppm
    #print records[0]
    #sort in descending order of years BP
    records.reverse()
    #records = sorted(records, key=float(itemgetter(0)))
    #header = ['Date', 'Price (Dollars per million btu)']
    # data begins on row 4
    #records = records[3:]

    #header = [ [ fixsymbol(x[1]) ] for x in header ]

    writer = csv.writer(open(out_path, 'w'), lineterminator='\n')
    writer.writerow(header)
    writer.writerows(records)

execute()
