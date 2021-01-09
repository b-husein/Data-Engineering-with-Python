'''
- Elasticsearch is a search engine, but in this case we will use it as 
  a NoSQL database. We will move data both to and from Elasticsearch to
  other locations. To download Elasticsearch, we need to:

  1. Use curl to download the files:
  
  curl https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.0-darwin-x86_64.tar.gz

  2. Extract the files using the following command:

  tar xvzf elasticsearch.tar.gz

  3. Ater extraction we can start Elasticsearch by running the command:

  bin/elasticsearch

  4. Once Elasticsearch has started, you can see the result at:

  http://localhost:9200

- Now that we have a NoSQL database running, we will need a relational database as well.

'''