from string import Template


class Templates:
    # temp names are in the format temp{t,c,v} where t = # tables,
    # c = # columns, v = # attribute-value pairs

    # zero columns, one table
    temp100 = Template("SELECT DISTINCT * FROM $table")
    # zero columns, one table, one attribute-value pair
    temp101 = Template("SELECT DISTINCT * FROM $table WHERE $attribute='$value'")
    # zero columns, one table, two attribute-value pairs (AND)
    temp102 = Template("SELECT DISTINCT * FROM $table WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # one column, one table
    temp110 = Template("SELECT DISTINCT $column FROM $table")
    # one column, one table, one attribute-value pair
    temp111 = Template("SELECT DISTINCT $column FROM $table WHERE $attribute='$value'")
    # one column, one table, two attribute-value pairs (AND)
    temp112 = Template("SELECT DISTINCT $column FROM $table WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # two columns, one table
    temp120 = Template("SELECT DISTINCT $column1, $column2 FROM $table")
    # two column, one table, one attribute-value pairs (AND)
    temp121 = Template("SELECT DISTINCT $column1, $column2 FROM $table WHERE $attribute='$value'")
    # two column, one table, two attribute-value pairs (AND)
    temp122 = Template("SELECT DISTINCT $column1, $column2 FROM $table WHERE $attribute1='$value1' AND $attribute2='$value2'")

    # zero columns, two tables
    temp200 = Template("SELECT DISTINCT * FROM $table1 NATURAL JOIN $table2")
    # zero columns, two tables, one attribute-value pair
    temp201 = Template("SELECT DISTINCT * FROM $table1 NATURAL JOIN $table2 WHERE $attribute='$value'")
    # zero columns, two tables, two attribute-value pairs
    temp202 = Template("SELECT DISTINCT * FROM $table1 NATURAL JOIN $table2 WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # one column, two tables
    temp210 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2")
    # one column, two tables, one attribute-value pair
    temp211 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 WHERE $attribute='$value'")
    # one column, two tables, two attribute-value pairs (AND)
    temp212 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # two columns, two tables
    temp220 = Template("SELECT DISTINCT $column1, $column2  FROM $table1 NATURAL JOIN $table2")
    # two columns, two tables, one attribute-value pair
    temp221 = Template("SELECT DISTINCT $column1, $column2 FROM $table1 NATURAL JOIN $table2 WHERE $attribute='$value'")
    # two columns, two tables, two attribute-value pairs (AND)
    temp222 = Template("SELECT DISTINCT $column1, $column2 FROM $table1 NATURAL JOIN $table2 WHERE $attribute1='$value1' AND $attribute2='$value2'")

    # zero columns, three tables
    temp300 = Template("SELECT DISTINCT * FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3")
    # zero columns, three tables, one attribute-value pair (AND)
    temp301 = Template("SELECT DISTINCT * FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute='value'")
    # zero columns, three tables, two attribute-value pairs (AND)
    temp302 = Template("SELECT DISTINCT * FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # one column, three tables
    temp310 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3")
    # two column, three tables
    temp320 = Template("SELECT DISTINCT $column1, #column2 FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3")
    # one column, three tables, one attribute-value pair (AND)
    temp311 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute='value'")
    # one column, three tables, two attribute-value pairs (AND)
    temp312 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # two columns, three tables, one attribute-value pair (AND)
    temp321 = Template("SELECT DISTINCT $column1, $column2 FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute='$value'")
    # two columns, three tables, two attribute-value pair (AND)
    temp322 = Template("SELECT DISTINCT $column1, $column2 FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute1='$value1' AND $attribute2='$value2'")
