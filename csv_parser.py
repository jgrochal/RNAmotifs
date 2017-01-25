import requests
import urllib.request

with open('int.csv', 'r', encoding='UTF8') as f:
    data = f.read()


all_data_lines = data.split('\n')
indexes_of_motif_names = []
indexes_content = []  # 0 is a header, 1 is data
headers = []
separated_data_lines = []
temp_string = ""

for line in all_data_lines:
    if len(line) > 0 and line[0] == '>':
        if len(temp_string) > 0:
            separated_data_lines.append(temp_string)
        temp_string = ""
        indexes_of_motif_names.append(all_data_lines.index(line))
        indexes_content.append(0)
        headers.append(line)

    else:
        indexes_content.append(1)
        temp_string += line
        temp_string += '\n'

separated_data_lines.append(temp_string)

motifs_temp_arr = []
for line in separated_data_lines:
    motifs_temp_arr.append(line.replace('"', '').split('\n'))

motifs_begin_end = []
for one_motif in motifs_temp_arr:
    i = motifs_temp_arr.index(one_motif)
    temp = []
    for a in one_motif:
        if len(a) > 0:
            temp.append(headers[i])
            temp.append(a.split(',')[0].split('|')[0])
            temp.append(a.split(',')[0].split('|')[-1])
            temp.append(a.split('.')[-1].split('|')[-1])
            if len(temp) == 4:
                motifs_begin_end.append(temp)
                temp = []

sites = []
for m in motifs_begin_end[1:15]:
    i = motifs_begin_end.index(m)
    # print(m[0] + " " + m[1] + ":" + m[2])
    s = 'http://iimcb.genesilico.pl/rnabricks2/fragments/browse_frags/mcannotate/' + m[1].lower() + '/'
    request = requests.get(s)
    if request.status_code == 200:
        sites.append(s + '\t' + m[2] + '\t' + m[3] + '\t' + m[0] + '\n')

f = open('websites.txt', 'w')
for line in sites:
    f.write(line)
f.close()

# images
for name in headers[1:10]:
    f = name[1:] + '.png'
    urllib.request.urlretrieve('http://rna.bgsu.edu/img/MotifAtlas/IL1.18/' + f, 'bgsu_rna/' + f)