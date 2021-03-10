package za.co.wethinkcode.mastermind;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MastermindTest {

    @Test
    public void checkCodeTest() {

        Mastermind mastermind = new Mastermind();
        mastermind.code = "1234";
        assertEquals(0, mastermind.checkCode("5678"));
        assertEquals(1, mastermind.checkCode("1678"));
        assertEquals(2, mastermind.checkCode("1278"));
        assertEquals(3, mastermind.checkCode("1238"));
        assertEquals(4, mastermind.checkCode("1234"));
    }
}
