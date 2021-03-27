package za.co.wethinkcode.toyrobot;

public class HelpCommand extends Command {

    public HelpCommand() {
        super("help");
    }

    @Override
    public boolean execute(Robot target) {
        target.setStatus("I can understand these commands:\n" +
                "OFF  - Shut down robot\n" +
                "HELP - provide information about commands\n" +
                "FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\n" +
                "SPRINT - move forward in descending values from a specified value\n" +
                "REPLAY - Replay all movement commands given to the robot\n" +
                "#REPLAY MUTATORS# - reversed, range (digit or digit-digit" +
                "MAZERUN - Solve the given maze, can solve to top, bottom, left, or right.");
        return true;
    }
}
