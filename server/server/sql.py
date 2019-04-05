import mysql.connector


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
        # use safe_substitute instead of substitute so that the program does not throw
        # an error if the wrong number of values are substituted in
        return template.safe_substitute(insertions)

    # returns the result of a query run on the MySQL database
    def run_query(self, query):
        csr = self.cnx.cursor()
        csr.execute(query)
        rslt = csr.fetchall()
        return rslt