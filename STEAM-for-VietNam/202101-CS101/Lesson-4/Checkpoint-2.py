def read_file():
    f = open("applications.csv", "r")
    all_lines = f.readlines()
    all_applications = []
    for line in all_lines:
        clean_data = line.strip()
        data = clean_data.split(",")
        all_applications.append(data)
    return all_applications


print(read_file())
