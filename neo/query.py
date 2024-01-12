from neo.config import graph


# def query_all_rela():
#     query = 'MATCH (n) RETURN n LIMIT 25'
#     result = graph.run(query)
#     return result.data()


def query(name):
    data = graph.run(
        "match(p:API {Name:'%s'}) -[r]->(n) return p.Name, type(r), n.Name, p.cate, n.cate" % name
    )
    data = list(data)
    return get_json_data(data)


def get_json_data(data):
    json_data = {'data': [], "links": []}
    d = []
    CA_LIST = {"API": 0, "PrimaryCategory": 1, "APIProvider": 2}

    for i in data:
        # print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
        d.append(i['p.Name'] + "_" + i['p.cate'])
        d.append(i['n.Name'] + "_" + i['n.cate'])
        d = list(set(d))
    name_dict = {}
    count = 0
    for j in d:
        j_array = j.split("_")

        data_item = {}
        name_dict[j_array[0]] = count
        count += 1
        data_item['name'] = j_array[0]
        data_item['cate'] = CA_LIST[j_array[1]]
        json_data['data'].append(data_item)
    for i in data:
        link_item = {}

        link_item['source'] = name_dict[i['p.Name']]
        link_item['target'] = name_dict[i['n.Name']]
        link_item['value'] = i['type(r)']
        json_data['links'].append(link_item)

    return json_data
