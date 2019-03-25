from server.mapper import Mapper
from server.tokenizer import Tokenizer
from server.sql_templates import Templates
from server.mysql import MySQL


# Controls the flow
class Bot:
    def __init__(self, sentence):
        self.sentence = sentence
        self.lemmatized = Tokenizer.lemmatize(self.sentence)
        self.query_terms = Tokenizer.noun_adj_extractor(self.lemmatized)

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
            rslt = Mapper.match_label(word)
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
        for a, v in values:
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
