import csv

parsed = []
count = 0

def return_file_content(file):
    with open (file) as f:
        lines = f.readlines()
    return lines

def return_after_cleaning(lines): 
    file_line = []
    for line in lines:
        file_line.append(line.strip().replace('    ', ',').split(','))
    return file_line
    
lines = return_file_content('raw_data.txt')
cleaned_data = return_after_cleaning(lines)

for items in cleaned_data:
    if len(items)==3:
        parsed.append({'State': items[0]})
        parsed[count]['Postal Abbr.'] = items[1]
        parsed[count]['FIPS Code'] = items[2]
        count+=1
    if len(items)==6:
        for i in range(6):
            if i%3==0:
                parsed.append({'State': items[i]})
                parsed[count]['Postal Abbr.'] = items[i+1]
                parsed[count]['FIPS Code'] = items[i+2]
                count +=1


columns = ['State', 'Postal Abbr.', 'FIPS Code']
with open('result.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = columns)
    writer.writeheader()
    writer.writerows(parsed)



