package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class SprintCommand extends Command{

    public SprintCommand(String argument) {
        super("sprint", argument);
    }

    @Override
    public boolean execute(Robot target) {
        int nrSteps = Integer.parseInt(getArgument());
        for (int i = nrSteps; i > 0; i--) {
            IWorld.UpdateResponse response = target.getWorld().updatePosition(i);
            switch (response) {
                case FAILED_OUTSIDE_WORLD:
                    target.setStatus("Sorry, I cannot go outside my safe zone.");
                    Play.printStatus(target);
                    break;
                case FAILED_OBSTRUCTED:
                    target.setStatus("Sorry, there is an obstacle in the way.");
                    Play.printStatus(target);
                    break;
                default:
                    target.setStatus("Moved forward by " + i + " steps.");
                    if (i > 1) { Play.printStatus(target); }
                    break;
            }
        }
        if (!ReplayCommand.replayInProgress) {
            target.addCommandList("sprint " + String.valueOf(nrSteps));
        }
        return true;
    }
}
