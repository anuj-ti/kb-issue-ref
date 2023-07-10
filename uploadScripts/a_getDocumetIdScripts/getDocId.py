from neo4j import GraphDatabase

# Neo4j connection details
uri = "neo4j://35.172.186.219:7687"
username = "neo4j"
password = "ccc"
database = "devcustomerdevspacedb"

# Query to retrieve DOCUMENT.idprop values
query_document_idprops = """
MATCH (d:DOCUMENT)
RETURN d.idprop AS documentIdprops
"""

# Establish a connection to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Retrieve the DOCUMENT.idprop values
document_idprops = []
with driver.session(database=database) as session:
    result = session.run(query_document_idprops)
    for record in result:
        document_idprops.append(record['documentIdprops'])

# Store the DOCUMENT.idprop values in a text file
file_path = 'uploadScripts\\a_getDocumetIdScripts\\document_idprops.txt'
with open(file_path, "w") as file:
    file.write("")  # Clear the contents of the file
    for idprop in document_idprops:
        file.write(idprop + "\n")

# Print the number of document IDs retrieved
num_document_ids = len(document_idprops)
print(f"Retrieved {num_document_ids} document IDs.")

# Close the Neo4j driver
driver.close()
