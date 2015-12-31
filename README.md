Introduction
============
Python scripts for generating [JMXTrans](https://github.com/jmxtrans/jmxtrans) JSON configuration files for Apache Hadoop, Apache Zookeeper, Apache Cassandra, LinkedIn's Kafka and Twitter Storm.

I use these when I add a new node to these clusters or a new column family to Cassandra. I update the script with the new node, run these python scripts and update the JMXTrans server JSON files.

These were tested with the following versions:

* Apache Zookeeper: 3.3.4
* Apache Tomcat: 7

Installation
============
There is no installation. Look at the various `genjmxtrans.py` and specify the host details and graphite endpoints in `config.py`.
