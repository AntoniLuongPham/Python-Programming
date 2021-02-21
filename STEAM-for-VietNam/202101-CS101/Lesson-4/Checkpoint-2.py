def read_file():
    f = open("applicants.csv", "r")
    all_lines = f.readlines()
    all_applicants = []
    for line in all_lines:
        clean_data = line.strip()
        data = clean_data.split(",")
        all_applicants.append(data)
    return all_applicants


print(read_file())
