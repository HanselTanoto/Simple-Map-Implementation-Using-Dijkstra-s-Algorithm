# read matrix from file
def read_file(file_name):
    """
    Reads a file and returns a matrix of the contents
    """
    try :
        open("../test/" + file_name, "r")
    except FileNotFoundError:
        return None
    with open("../test/" + file_name) as f:
        matrix = []
        for line in f:
            row = []
            for i in line.split():
                row.append(float(i))
            matrix.append(row)
        return matrix

