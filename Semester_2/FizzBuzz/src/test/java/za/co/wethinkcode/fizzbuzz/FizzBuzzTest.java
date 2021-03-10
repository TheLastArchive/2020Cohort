package za.co.wethinkcode.fizzbuzz;

import org.junit.jupiter.api.Test;
import za.co.wethinkcode.fizzbuzz.FizzBuzz;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FizzBuzzTest {
    @Test
    public void notDivisibleBy3or5() {
        za.co.wethinkcode.fizzbuzz.FizzBuzz fizzBuzz = new za.co.wethinkcode.fizzbuzz.FizzBuzz();
        String result = fizzBuzz.checkNumber(13);
        assertEquals("13", result);
    }

    @Test
    public void divisibleBy3() {
        za.co.wethinkcode.fizzbuzz.FizzBuzz fizzBuzz = new FizzBuzz();
        assertEquals("Fizz", fizzBuzz.checkNumber(3));
        assertEquals("Fizz", fizzBuzz.checkNumber(6));
        assertEquals("8", fizzBuzz.checkNumber(8));
    }

    @Test
    public void divisibleBy5() {
        za.co.wethinkcode.fizzbuzz.FizzBuzz fizzBuzz = new FizzBuzz();
        assertEquals("Buzz", fizzBuzz.checkNumber(5));
        assertEquals("Buzz", fizzBuzz.checkNumber(10));
        assertEquals("8", fizzBuzz.checkNumber(8));
    }

    @Test void divisibleBy3And5() {
        za.co.wethinkcode.fizzbuzz.FizzBuzz fizzBuzz = new FizzBuzz();
        assertEquals("FizzBuzz", fizzBuzz.checkNumber(15));
        assertEquals("FizzBuzz", fizzBuzz.checkNumber(30));
        assertEquals("29", fizzBuzz.checkNumber(29));
    }

    @Test
    public void generateUpTo15() {
        za.co.wethinkcode.fizzbuzz.FizzBuzz fizzBuzz = new FizzBuzz();
        String result = fizzBuzz.countTo(15);
        assertEquals("[1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz]", result);
    }
}
