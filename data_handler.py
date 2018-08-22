FILE_PATH = "request_counts.txt"

def get_numbers_from_file():
    dict_of_request_counts = {}
    with open(FILE_PATH, "r") as txtfile:
        for line in txtfile:
            splitted_line = line.split(": ")
            dict_of_request_counts[splitted_line[0]] = int(splitted_line[1])
    return dict_of_request_counts


def write_numbers_to_file(dict_of_counts):
    with open(FILE_PATH, "w") as txtfile:
        for key in dict_of_counts:
            txtfile.write(f"{key}: {dict_of_counts[key]}\n")
