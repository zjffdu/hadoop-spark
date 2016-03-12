import org.apache.spark.sql.SQLContext
import org.apache.spark.{SparkContext, SparkConf}
import org.apache.spark.sql.Row

object SparkSQLExample {

  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("example").setMaster("local[4]")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
    import sqlContext.implicits._
    val df = sqlContext.read.text("data/wordcount/input").toDF("text")
    df.printSchema()
    val wcDF = df.explode('text) {
      (r: Row) =>  r.getString(0).split("\\s").map(Tuple1(_)).toSeq
    }.toDF("text", "word")
    .select("word")
    .groupBy("word")
    .count()

    wcDF.collect() foreach println
  }
}
