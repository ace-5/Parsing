import csv

parsed = []

def get_data_lines(file):
    with open (file) as f:
        lines = f.readlines()
    
    return lines[5:]


def remove_whitespace(lines):
    line = []
    for aLine in lines:
        line.append(aLine.strip())

    return line

def make_each_word_listItem(lines):
    line = []
    for i in range(len(lines)):
        line.append(lines[i].split())
    return line

file_lines = get_data_lines('raw_data.txt')
no_following_whitespace = remove_whitespace(file_lines)
lines_to_parse = make_each_word_listItem(no_following_whitespace)

count = 0
for items in lines_to_parse:
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



