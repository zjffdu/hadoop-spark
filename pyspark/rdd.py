
rdd = sc.parallelize(range(1,11))
sum = rdd.sum()
count = rdd.count()
print(sum/count)




rdd = sc.parallelize([('a',1), ('b', 2), ('a', 3)])
rdd2 = rdd.map(lambda x : (x[0].upper(),x[1]))
rdd3 = rdd2.reduceByKey(lambda a,b : a+b)
rdd3.collect()



