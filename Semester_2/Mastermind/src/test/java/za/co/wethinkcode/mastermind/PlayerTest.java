package za.co.wethinkcode.mastermind;

import org.junit.jupiter.api.Test;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PlayerTest {

    private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

    @Test
    public void validInput() {
        Player player = new Player(new ByteArrayInputStream("1234\n5678".getBytes()));
        assertEquals("1234", player.getGuess());
        assertEquals("5678", player.getGuess());

    }
    @Test
    public void invalidInput() {
        Player player = new Player(new ByteArrayInputStream("12345\n123\na\nabcd\n1234".getBytes()));
        assertEquals("1234", player.getGuess());

    }

    @Test
    public void loseChance() {

        Player player = new Player();
        player.loseChance();
        assertEquals(11, player.getChances());
        player.loseChance();
        assertEquals(10, player.getChances());
    }
}
