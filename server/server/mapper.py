from neo4j import GraphDatabase
from server.map import Map


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
                return matching_table, matching_attribute, token
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