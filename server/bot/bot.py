import re
from neo4j import GraphDatabase
from textblob import TextBlob
import mysql.connector
from bot.map import Map
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
        self._driver = GraphDatabase.driver(uri, auth=("neo4j", "admin123"))
        # connect to the database session
        self.session = self._driver.session()

    def close(self):
        self._driver.close()

    # matches the given to token to a table and/or attribute and/or value
    def match_label(self, token):
        all_matches = []
        """
        :param token: string
        :return: tuple corresponding to (table match, attribute match, value to corresponding attribute)
        """
        # check if tokens corresponds to a value within Map
        matching_attribute = Map.mapping_table.get(token)
        # if the token has a matching attribute within map, find the corresponding table
        if matching_attribute:
            # match the corresponding table to the attribute
            result = self.session.run("MATCH (t:Table)-[:HAS_ATTRIBUTE]->(:Attribute {value:{attribute}}) RETURN t", {"attribute": matching_attribute, "token": token})
            # use results.peek() because we only want the first result
            if result.peek() and result.peek().get('t'):
                # extract the table name from the result
                matching_table = list(result.peek().get('t').values())[0]
                all_matches.append((matching_table, matching_attribute, token))

        # check if token corresponds to either a table, attribute, or synonym
        results = self.session.run("MATCH (n {value: {token}}) RETURN n", {"token": token})
        iterator = results.records()
        # iterate through the results
        while results.peek():
            node = next(iterator).get('n')
            # label unpacks a frozenset (there is only one label on every node - else we could not unpack like this)
            label, = node.labels
            # if it is a synonym, find the corresponding table
            if label == "Synonym":
                synonym = list(node.values())[0]
                # find the corresponding table(s) and attribute
                result = self.session.run("MATCH (:Synonym {value:{synonym}})-[:IS_LIKE]->(a:Attribute)<-[:HAS_ATTRIBUTE]-(t:Table) RETURN a,t",{"synonym": synonym})
                if result.peek() and result.peek().get('a') and result.peek().get('t'):
                    table_iterator = result.records()
                    while result.peek():
                        curr_node = next(table_iterator)
                        matching_attribute = list(curr_node.get('a').values())[0]
                        matching_table = list(curr_node.get('t').values())[0]
                        all_matches.append((matching_table, matching_attribute, False))
            elif label == "Attribute":
                attribute = list(node.values())[0]
                # find the corresponding table(s) the attribute belongs to
                result = self.session.run("MATCH (t:Table)-[:HAS_ATTRIBUTE]->(:Attribute {value:{attribute}}) RETURN t",{"attribute": attribute})
                # use results.peek() because we only want the first result
                if result.peek() and result.peek().get('t'):
                    table_iterator = result.records()
                    while result.peek():
                        curr_node = next(table_iterator)
                        # extract the table name from the result
                        matching_table = list(curr_node.get('t').values())[0]
                        all_matches.append((matching_table, attribute, False))
            elif label == "Table":
                table = list(node.values())[0]
                all_matches.append((table, False, False))
        return all_matches


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

# Main Function - Controls the flow
class Get_Response:
    def __init__(self, sentence):

