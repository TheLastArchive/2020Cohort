package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.maze.*;
import za.co.wethinkcode.toyrobot.world.*;
import za.co.wethinkcode.toyrobot.maze.Maze;
import java.util.Scanner;


public class Play {
    static Scanner scanner;
    static IWorld world;
    static String selectedMaze;
    static Maze maze;

    public static void main(String[] args) {

        selectMaze(args);
        selectWorld(args);

        scanner = new Scanner(System.in);
        Robot robot;
        String name = getInput("What do you want to name your robot?");
        robot = new Robot(name);
        robot.setWorld(world);
        System.out.println("Hello Kiddo!");
        System.out.println("Loaded " + selectedMaze);
        world.generateObstacles(maze);
        System.out.println(robot.toString());

        Command command;
        boolean shouldContinue = true;
        do {
            String instruction = getInput(robot.getName() + "> What must I do next?").strip().toLowerCase();
            try {
                command = Command.create(instruction);
                shouldContinue = robot.handleCommand(command);
            } catch (IllegalArgumentException e) {
                robot.setStatus("Sorry, I did not understand '" + instruction + "'.");
            }
            System.out.println(robot);
        } while (shouldContinue);

    }

    private static String getInput(String prompt) {
        System.out.println(prompt);
        String input = scanner.nextLine();

        while (input.isBlank()) {
            System.out.println(prompt);
            input = scanner.nextLine();
        }
        return input;
    }

    public static void printStatus(Robot robot) {
        System.out.println(robot.toString());
    }

    public static void printOutput(String output) {
        System.out.println(output);
    }

    /**
     * Takes the command line arguments to create the IWorld object specified by the user
     * @param args command line arguments
     */
    public static void selectWorld(String[] args) {

        try {
            switch (args[0].toLowerCase()) {
                case "turtle":
                    world = new TurtleWorld(maze);
                    break;
                case "text":
                default:
                    world = new TextWorld(maze);
                    break;
            }
        }
        catch (IndexOutOfBoundsException e) {
            //Default to TextWorld if an incorrect argument is input
            world = new TextWorld(maze);
        }
    }

    /**
     * Takes the command line arguments to create the Maze object specified by the user
     * @param args command line arguments
     */
    public static void selectMaze(String[] args) {
        try {
            switch (args[1].toLowerCase()) {
                case "emptymaze":
                    maze = new EmptyMaze();
                    selectedMaze = "EmptyMaze";
                    break;
                case "simplemaze":
                    maze = new SimpleMaze();
                    selectedMaze = "SimpleMaze";
                    break;
                case "designedmaze":
                    maze = new DesignedMaze();
                    selectedMaze = "DesignedMaze";
                    break;
                case "randommaze":
                default:
                    maze = new RandomMaze();
            }
        } catch (IndexOutOfBoundsException e) {
            //Default to RandomMaze if an incorrect argument is input
            maze = new RandomMaze();
        }
    }
}