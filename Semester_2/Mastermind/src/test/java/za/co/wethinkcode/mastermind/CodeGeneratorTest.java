package za.co.wethinkcode.mastermind;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CodeGeneratorTest {

    @Test
    public void fourDigitCode() {
        for (int i = 0; i < 100; i++) {
            CodeGenerator codeGenerator = new CodeGenerator();
            assertEquals(4, codeGenerator.generateCode().length());
        }
    }
}
