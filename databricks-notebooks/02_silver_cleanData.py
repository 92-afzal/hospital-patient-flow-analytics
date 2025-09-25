from pyspark.sql.types import *
from pyspark.sql.functions import *
from sklearn.model_selection import train_test_split

# ADLS config
spark.conf.set(
    "fs.azure.account.key.hospitalstorageaccnt.dfs.core.windows.net",
    dbutils.secrets.get(scope="valt", key="connection")
)

bronze_path = "abfss://<bronze_container>@<storage_acct>.dfs.core.windows.net/patient_flow"
silver_path = "abfss://<silver_container>@<storage_acct>.dfs.core.windows.net/patient_flow"

# Read stream from Bronze
bronze_df = (
    spark.readStream
    .format("delta")
    .load(bronze_path)
)

# Define schema
schema = StructType([
    StructField("patient_id", StringType()),
    StructField("gender", StringType()),
    StructField("age", IntegerType()),
    StructField("department", StringType()),
    StructField("admission_time", StringType()),
    StructField("discharge_time", StringType()),
    StructField("bed_id", IntegerType()),
    StructField("hospital_id", IntegerType())
])

# Parse raw json
parse_df = bronze_df.withColumn("data", from_json(col("raw_json"), schema)).select("data.*")

# Clean time columns
clean_df = parse_df.withColumn("admission_time", to_timestamp("admission_time"))
clean_df = clean_df.withColumn("discharge_time", to_timestamp("discharge_time"))

clean_df = clean_df.withColumn(
    "admission_time",
    when(
        col("admission_time").isNull() | (col("admission_time") > current_timestamp()),
        current_timestamp()
    ).otherwise(col("admission_time"))
)

# Fix age
clean_df = clean_df.withColumn(
    "age",
    when(
        col("age") >= 100,
        floor(rand() * 90 + 1).cast("int")
    ).otherwise(col("age"))
)

# Ensure all expected columns exist
expected_cols = ["patient_id", "gender", "age", "department", "admission_time", "discharge_time", "bed_id", "hospital_id"]

for col_name in expected_cols:
    if col_name not in clean_df.columns:
        clean_df = clean_df.withColumn(col_name, lit(None))

# Write to Silver
(
    clean_df
    .writeStream
    .format("delta")
    .outputMode("append")
    .option("mergeSchema", "true")
    .option("checkpointLocation", silver_path + "_checkpoint")
    .start(silver_path)
)
