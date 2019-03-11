import re
from neo4j import GraphDatabase
from textblob import TextBlob
import mysql.connector
from map import Map
'''
    Algorithm
    1. Strip syntactic markers such as "a" and "the"
    2. Designate tokens to either a relation, attribute, or value
    3. Each database values needs to be attached to its corresponding database attribute

'''

class Parser:
    def __init__(self, grouping):
        self.grouping = grouping

    # Remove all whitespace and punctuation from question
    # Put words into lowercase
    def parse_word(self):
        # matches unicode word characters
        return re.findall("[\w']", self.grouping.lower())


class Tokenizer:
    def __init__(self):
        pass

    # Returns a tagged version of tokens
    def tag(self, tokens):
        sentence = TextBlob(tokens)
        return sentence.tags

class Mapper:
    def __init__(self):
        # connect to Neo4j server
        uri = "bolt://localhost:7687"
        _driver = GraphDatabase.driver(uri, auth=("neo4j", "admin123"))
        # connect to the database session
        self.session = _driver.session()

    def close(self):
        self._driver.close()

    # matches the given to string (token) to a table and/or attribute and/or value
    def match_label(self, token):
        """
        :param token: string
        :return: tuple corresponding to (table match, attribute match, value to corresponding attribute)
        """
        # check if tokens corresponds to a value within Map

        # check if tokens corresponds to either an attribute or synonym
        results = self.session.run("MATCH (n {value: {token}}) RETURN n", {"token": token})
        iterator = results.records()
        # iterate through the results
        while results.peek():
            node = next(iterator)['n']
            # label is an unpacked frozenset (there is only one label on every node - else we could not unpack like this)
            label, = node.labels
            # if it is a synonym, find the corresponding table

            # find the corresponding table the attribute belongs to

        # check if tokens corresponds to a table
        pass

    # find the corresponding attribute to a synonym
    def synonym_to_attribute(self):
        pass

    # find the corresponding table to an attribute
    def attribute_to_table(self):
        pass

class MySQL:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', database='zomato')

    # returns the result of a query run on the MySQL database
    def run_query(self, query):
        csr = self.cnx.cursor()
        csr.execute(query)
        rslt = csr.fetchall()
        return rslt

