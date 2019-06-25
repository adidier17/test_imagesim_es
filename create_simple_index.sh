curl -X PUT "localhost:9200/es_image_search" -H 'Content-Type: application/json' -d'
{
    "settings" : {
        "number_of_shards" : 3,
        "number_of_replicas" : 2
    },
    "mappings" : {
        "image_data" : {
            "properties" : {
                "fpath" : { "type" : "keyword"},
                "image_feature": {"type": "float"}
       
            }
        }
    }
}
'
