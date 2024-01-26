<h1>Crawl newspaper</h1><br>
<span>Simple project using Scrapy framework to crawl data from online news. Additionally, Kafka and Java is also used to consume and handle data</span><br>
<br>
<h2>Prerequisites</h2>
<h3>Python</h3>

```
pip install scrapy
pip install mysql-connector-python
pip install kafka-python
```

<h3>Kafka</h3>
<span>Run Kafka</span>

```
cd consumer
docker compose up -d
```
<span>Check the status of Kafka</span>
```
docker-compose ps
```
<span>Create a topic</span>
```
docker-compose exec kafka kafka-topics.sh --create --topic <topic-name> --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092
```
<span>Check available topics</span>
```
docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092
```
