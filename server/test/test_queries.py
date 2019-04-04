'''
    This file is to run a set of English Question on Bot and view the query that is generated
'''

from server.bot import Bot


class TestQueries:

    def test_bot(self):
        test_queries = ["what are the italian restaurants?", "which restaurants have indian cuisine?", "what restaurants are in australia?",
                        "what are the restaurants in athens?", "what restaurants in mumbai have chinese food?", "which chinese restaurants are in mumbai?",
                        "which restaurants have an excellent rating?",
                        "what are the cities in canada?", "what cities have dim sum?", "how many restaurants serve french food?",
                        "which restaurants have indian cuisine and what is their city?", "which restaurants have delivery"]
        for i in range(0, len(test_queries)):
            query = test_queries[i]
            print("----------------------------------------------------")
            print("Testing Query Number {}: '{}'".format(i+1, query))
            query_bot = Bot(query)
            print("{}".format(query_bot.generate_query()[0]))

if __name__ == '__main__':
    test = TestQueries()
    test.test_bot()