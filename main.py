import csv

with open ('raw_data.txt') as f:
    lines = f.readlines()

lines1 = []
lines2=[]
parsed = []

for line in lines[5:]:
    lines1.append(line.strip())

for i in range(len(lines1)):
    lines2.append(lines1[i].split())

count = 0
for items in lines2:
    for i in range(len(items)):
        if len(items[i]) > 2:
            if not (len(items[i+1])>2 or len(items[i+2])>2):
                parsed.append(dict())
                parsed[count]['State'] = items[i]
                parsed[count]['Postal Abbr.'] = items[i+1]
                parsed[count]['FIPS Code'] = items[i+2]
                count +=1
            else:
                parsed.append(dict())
                if len(items[i+2])>2:
                    parsed[count]['State'] = items[i]+' '+items[i+1]+' '+items[i+2]
                    parsed[count]['Postal Abbr.'] = items[i+3]
                    parsed[count]['FIPS Code'] = items[i+4]
                    count +=1
                else:
                    parsed[count]['State'] = items[i]+' '+items[i+1]
                    parsed[count]['Postal Abbr.'] = items[i+2]
                    parsed[count]['FIPS Code'] = items[i+3]
                    count+=1


columns = ['State', 'Postal Abbr.', 'FIPS Code']
with open('result.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = columns)
    writer.writeheader()
    writer.writerows(parsed)



