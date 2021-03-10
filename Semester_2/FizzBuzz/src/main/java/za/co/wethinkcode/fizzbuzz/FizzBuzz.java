package za.co.wethinkcode.fizzbuzz;

import java.util.ArrayList;

public class FizzBuzz {
    public String checkNumber(int number) {
        boolean divisibleBy3 = number % 3 == 0;
        boolean divisibleBy5 = number % 5 == 0;

        if (divisibleBy3 && divisibleBy5) {
            return "FizzBuzz";
        } else if (divisibleBy5) {
            return "Buzz";
        } else if (divisibleBy3) {
            return "Fizz";
        }
        return String.valueOf(number);
    }

    public String countTo(int number) {

        ArrayList<String> output = new ArrayList<>();
        for (int i = 1; i<= number; i++) {
            output.add(checkNumber(i));
        }
        return String.valueOf(output);
    }

}