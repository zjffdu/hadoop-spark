package com.tutorial.pig;


import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

import java.io.IOException;

public class Lower extends EvalFunc<String>{
  @Override
  public String exec(Tuple input) throws IOException {
    String word = (String) input.get(0);
    if (word == null) {
      return "";
    }
    return word.toLowerCase();
  }
}
