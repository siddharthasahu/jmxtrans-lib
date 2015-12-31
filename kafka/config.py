servers = [
    {"host":"172.16.0.1","port":"9111","server_alias":"kafka-1"},
    {"host":"172.16.0.2","port":"9011","server_alias":"kafka-2"},
    {"host":"172.16.0.3","port":"8880","server_alias":"kafka-3"}
]
graphite_data = {
    "graphite_host": "graphite.myorg.com",
    "graphite_port": "2003",
    "graphite_prefix": "zookeeperCluster.jmxmetrics"
}
output_dir="output"
