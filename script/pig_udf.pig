
register target/original-hadoop-spark-1.0-SNAPSHOT.jar;

A = load 'data/wordcount/input';
B = foreach A generate flatten(TOKENIZE(com.tutorial.pig.Lower((chararray)$0))) as word;
C = group B by word;
D = foreach C generate group, COUNT(B) as count;
E = order D by count desc;
F = limit E 10;
dump F;