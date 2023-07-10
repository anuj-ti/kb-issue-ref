from neo4j import GraphDatabase

# Neo4j connection details
uri = "neo4j://35.172.186.219:7687"
username = "neo4j"
password = "555"
database = "devcustomerdevspacedb"

query_edges = """
MATCH path = (e1:ENTITY)-[:RELATIONSHIP]->(r:RELATIONSHIP)-[:RELATIONSHIP]->(e2:ENTITY)
WITH $idprop AS idprop, e1, r, e2
WHERE (:CHUNK {idprop: idprop})-[:MENTIONS]->(e1)
  AND (:CHUNK {idprop: idprop})-[:MENTIONS]->(e2)
  AND (:CHUNK {idprop: idprop})-[:MENTIONS_RELATIONSHIP]->(r)
RETURN e1, r, e2
"""

query_entities = """
MATCH (e:ENTITY)
WHERE (:CHUNK {idprop: $idprop})-[:MENTIONS]->(e)
RETURN e
"""

query_chunk_id = """
MATCH (c:CHUNK)
RETURN COLLECT(c.idprop) AS chunkIds
"""

# Establish a connection to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Clear the contents of the existing text files
with open("dev_customer_dev_space_db.txt", "w") as file:
    file.write("")


def convert_string(input_string):
    words = input_string.split('_')
    words = words[1:]
    words = words[:-2]
    result = '_'.join(words)
    return result


def get_entities(idprop):
    entities = []
    with driver.session(database=database) as session:
        result = session.run(query_entities, idprop=idprop)
        for record in result:
            e = record['e']
            entities.append(e)
    return entities


def get_edges(idprop):
    edges = []
    with driver.session(database=database) as session:
        result = session.run(query_edges, idprop=idprop)
        for record in result:
            e1 = record['e1']
            r = record['r']
            e2 = record['e2']

            e1 = e1['idprop']
            r = r['idprop']
            r = convert_string(r)
            e2 = e2['idprop']
            edges.append((e1, r, e2))

    return edges


def process_id(idprop):
    entities = get_entities(idprop)
    edges = get_edges(idprop)

    matching_entities = []
    non_matching_entities = []

    for entity in entities:
        mentioned_in_edges = False
        for edge in edges:
            e1, _, e2 = edge
            if entity['idprop'] == e1 or entity['idprop'] == e2:
                mentioned_in_edges = True
                break

        if mentioned_in_edges:
            if entity not in matching_entities:
                matching_entities.append(entity)
        else:
            non_matching_entities.append(entity)

    return matching_entities, non_matching_entities, edges


# def get_idprops():
#     idprops = []
#     with driver.session(database=database) as session:
#         result = session.run(query_chunk_id)
#         for record in result:
#             chunkIds = record['chunkIds']
#             idprops.extend(chunkIds)
#     return idprops

def get_idprops():
    idprops = []
    with open("idprops_array.txt", "r") as idprops_file:
        for line in idprops_file:
            idprop = line.strip()
            idprops.append(idprop)
    return idprops


# Get the array of ID props
idprops_array = get_idprops()

# Process each ID prop and store the results
results = []
for idprop in idprops_array:
    matching_entities, non_matching_entities, extracted_edges = process_id(
        idprop)
    results.append({
        'idprop': idprop,
        'matching_entities': matching_entities,
        'non_matching_entities': non_matching_entities,
        'extracted_edges': extracted_edges
    })

# Store the ID props array in a separate text file
with open("idprops_array.txt", "w") as idprops_file:
    for idprop in idprops_array:
        idprops_file.write(idprop + "\n")

# Store the results in the desired format
with open("dev_customer_dev_space_db.txt", "a") as file:
    for result in results:
        idprop = result['idprop']
        matching_entities = result['matching_entities']
        non_matching_entities = result['non_matching_entities']
        extracted_edges = result['extracted_edges']

        file.write(f"Document ID: {idprop}\n\n")

        file.write("Matching Entities:\n")
        for entity in matching_entities:
            file.write(
                f"ID: {entity['idprop']}, Type: {entity['type']}, Desc: {entity['desc']}\n")
        file.write("\n")

        file.write("Non-Matching Entities:\n")
        for entity in non_matching_entities:
            file.write(
                f"ID: {entity['idprop']}, Type: {entity['type']}, Desc: {entity['desc']}\n")
        file.write("\n")

        file.write("Matching Edges:\n")
        for edge in extracted_edges:
            file.write(
                f"Source: {edge[0]}, Type: {edge[1]}, Target: {edge[2]}\n")
        file.write("\n")

driver.close()
