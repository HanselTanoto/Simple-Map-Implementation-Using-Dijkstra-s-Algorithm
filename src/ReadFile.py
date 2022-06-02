# read matrix from file
def read_file(file_name, type):
    try :
        open("../test/" + file_name, "r")
    except FileNotFoundError:
        print("File not found")
        return False
    with open("../test/" + file_name) as f:
        read = []
        matrix = []
        nodes_name = []
        # Read Adjacency Matrix
        if (type == "Adjacency Matrix"):
            for line in f:
                row = []
                for i in line.split():
                    row.append(i)
                read.append(row)
            # Checking Adjacency Matrix
            if (not checkAdjacencyMatrix(read)):
                print("Invalid Adjacency Matrix")
                return None
            # Return Adjacency Matrix and Nodes Name
            matrix = [[float(read[i][j]) for j in range(len(read))] for i in range(len(read))]
            nodes_name = [str(i) for i in range(len(read))]
        # Read Edge List
        elif (type == "Edge List"):
            print("aaaa")
            for line in f:
                row = []
                for i in line.split():
                    row.append(i)
                read.append(row)
            # Checking Edge List
            if (not checkEdgeList(read)):
                print("Invalid Edge List")
                return None
            # Return Adjacency Matrix and Nodes Name
            for i in range(len(read)):
                nodes_name.append(read[i][0]) if read[i][0] not in nodes_name else None
                nodes_name.append(read[i][1]) if read[i][1] not in nodes_name else None
            matrix = [[0 for i in range(len(nodes_name))] for j in range(len(nodes_name))]
            for i in range(len(read)):
                matrix[nodes_name.index(read[i][0])][nodes_name.index(read[i][1])] = float(read[i][2])
        print(matrix)
        print(nodes_name)
        return matrix, nodes_name


# Check Adjacency Matrix
def checkAdjacencyMatrix(read):
    if (any (len(row) != len(read[0]) for row in read)):
        print("Error: Adjacency Matrix is not square")
        return False
    for i in range(len(read)):
        for j in range(len(read)):
            try :
                float(read[i][j])
            except ValueError:
                print("Error: Adjacency Matrix is not numeric")
                return False
            if (float(read[i][j]) < 0):
                print("Error: Adjacency Matrix has negative weight")
                return False
    return True


# Check Edge List
def checkEdgeList(read):
    if (any (len(row) != 3 for row in read)):
        print("Error: Edge List is not correct")
        return False
    for i in range(len(read)):
        try :
            float(read[i][2])
        except ValueError:
            print("Error: Edge List is not numeric")
            return False
        if (float(read[i][2]) < 0):
            print("Error: Edge weight is negative")
            return False
    return True