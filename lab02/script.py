from pyspark.sql import SparkSession
# Создаем сессию Spark на локальном компьютере
spark = SparkSession.builder.master("local[*]").getOrCreate()

import collections
rdd = spark.sparkContext.textFile("/content/sample_data/ml-100k/u.data")
#<put your code here>

def printStat(inp):
  #<put your code here>
  print(f'Marks for film {ind}: 1 -> {marks[0]}, 2 -> {marks[1]}, 3 -> {marks[2]}, 4 -> {marks[3]}, 5 -> {marks[4]}')

for i in aggPairRDD.mapValues(lambda x: dict(collections.Counter(x))).collect():
  printStat(i)

#<put your code here>