

import pyspark.sql.functions as F

df = sqlContext.createDataFrame([('a', 1), ('b', 2), ('a', 3)], ["key", "value"])
df2 = df.withColumn('key', F.upper(df.key))
df2.groupBy('key').agg(F.avg(df.value)).collect()


