def read_file():
    f = open('applications.csv', 'r')
    all_lines = f.readlines()
    all_appliccations = []
    for line in all_lines:
        clean_data = line.strip()
        data = clean_data.split(',')
        all_appliccations.append(data)

    f.close()
    return all_appliccations


def get_first_applicants(applicants):
    first_applicants = {}
    for data in applicants:
        name = data[0]
        city = data[1]
        if (city in first_applicants) is False:
            first_applicants[city] = name
    return first_applicants


all_applicants = read_file()
first_applicants = get_first_applicants(all_applicants)
print(first_applicants)
