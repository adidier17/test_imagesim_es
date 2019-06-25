import requests
import numpy as np
import json
from elasticsearch import Elasticsearch

fake_data = []
data_size = 10
es_index = 'es_image_search'
es_doc_type = 'image_data'

for i in range(data_size):
	vector = list(np.random.rand(512))
	vector = [num*10 for num in vector]
	fake_data.append(vector)


es_url = 'http://localhost:9200'
es = Elasticsearch(es_url)

# headers={'Content-Type': 'application/json'}

counter = 1
for vector in fake_data:
	data = {"fpath": "fake_path_" +str(counter),
	 		"image_feature": vector}
	res = es.index(index=es_index, doc_type=es_doc_type, body=data, id=counter)
	print(res["result"]) 
	counter +=1
# 	res = requests.put(es_url, headers=headers, data=json.dumps(data))
# 	print(res)


def get_first():
	res = es.get(index=es_index, doc_type=es_doc_type, id=1)
	if res["found"]:
		return res["_source"]
	else:
		print(f"get_first Result is: {res}")

def similar_images(size):
	query_image = get_first()
	print(f"image feature len: {lenquery_image['image_feature']}")
	query = {
			  "sort" : {
			    "_score" : "asc" 
			  },
			  "query": {
			    "function_score": {
			      "script_score": {
			        "script": {
			          "file": "image_similarity", 
			          "lang": "groovy",
			          "params": {
			            "query_feature": query_image["image_feature"]
			             }
			        }
			      }
			    }
			  },
			  "size" : size
			}

	res = es.search(index=es_index, body=query)
	for hit in res['hits']['hits']:
		print(f"id: {id} score: {score}")
