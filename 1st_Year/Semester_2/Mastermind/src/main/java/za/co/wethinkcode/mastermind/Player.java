package za.co.wethinkcode.mastermind;

import java.io.InputStream;
import java.util.Scanner;

public class Player {
    private final Scanner inputScanner;
    public boolean quit = false;
    private int chances = 12;


    public Player(){
        this.inputScanner = new Scanner(System.in);
    }

    public Player(InputStream inputStream){
        this.inputScanner = new Scanner(inputStream);
    }

    /**
     * Gets a guess from user via text console.
     * This must prompt the user to re-enter a guess until a valid 4-digit string is entered,
     * or until the user enters `exit` or `quit`.
     *
     * @return the value entered by the user
     */
    public String getGuess(){


        System.out.println("Input 4 digit code:");
        String newString = this.inputScanner.nextLine();

        while (!is4Digit(newString)) {
            if (wantsToQuit(newString)) {
                return null;
            }
            else {
                System.out.println("Please enter exactly 4 digits (each from 1 to 8).");
                System.out.println("Input 4 digit code:");
                newString = this.inputScanner.nextLine();}
        }
        return newString;
        }

    public boolean wantsToQuit(String newString) {

        this.quit = newString.equalsIgnoreCase("quit")
                || newString.equalsIgnoreCase("exit");
        return quit;
    }

    public void endGame() {
        this.quit = true;
    }

    public boolean is4Digit(String newString) {

        if (newString.length() != 4) {
            return false;
        }
        for (int i = 0; i < 4; i++) {
            // - '0' to check the ASCII value
            if (newString.charAt(i) - '0' > 8 || newString.charAt(i) - '0' < 1) {
                return false;
            }
        }
        return true;
    }

    public void loseChance() {

        this.chances--;
        if (this.chances < 1) {
            System.out.println("No more turns left.");
            endGame();
        }
        else if (!this.quit) {
            System.out.println("Turns left: " + getChances());
        }
    }

    public int getChances() {

        return this.chances;
    }
}

