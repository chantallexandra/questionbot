import re
from neo4j import GraphDatabase
from textblob import TextBlob, Word
import mysql.connector
from bot.map import Map
from bot.sql_templates import Templates
'''
    Algorithm
    1. Strip syntactic markers such as "a" and "the"
    2. Designate tokens to either a relation, attribute, or value
    3. Each database values needs to be attached to its corresponding database attribute

'''


class Tokenizer:
    def __init__(self):
        pass

    # Returns a tagged version of the tokens
    @classmethod
    def tag(cls, tokens):
        sentence = TextBlob(tokens)
        return sentence.tags

    # Returns a tagged version of the lemmatized tokens
    @classmethod
    def lemmatize(cls, tokens):
        sentence = TextBlob(tokens)
        words = sentence.words
        lemmatized = ""
        for word in words:
            lemmatized += Word(word).lemmatize() + " "
        return lemmatized[:-1]


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
                result = self.session.run("MATCH (:Synonym {value:{synonym}})-[:IS_LIKE]->(a:Attribute)<-[:HAS_ATTRIBUTE]-(t:Table) RETURN a,t", {"synonym": synonym})
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
                result = self.session.run("MATCH (t:Table)-[:HAS_ATTRIBUTE]->(:Attribute {value:{attribute}}) RETURN t", {"attribute": attribute})
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

    # choose which template should be used to create the query
    def choose_template(self, tables, columns, values):
        if tables == 1:
            if columns == 0:
                if values == 0:
                    return "temp1"
                elif values == 1:
                    return "temp2"
                elif values == 2:
                    return "temp3"
                else:
                    return -1
            elif columns == 1:
                if values == 0:
                    return "temp4"
                elif values == 1:
                    return "temp5"
                elif values == 2:
                    return "temp6"
                else:
                    return -1
            elif columns == 2:
                if values == 0:
                    return "temp7"
                else:
                    return -1
            else:
                return -1
        elif tables == 2:
            if columns == 0:
                if values == 0:
                    return "temp8"
                elif values == 1:
                    return "temp9"
                elif values == 2:
                    return "temp10"
                else:
                    return -1
            elif columns == 1:
                if values == 0:
                    return "temp11"
                elif values == 1:
                    return "temp12"
                elif values == 2:
                    return "temp13"
                else:
                    return -1
            elif columns == 2:
                if values == 0:
                    return "temp14"
                elif values == 1:
                    return "temp15"
                elif values == 2:
                    return "temp16"
                else:
                    return -1
            else:
                return -1

        elif tables == 3:
            if columns == 0:
                if values == 0:
                    return "temp17"
                else:
                    return -1
            elif columns == 1:
                if values == 0:
                    return "temp18"
                elif values == 1:
                    return "temp19"
                elif values == 2:
                    return "temp20"
                else:
                    return -1
            elif columns == 2:
                if values == 1:
                    return "temp21"
                else:
                    return -1
            else:
                return -1
        else:
            return -1

    def insert_into_template(self, template, tables, columns, values):
        insertions = {}
        # tables
        if len(tables) == 1:
            insertions['table'] = tables[0]
        elif len(tables) > 1:
            i = 0
            while i < len(tables):
                var = 'table' + str(i + 1)
                insertions[var] = tables[i]
                i += 1
        if len(columns) == 1:
            insertions['column'] = columns[0]
        elif len(columns) > 1:
            i = 0
            while i < len(columns):
                var = 'column' + str(i + 1)
                insertions[var] = columns[i]
                i += 1
        if len(values) == 1:
            insertions['attribute'] = values[0][0]
            insertions['value'] = values[0][1]
        elif len(values) > 1:
            i = 0
            while i < len(values):
                insertions['attribute' + str(i+1)] = values[i][0]
                insertions['value' + str(i+1)] = values[i][1]
                i += 1
        return template.safe_substitute(insertions)


    # returns the result of a query run on the MySQL database
    def run_query(self, query):
        csr = self.cnx.cursor()
        csr.execute(query)
        rslt = csr.fetchall()
        return rslt


# Main Function - Controls the flow
class Bot:
    def __init__(self, sentence):
        self.sentence = sentence
        self.tagged = Tokenizer.tag(sentence)
        self.lemmatized = Tokenizer.lemmatize(sentence)
        self.lemmatized_tagged = Tokenizer.tag(self.lemmatized)

    # returns a list of the responses from the SQL query
    def get_response(self):
        mapper = Mapper()
        # the tables to select from
        tables = set()
        # the attributes to select
        attributes = set()
        # the values to select with the associated attribute in the form (attribute, value)
        values = set()
        for word in self.lemmatized.split():
            # rslt[0] is in the form (table, attribute, value)
            rslt = mapper.match_label(word)
            print(rslt)
            if rslt:
                rslt = rslt[0]
                if rslt[0]:
                    # add to the tables
                    tables.add(rslt[0])
                if rslt[1]:
                    if rslt[2]:
                        # if there is a corresponding attribute, add to the values table
                        values.add((rslt[1], rslt[2]))
                    else:
                        attributes.add(rslt[1])
        print(tables, attributes, values)
        database = MySQL()
        tables = list(tables)
        attributes = list(attributes)
        values = list(values)
        template = database.choose_template(len(tables), len(attributes), len(values))
        if template != -1:
            print(template)
            query = database.insert_into_template(getattr(Templates, template), tables, attributes, values)
            print(query)
            print(database.run_query(query))

