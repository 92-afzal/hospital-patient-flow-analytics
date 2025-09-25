from pyspark.sql.functions import *

# Azure Event Hub Configuration
event_hub_namespace = "<<event_hub_namespace>>"
event_hub_name = "<<event_hub_name>>"
event_hub_conn_str = dbutils.secrets.get(scope = "vault", key = "eventhub_connection_name")

kafka_options = {
    "kafka.bootstrap.servers": f"{event_hub_namespace}:9093",
    "subscribe": event_hub_name,
    "kafka.security.protocol": "SASL_SSL",
    "kafka.sasl.mechanism": "PLAIN",
    "kafka.sasl.jaas.config": f'kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="{event_hub_conn_str}";',
    "startingOffsets": "latest",
    "failOnDataLoss": "false"
}

#Read from Eventhub

raw_df = (spark.readStream
           .format("kafka")
           .options(**kafka_options)
           .load()
)

# cast raw data to json string
json_df = raw_df.selectExpr("CAST(value AS STRING) AS raw_json")


# ADLS configuration
spark.conf.set(
    "fs.azure.account.key.storage_acct.dfs.core.windows.net",
    dbutils.secrets.get(scope = "vault", key = "storage_connection_name")
)

bronze_path = "abfss://<bronze_container>@<storage_acct>.dfs.core.windows.net/patient_flow"

# write stream of raw data

(
    json_df
    .writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation","dbfs:/mnt/bronze/_checkpoints/patient_flow")
    .start(bronze_path)
)

