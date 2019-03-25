from neo4j import GraphDatabase
from textblob import TextBlob, Word
import mysql.connector
from server.map import Map
from server.sql_templates import Templates
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
        print(sentence.tags)
        return sentence.tags

    # Returns the extracted noun phrase from the tokens
    @classmethod
    def noun_phrase(cls, tokens):
        sentence = TextBlob(tokens)
        return sentence.noun_phrases


    # Returns a tagged version of the lemmatized tokens
    @classmethod
    def lemmatize(cls, tokens):
        sentence = TextBlob(tokens)
        words = sentence.words
        lemmatized = ""
        for word in words:
            lemmatized += Word(word).lemmatize() + " "
        return lemmatized[:-1]

    # Returns a list of the noun-phrases, nouns, and adjectives
    @classmethod
    def noun_adj_extractor(cls, sentence):
        noun_adj = []
        tagged = Tokenizer.tag(sentence)
        noun_p = Tokenizer.noun_phrase(sentence)
        for np in noun_p:
            noun_adj.append(np)

        for word,pos in tagged:
            # check if the word is a noun or adjective
            if pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS" or pos =="JJ" or pos == "JJR" or pos == "JJS":
                noun_adj.append(word)
        # print(noun_adj)
        return noun_adj


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
        # check if the token corresponds to a value
        matching_value = self.match_value(token)
        if matching_value:
            all_matches.append(matching_value)

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
                all_matches.extend(self.match_synonym(synonym))
            elif label == "Attribute":
                attribute = list(node.values())[0]
                all_matches.extend(self.match_attribute(attribute))
            elif label == "Table":
                table = list(node.values())[0]
                all_matches.append((table, None, None))
        return all_matches

    # match_value tries to match the token to a value in the mapping table
    # If a match is found, it returns the match in the form (table, attribute, value)
    # If a match is not found, it returns None
    def match_value(self, token):
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
                return (matching_table, matching_attribute, token)
        return None

    # match_attributes tries to match the token to an attribute in the Neo4j database
    # If a match is found, it returns the match in the form (table, attribute, value)
    # If a match is not found, it returns None
    def match_attribute(self, attribute):
        all_matches = []
        # find the corresponding table(s) the attribute belongs to
        result = self.session.run("MATCH (t:Table)-[:HAS_ATTRIBUTE]->(:Attribute {value:{attribute}}) RETURN t",
                                  {"attribute": attribute})
        # use results.peek() because we only want the first result
        if result.peek() and result.peek().get('t'):
            table_iterator = result.records()
            while result.peek():
                curr_node = next(table_iterator)
                # extract the table name from the result
                matching_table = list(curr_node.get('t').values())[0]
                all_matches.append((matching_table, attribute, None))
        return all_matches

    # match_value tries to match the token to an synonym in the Neo4j database
    # If a match is found, it returns the match in the form (table, attribute, value)
    # If a match is not found, it returns None
    def match_synonym(self, synonym):
        all_matches = []
        # find the corresponding table(s) and attribute
        result = self.session.run(
            "MATCH (:Synonym {value:{synonym}})-[:IS_LIKE]->(a:Attribute)<-[:HAS_ATTRIBUTE]-(t:Table) RETURN a,t",
            {"synonym": synonym})
        if result.peek() and result.peek().get('a') and result.peek().get('t'):
            table_iterator = result.records()
            while result.peek():
                curr_node = next(table_iterator)
                matching_attribute = list(curr_node.get('a').values())[0]
                matching_table = list(curr_node.get('t').values())[0]
                all_matches.append((matching_table, matching_attribute, None))
        return all_matches



class MySQL:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', database='zomato')

    # choose which template should be used to create the query
    def choose_template(self, tables, columns, values):
        if 1 <= tables <= 3 and 0 <= columns <= 2 and 0 <= values <= 2:
            return "temp" + str(tables) + str(columns) + str(values)
        else:
            return -1

    # takes a Template and list of tables, columns, and values
    # returns a string with the values inserted
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
        self.lemmatized = Tokenizer.lemmatize(self.sentence)
        self.query_terms = Tokenizer.noun_adj_extractor(self.lemmatized);

    def generate_query(self):
        mapper = Mapper()
        # the tables to select from
        tables = set()
        # the attributes to select
        attributes = set()
        # the values to select with the associated attribute in the form (attribute, value)
        values = set()
        for word in self.query_terms:
            # rslt[0] is in the form (table, attribute, value)
            rslt = mapper.match_label(word)
            # print(rslt)
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
        # Remove elements from attributes which are also in values
        for a,v in values:
            if a in attributes:
                attributes.remove(a)
        # print(tables, attributes, values)
        database = MySQL()
        tables = list(tables)
        attributes = list(attributes)
        values = list(values)
        template = database.choose_template(len(tables), len(attributes), len(values))
        if template != -1:
            # print(template)
            query = database.insert_into_template(getattr(Templates, template), tables, attributes, values)
            return query, attributes
        else:
            return None, None

    # returns a list of the responses from the SQL query
    def get_response(self, query):
        if query:
            database = MySQL()
            rslt = database.run_query(query)
            # convert query responses to strings
            rslt = [tuple(str(x) for x in tup) for tup in rslt]
            return rslt


