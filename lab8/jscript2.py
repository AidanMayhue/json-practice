#!/Users/aidanmayhue/anaconda3/bin/python3

import json

#for whatever reason the code from the lab doc isn't working, I'm just going to leave it as is since that is what I was instructed to do
#The rest of the code should work python doesn't have head as far as I know so I just used an accumulator function
with open('schacon.json', 'r') as file:
    data = json.load(file)

csvf = 'chacon.csv'

line_count = 0
max_lines = 5

with open(csvf, 'a') as outfile:
    for item in data:
        if line_count >= max_lines:
            break

        name = item.get('name', '')
        html_url = item.get('html_url', '')
        updated_at = item.get('updated_at', '')
        visibility = item.get('visibility', '')

        line = f'{name},{html_url},{updated_at},{visibility}\n'
        outfile.write(line)
        line_count += 1
