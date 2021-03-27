package za.co.wethinkcode.toyrobot;

public class LeftCommand extends Command {
    public LeftCommand() { super("left"); }

    @Override
    public boolean execute(Robot target) {

        target.getWorld().updateDirection(false);
        target.setStatus("Turned left.");

        //Check if replay is in progress
        if (!ReplayCommand.replayInProgress) {
            target.addCommandList("left");
        }
        return true;
    }
}
