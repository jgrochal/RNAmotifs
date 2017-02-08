import requests
from io import open
import unittest

# URLs of RNA databases
website_db = 'http://iimcb.genesilico.pl/rnabricks2/fragments/browse_frags/mcannotate/'
website_initial_db_il = 'http://rna.bgsu.edu/img/MotifAtlas/IL1.18/'
website_initial_db_hl = 'http://rna.bgsu.edu/img/MotifAtlas/HL1.18/'


# Checks website status and returns true if requested website exists. Warning: this function may run for a long time!
def does_website_exist(site):
    request = requests.get(site)
    if request.status_code == 200:
        return True
    else:
        return False


# Takes a website address and list of file names as parameters and generates list of urls.
def create_list_of_urls(site, name_list):
    result_list = []
    for name in name_list:
        f = name[1:] + '.png'  # starting from second character, as we know the header name begins with '>'.
        s = site + f
        if does_website_exist(s):
            result_list.append(site + f)
        else:
            result_list.append('404')
    return result_list


# Takes initial CSV file from first database and returns file containing existing websites with possible motifs.
# argument 'website' in this script should be website_initial_db_il if processed internal loops, and
# website_initial_db_hl when working with hairpin loops.
def parse_file(input_file, output_file, id_out_file, website):
    with open(input_file, 'r', encoding='UTF8') as f:
        data = f.read()

    all_data_lines = data.split('\n')
    indexes_of_motif_names = []
    # indexes_content = []  # 0 is an ID, 1 is data
    headers = []
    separated_data_lines = []
    temp_string = ""

    for line in all_data_lines:
        if len(line) > 0 and line[0] == '>':
            if len(temp_string) > 0:
                separated_data_lines.append(temp_string)
            temp_string = ""
            indexes_of_motif_names.append(all_data_lines.index(line))
            # indexes_content.append(0)
            headers.append(line)

        else:
            # indexes_content.append(1)
            temp_string += line
            temp_string += '\n'

    separated_data_lines.append(temp_string)

    # Take list of those 'headers' and generate list of URLs to their 2D structures. This is commented, as it takes
    # quite some time to compute. Please uncomment if you wish to recheck websites and generate a file later.
    # headers_urls = create_list_of_urls(website, headers)

    # Save those URLs to a file.
    # This section is now commented as it takes a lot of time to compute it,
    # if you wish to recreate output files please uncomment.
    """"
    n_headers = len(headers)
    f = open(id_out_file, 'w')
    for i in range(n_headers):
        line = headers[i] + '|' + headers_urls[i] + '\n'
        f.write(line)
    f.close()"""

    motifs_temp_arr = []
    for line in separated_data_lines:
        motifs_temp_arr.append(line.replace('"', '').split('\n'))

    motifs_begin_end = []
    for one_motif in motifs_temp_arr:
        i = motifs_temp_arr.index(one_motif)
        temp = []
        for a in one_motif:
            if len(a) > 0:
                temp.append(headers[i])  # add ID of motif
                temp.append(a.split(',')[0].split('|')[0])  # url of structure
                temp.append(a.split(',')[0].split('|')[-1])  # motif beginning
                temp.append(a.split('.')[-1].split('|')[-1])  # motif end
                if len(temp) == 4:
                    motifs_begin_end.append(temp)
                    temp = []

    # Next part takes a lot of time and is commented, as result files have been generated already.
    # To re-generate those files please uncomment section below.
    """
    sites = []
    for m in motifs_begin_end:
        s = website_db + m[1].lower() + '/'
        if does_website_exist(s):
            sites.append(s + '\t' + m[2] + '\t' + m[3] + '\t' + m[0] + '\n')

    f = open(output_file, 'w')
    for line in sites:
        f.write(line)
    f.close() """


class TestMethods(unittest.TestCase):

    def test_does_website_exist(self):
        self.assertTrue(does_website_exist('http://www.google.pl/'))


def main():
    parse_file('int.csv', 'websites_int.txt', 'int_id_url.txt', website_initial_db_il)
    parse_file('pin.csv', 'websites_pin.txt', 'pin_id_url.txt', website_initial_db_hl)

if __name__ == '__main__':
    # unittest.main()
    main()
