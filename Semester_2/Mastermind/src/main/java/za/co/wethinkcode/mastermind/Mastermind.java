package za.co.wethinkcode.mastermind;


public class Mastermind {
    public static String code;
    private final Player player;


    public Mastermind(CodeGenerator generator, Player player){
        code = generator.generateCode();
        System.out.println("4-digit Code has been set. Digits in range 1 to 8." +
                " You have 12 turns to break it.");
        this.player = player;
    }
    public Mastermind(){
        this(new CodeGenerator(), new Player());
    }

    public void runGame(){
        //TODO: implement the main run loop logic
        while (!player.quit) {
            String userIn = player.getGuess();
            if (userIn == null) {
                player.loseChance();
            }
            else {
                checkCode(userIn);
            }
        }
        displayCode();
    }

    public int checkCode(String userCode) {

        int correctPlace = 0;
        int correctDigit = 0;
        StringBuilder tempCode = new StringBuilder(code);

        for (int i = 0; i < 4; i++) {
            if (this.code.charAt(i) == userCode.charAt(i)) {
                correctPlace++;
                tempCode.setCharAt(i, '_');
            }
        }
        for (int i = 0; i < 4; i++) {
            if (String.valueOf(tempCode).contains
                    (String.valueOf(userCode.charAt(i)))) {
                correctDigit++;
                int index = tempCode.indexOf(String.valueOf(userCode.charAt(i)));
                tempCode.setCharAt(index, '_');
            }
        }

        System.out.println("Number of correct digits in correct place: " + correctPlace);
        System.out.println("Number of correct digits not in correct place: " + correctDigit);
        if (correctPlace == 4) {
            winGame();
        }
        else {
            player.loseChance();
        }
        return correctPlace;
    }

    public void winGame() {
        System.out.println("Congratulations! You are a codebreaker!");
        player.endGame();
    }

    public static void displayCode() {
        System.out.println("The code was: " + code);
    }

    public static void main(String[] args){
        Mastermind game = new Mastermind();
        game.runGame();
    }
}
