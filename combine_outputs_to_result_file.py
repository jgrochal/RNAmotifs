from io import open


def parse_files_into_one(websites, images, headers, output_file_name):
    result = []

    with open(images, 'r', encoding='UTF8') as f:
        data = f.read()
    images_lines = data.split('\n')

    with open(headers, 'r', encoding='UTF8') as f:
        data = f.read()
    header_lines = data.split('\n')

    header_dict = {}

    for line in header_lines:
        if len(line) > 0:
            temp = line.split('|')
            header_dict[temp[0]] = temp[1]

    with open(websites, 'r', encoding='UTF8') as f:
        data = f.read()
    websites_lines = data.split('\n')
    websites_split = []
    for line in websites_lines:
        if len(line) > 0:
            websites_split.append(line.split('\t'))

    # headers_found = []

    n_lines = len(images_lines)
    for i in range(n_lines):
        if len(images_lines[i]) > 0:
            if not images_lines[i] == '0':
                # headers_found.append(websites_split[i][3])
                temp = websites_split[i][3] + ',' + header_dict[websites_split[i][3]] + ',' + \
                       websites_split[i][0][-5:-1].upper() + ',' + images_lines[i] + '\n'
                result.append(temp)

    # print(len(set(headers_found)))

    f = open(output_file_name, 'w')
    for line in result:
        f.write(line)
    f.close()


def main():
    parse_files_into_one('websites_int.txt', 'images_int.txt', 'int_id_url.txt', 'out_int.csv')
    parse_files_into_one('websites_pin.txt', 'images_pin.txt', 'pin_id_url.txt', 'out_pin.csv')


if __name__ == '__main__':
    main()
