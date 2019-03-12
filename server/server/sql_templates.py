from string import Template


class Templates:

    # zero columns, one table
    temp1 = Template("SELECT * FROM $table")
    # zero columns, one table, one attribute-value pair
    temp2 = Template("SELECT * FROM $table WHERE $attribute='$value'")
    # zero columns, one table, two attribute-value pairs (AND)
    temp3 = Template("SELECT * FROM $table WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # one column, one table
    temp4 = Template("SELECT DISTINCT $column FROM $table")
    # one column, one table, one attribute-value pair
    temp5 = Template("SELECT DISTINCT $column FROM $table WHERE $attribute='$value'")
    # one column, one table, two attribute-value pairs (AND)
    temp6 = Template("SELECT DISTINCT $column FROM $table WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # two columns, one table
    temp7 = Template("SELECT $column1, $column2 FROM $table")

    # zero columns, two tables
    temp8 = Template("SELECT * FROM $table1 NATURAL JOIN $table2")
    # zero columns, two tables, one attribute-value pair
    temp9 = Template("SELECT * FROM $table1 NATURAL JOIN $table2 WHERE $attribute='$value'")
    # zero columns, two tables, one attribute-value pair
    temp10 = Template("SELECT * FROM $table1 NATURAL JOIN $table2 WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # one column, two tables
    temp11 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2")
    # one column, two tables, one attribute-value pair
    temp12 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 WHERE $attribute='$value'")
    # one column, two tables, two attribute-value pairs (AND)
    temp13 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # two columns, two tables
    temp14 = Template("SELECT $column1, $column2  FROM $table1 NATURAL JOIN $table2")
    # two columns, two tables, one attribute-value pair
    temp15 = Template("SELECT $column1, $column2 FROM $table1 NATURAL JOIN $table2 WHERE $attribute='$value'")
    # two columns, two tables, two attribute-value pairs (AND)
    temp16 = Template("SELECT $column1, $column2 FROM $table1 NATURAL JOIN $table2 WHERE $attribute1='$value1' AND $attribute2='$value2'")

    # zero columns, three tables
    temp17 = Template("SELECT * FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3")
    # one column, three tables
    temp18 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3")
    # one column, three tables, one attribute-value pair (AND)
    temp19 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute='value'")
    # one column, three tables, two attribute-value pairs (AND)
    temp20 = Template("SELECT DISTINCT $column FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute1='$value1' AND $attribute2='$value2'")
    # two columns, three tables, one attribute-value pair (AND)
    temp21 = Template("SELECT $column1, $column2 FROM $table1 NATURAL JOIN $table2 NATURAL JOIN $table3 WHERE $attribute='$value'")