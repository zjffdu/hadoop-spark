import org.apache.spark.{SparkContext, SparkConf}

object SparkExample {


  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("example").setMaster("local[4]")
    val sc = new SparkContext(conf)
    val wordcount = sc.textFile("data/wordcount/input")
      .flatMap(line=>line.split("\\s"))
      .countByValue()
    wordcount foreach println
  }
}
