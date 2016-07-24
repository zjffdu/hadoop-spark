

from pyspark.ml.classification import LogisticRegression
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors

data= [LabeledPoint(0.0, Vectors.dense([0.0,0.0]),), LabeledPoint(0.0, Vectors.dense([0.0,0.1])), LabeledPoint(1.0, Vectors.dense([5.0,5.0])), LabeledPoint(1.0, Vectors.dense([6.0,6.0])),LabeledPoint(1.0, Vectors.dense([7.0,7.0]))]

training = sqlContext.createDataFrame(data[0:-1])
testing = sqlContext.createDataFrame(data[-1:])

lr = LogisticRegression(maxIter=5, regParam=0.01)
model = lr.fit(training)
result = model.transform(testing)



