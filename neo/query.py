from neo.config import graph


def query_all_rela():
    query = 'MATCH (n) RETURN n LIMIT 25'
    result = graph.run(query)
    return result.data()
