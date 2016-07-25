package com.tutorial.pig;


import org.apache.pig.ExecType;
import org.apache.pig.PigServer;

import java.io.IOException;

public class PigExample {

  public static void main(String[] args) throws IOException {
    PigServer pigServer = new PigServer(ExecType.LOCAL);
    pigServer.registerScript("script/pig_udf.pig");
  }
}
