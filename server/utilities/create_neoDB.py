"""
    This file is used to create the Neo4j database
"""

from neo4j import GraphDatabase
import csv

# connect to Neo4j server
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "admin123"))
# connect to the database session
session = driver.session()

# method to insert tables into database
def insert_tables():
    # add the three tables to the graph
    session.run("MERGE (:Table {value: 'restaurants'})")
    session.run("MERGE (:Table {value: 'cuisines'})")
    session.run("MERGE (:Table {value: 'code'})")

# Method to insert the attributes into database
def insert_attributes():
    # open the three csv files containing the database attributes and
    # add the first row (attributes) of each csv file to the graph
    with open('zomato.csv', mode='r') as zomato:
        reader = csv.reader(zomato)
        # only look at the first row
        attributes = next(reader)
        for attribute in attributes:
            # the attribute names in the MySQL database are lowercase with underscores between words
            attribute = attribute.lower().replace(" ", "_")
            # Add the attribute and then create :HAS_ATTRIBUTE relationship with table 'restaurants'
            session.run("MERGE (:Attribute {value: {att}})", {"att": attribute})
            session.run("MATCH (attribute:Attribute {value: {att}}), (table:Table {value: 'restaurants'}) MERGE (table)-[:HAS_ATTRIBUTE]->(attribute)", {"att": attribute})

    with open('zomato_cuisines.csv', mode='r') as zomato_cuisine:
        reader = csv.reader(zomato_cuisine)
        attributes = next(reader)
        for attribute in attributes:
            attribute = attribute.lower().replace(" ", "_")
            session.run("MERGE (:Attribute {value: {att}})", {"att": attribute})
            session.run("MATCH (attribute:Attribute {value: {att}}), (table:Table {value: 'cuisines'}) MERGE (table)-[:HAS_ATTRIBUTE]->(attribute)", {"att": attribute})

    with  open('country_code.csv', mode='r') as country_code:
        reader = csv.reader(country_code)
        attributes = next(reader)
        for attribute in attributes:
            attribute = attribute.lower().replace(" ", "_")
            session.run("MERGE (:Attribute {value: {att}})", {"att": attribute})
            session.run("MATCH (attribute:Attribute {value: {att}}), (table:Table {value: 'code'}) MERGE (table)-[:HAS_ATTRIBUTE]->(attribute)", {"att": attribute})


def insert_synonyms():
    with open('synonyms.csv', mode='r') as synonyms:
        reader = csv.reader(synonyms)
        for row in reader:
            attribute_name = row[0].lower().replace(" ", "_")
            for similar_word in row:
                similar_word = similar_word.lower()
                if similar_word.replace(" ", "_") != attribute_name and similar_word != "":
                    # Add the synonym and then create :IS_LIKE relationship with corresponding attribute
                    session.run("MERGE (:Synonym {value: {syn}})", {"syn": similar_word})
                    session.run("MATCH (attribute:Attribute {value: {att}}), (synonym:Synonym {value: {syn}}) MERGE (synonym)-[:IS_LIKE]->(attribute)",{"att": attribute_name, "syn": similar_word})

insert_tables()
insert_attributes()
insert_synonyms()


