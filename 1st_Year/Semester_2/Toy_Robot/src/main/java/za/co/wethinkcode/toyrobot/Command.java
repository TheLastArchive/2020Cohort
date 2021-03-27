package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.maze.SimpleMazeRunner;

import java.util.Arrays;

public abstract class Command {
    private final String name;
    private String argument;

    public abstract boolean execute(Robot target);

    public Command(String name){
        this.name = name.trim().toLowerCase();
        this.argument = "";
    }

    public Command(String name, String argument) {
        this(name);
        this.argument = argument.trim();
    }

    public String getName() {                                                                           //<2>
        return name;
    }

    public String getArgument() {
        return this.argument;
    }

    public static Command create(String instruction) {
        String[] args = instruction.toLowerCase().trim().split(" ");
        switch (args[0]){
            case "shutdown":
            case "off":
                return new ShutdownCommand();
            case "help":
                return new HelpCommand();
            case "left":
                return new LeftCommand();
            case "right":
                return new RightCommand();
            case "forward":
                return new ForwardCommand(args[1]);
            case "back":
                return new BackCommand(args[1]);
            case "sprint":
                return new SprintCommand(args[1]);
            case "replay":
                return new ReplayCommand(Arrays.toString(args));
            case "mazerun":
                return new MazeRunCommand(Arrays.toString(args));
            default:
                throw new IllegalArgumentException("Unsupported command: " + instruction);
        }
    }
}

