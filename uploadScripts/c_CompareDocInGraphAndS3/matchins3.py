def read_names_from_file(file_path):
    names = []
    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip()
            names.append(name)
    return names


document_idprops_path = 'uploadScripts\c_CompareDocInGraphAndS3\document_idprops.txt'
document_name_path = 'uploadScripts\c_CompareDocInGraphAndS3\document_names.txt'

document_idprops = read_names_from_file(document_idprops_path)
document_name = read_names_from_file(document_name_path)


def find_intersection(document_idprops, document_name):
    intersection = []

    for name in document_name:
        name_without_ext = name.replace(".json", "")
        if name_without_ext in document_idprops:
            intersection.append(name)

    return intersection


# Find the intersection
intersection = find_intersection(document_idprops, document_name)

# Print the array size and the array itself
print("Array Size:", len(intersection))
print("Intersection Array:", intersection)

# Write the array to a text file
filename = "uploadScripts\c_CompareDocInGraphAndS3\intersection.txt"
with open(filename, "w") as file:
    for item in intersection:
        file.write(item + "\n")

print("Array written to", filename)
