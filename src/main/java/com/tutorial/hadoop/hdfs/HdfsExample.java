package com.tutorial.hadoop.hdfs;


import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;

public class HdfsExample {

  public static void main(String[] args) throws IOException {
    Configuration conf = new Configuration();
    FileSystem fs = FileSystem.get(conf);
    FileStatus[] statuses = fs.listStatus(new Path("/"));
    for (FileStatus status : statuses) {
      System.out.println(status.getPath().toString() + "\t" + status.getLen());
    }

    PrintStream writer = new PrintStream(fs.create(new Path("/tmp/a.txt")));
    for (int i = 0; i < 10; ++i) {
      writer.println(i);
    }
    writer.close();

    BufferedReader reader = new BufferedReader(new InputStreamReader(fs.open(new Path("/tmp/a.txt"))));
    String line = null;
    while ((line = reader.readLine()) != null) {
      System.out.println(line);
    }
    reader.close();

  }
}
