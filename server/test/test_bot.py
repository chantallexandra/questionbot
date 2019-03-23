import unittest
from server.bot import Mapper, Tokenizer, MySQL
from string import Template


class TestBot(unittest.TestCase):

    def setUp(self):
        self.mapper = Mapper()
        self.mysql = MySQL()

    # TEST TOKENIZER
    def test_tag(self):
        self.assertEqual(Tokenizer.tag("what are the italian restaurants"), [('what', 'WDT'), ('are', 'VBP'), ('the', 'DT'), ('italian', 'JJ'), ('restaurants', 'NNS')])
        self.assertEqual(Tokenizer.tag("what restaurants in mumbai have chinese food?"), [('what', 'WP'), ('restaurants', 'VBZ'), ('in', 'IN'), ('mumbai', 'NNS'), ('have', 'VBP'), ('chinese', 'VBN'), ('food', 'NN')])

    def test_lemmatized(self):
        self.assertEqual(Tokenizer.lemmatize("what are the italian restaurants"), "what are the italian restaurant")
        self.assertEqual(Tokenizer.lemmatize("restaurants flights them"), "restaurant flight them")

    # TEST MAPPER
    def test_match_labels(self):
        self.assertEqual(self.mapper.match_label("won't be found"), [])

        # Matching Values
        self.assertEqual(self.mapper.match_label("french"), [('cuisines','cuisine','french')])
        self.assertEqual(self.mapper.match_label("fish and chips"), [('cuisines', 'cuisine', 'fish and chips')])
        self.assertEqual(self.mapper.match_label("mumbai"), [('restaurants', 'city', 'mumbai')])
        self.assertEqual(self.mapper.match_label("canada"), [('code', 'country_name', 'canada')])

        # Matching Synonyms
        self.assertEqual(self.mapper.match_label("position"), [('restaurants', 'locality', False)])
        self.assertEqual(self.mapper.match_label("street"), [('restaurants', 'address', False)])

        # Matching Attributes
        self.assertEqual(self.mapper.match_label("city"), [('restaurants', 'city', False)])
        self.assertEqual(self.mapper.match_label("restaurant"), [('restaurants', 'restaurant_name', False)])
        self.assertEqual(self.mapper.match_label("country"), [('code', 'country_name', False)])
        self.assertEqual(self.mapper.match_label("food"), [('cuisines', 'cuisine', False)])

        # Matching Tables
        self.assertEqual(self.mapper.match_label("restaurants"), [('restaurants', False, False)])
        self.assertEqual(self.mapper.match_label("code"), [('code', False, False)])
        self.assertEqual(self.mapper.match_label("cuisines"), [('cuisines', False, False)])

        # Matching Multiple
        self.assertEqual(self.mapper.match_label("average"), [('restaurants', 'rating_text', 'average'), ('restaurants', 'average_cost_for_two', False)])
        # self.assertEqual(self.mapper.match_label("restaurant_id"), [('restaurants', 'restaurant_id', False),('cuisines', 'restaurant_id', False)])
        self.assertEqual(self.mapper.match_label("country_code"), [('code', 'country_code', False), ('restaurants', 'country_code', False)])

    # TEST MySQL
    def test_choose_template(self):
        self.assertEqual(self.mysql.choose_template(3, 2, 0), "temp320")
        self.assertEqual(self.mysql.choose_template(1, 1, 1), "temp111")
        self.assertEqual(self.mysql.choose_template(2, 0, 2), "temp202")
        self.assertEqual(self.mysql.choose_template(0, 2, 0), -1)
        self.assertEqual(self.mysql.choose_template(3, 2, 3), -1)

    def test_insert_into_template(self):
        self.assertEqual(self.mysql.insert_into_template(Template("SELECT DISTINCT * FROM $table1 NATURAL JOIN $table2"), ['restaurants', 'code'], [], []), "SELECT DISTINCT * FROM restaurants NATURAL JOIN code")
        self.assertEqual(self.mysql.insert_into_template(Template("SELECT DISTINCT $column FROM $table WHERE $attribute='$value'"), ['restaurants'], ['city'], [('street','123 westbrook')]), "SELECT DISTINCT city FROM restaurants WHERE street='123 westbrook'")


if __name__ == '__main__':
    unittest.main()