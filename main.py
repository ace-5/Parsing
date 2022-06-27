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

def parser(items):
    return({
        'State': items[0],
        'Postal Abbr.': items[1],
        'FIPS Code': items[2]
    })

lines = return_file_content('raw_data.txt')
cleaned_data = return_after_cleaning(lines)


for items in cleaned_data:
    if len(items)==3:
        parsed.append(parser(items))
    if len(items)==6:
        parsed.append(parser(items[:3]))
        parsed.append(parser(items[3:]))


columns = ['State', 'Postal Abbr.', 'FIPS Code']
with open('result.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = columns)
    writer.writeheader()
    writer.writerows(parsed[1:])



