import requests

website_db = 'http://iimcb.genesilico.pl/rnabricks2/fragments/browse_frags/mcannotate/'
website_initial_db = 'http://rna.bgsu.edu/img/MotifAtlas/IL1.18/'


def create_list_of_urls(site, name_list):
    result_list = []
    for name in name_list:
        f = name[1:] + '.png'
        s = site + f
        if does_website_exist(s):
            result_list.append(site + f)
        else:
            result_list.append('404')
    return result_list


def parse_file(input_file, output_file):
    with open(input_file, 'r', encoding='UTF8') as f:
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

    # headers_urls = create_list_of_urls(website_initial_db, headers)
    # print(headers_urls)

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
    for m in motifs_begin_end:
        # i = motifs_begin_end.index(m)
        # print(m[0] + " " + m[1] + ":" + m[2])
        s = website_db + m[1].lower() + '/'
        if does_website_exist(s):
            sites.append(s + '\t' + m[2] + '\t' + m[3] + '\t' + m[0] + '\n')

    f = open(output_file, 'w')
    for line in sites:
        f.write(line)
    f.close()


def does_website_exist(site):
    request = requests.get(site)
    if request.status_code == 200:
        return True
    else:
        return False


def main():
    parse_file('int.csv', 'websites_int.txt')
    parse_file('pin.csv', 'websites_pin.txt')

if __name__ == '__main__':
    main()
