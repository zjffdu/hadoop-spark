

from pyspark.mllib.linalg import Vectors
from pyspark.ml.clustering import KMeans
from pyspark import SparkContext
from pyspark.sql import SQLContext

# sc = SparkContext(appName="test")
# sqlContext = SQLContext(sc)

data = [(Vectors.dense([0.0, 0.0]),), (Vectors.dense([1.0, 1.0]),),(Vectors.dense([9.0, 8.0]),), (Vectors.dense([8.0, 9.0]),)]
df = sqlContext.createDataFrame(data, ["features"])
kmeans = KMeans(k=2, seed=1)
model = kmeans.fit(df)

centers = model.clusterCenters()
model.transform(df).select("features", "prediction").collect()

