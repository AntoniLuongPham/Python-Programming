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


print(read_file())
