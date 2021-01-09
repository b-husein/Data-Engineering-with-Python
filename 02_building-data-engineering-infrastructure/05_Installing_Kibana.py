''' 
- Elasticsearch doesn not ship with a GUI, but rather an API; 
  In order to add a GUI to elasticsearch we can use Kibana.

- Kibana will allow us an access to the Elasticsearch API in GUI
  but more importantly we can use it to build visualizations and 
  dashboards of our data held in Elasticsearch. We can install Kibana
  with:

1. Using wget, add the key:

    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

2. Then, add the repository along with it:

    echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list

3. Lastly, update apt and install Kibana:

    sudo apt-get update
    sudo apt-get install kibana






'''