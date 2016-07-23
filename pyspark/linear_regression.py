
from pyspark.mllib.linalg import Vectors
from pyspark.ml.regression import LinearRegression
from pyspark.mllib.regression import LabeledPoint

data= [LabeledPoint(0.0, Vectors.dense([0.0]),), LabeledPoint(0.99, Vectors.dense([1.0])), LabeledPoint(2.0, Vectors.dense([2.0])), LabeledPoint(3.01, Vectors.dense([3.0]))]
training = sqlContext.createDataFrame(data)

lr = LinearRegression(maxIter=100, regParam=0.05, elasticNetParam=0.8)
lrModel = lr.fit(training)
print("Coefficients: " + str(lrModel.coefficients))
print("Intercept: " + str(lrModel.intercept))

