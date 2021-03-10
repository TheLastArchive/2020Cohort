package za.co.wethinkcode.mastermind;

import java.util.Random;

public class CodeGenerator {
    private final Random random;
    private String code = "";

    public CodeGenerator(){
        this.random = new Random();
    }

    public CodeGenerator(Random random){
        this.random = random;
    }

    /**
     * Generates a random 4 digit code, using this.random, where each digit is in the range 1 to 8 only.
     * Duplicated digits are allowed.
     * @return the generated 4-digit code
     */
    public String generateCode(){
        //TODO: implement using this.random
        for (int i = 0; i < 4; i++) {
            //Generates digits in range 0-7, add one to put it to 1-8
            this.code += Integer.toString(this.random.nextInt(8) + 1);
        }
        return code;
    }
}
