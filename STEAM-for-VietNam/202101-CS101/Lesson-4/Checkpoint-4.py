def read_file():
    f = open("applications.csv", "r")
    all_lines = f.readlines()
    all_applicants = []
    for line in all_lines:
        clean_data = line.strip()
        data = clean_data.split(",")
        all_applicants.append(data)
    return all_applicants


def get_first_applicants(applicants):
    first_applicants = {}
    for data in applicants:
        name = data[0]
        city = data[1]
        if (city in first_applicants) is False:
            first_applicants[city] = name
    return first_applicants


def write_result(first_applicants):
    f = open("result.txt", "w")
    for city in first_applicants:
        f.write(city + ',' + first_applicants[city] + '\n')
    f.close()


all_applicants = read_file()
first_applicants = get_first_applicants(all_applicants)
write_result(first_applicants)
print('Da hoan thanh')
