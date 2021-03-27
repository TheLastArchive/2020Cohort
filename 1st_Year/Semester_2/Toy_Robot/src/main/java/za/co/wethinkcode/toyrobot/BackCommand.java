package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class BackCommand extends Command {

    public BackCommand(String argument) {
        super("back", argument);
    }

    @Override
    public boolean execute(Robot target) {
        int nrSteps = Integer.parseInt(getArgument());
        IWorld.UpdateResponse response = target.getWorld().updatePosition(nrSteps * -1);
        switch (response) {
            case FAILED_OUTSIDE_WORLD:
                target.setStatus("Sorry, I cannot go outside my safe zone.");
                break;
            case FAILED_OBSTRUCTED:
                target.setStatus("Sorry, there is an obstacle in the way.");
                break;
            default:
                target.setStatus("Moved back by " + nrSteps + " steps.");
                break;
        }

        //Check if replay is in progress
        if (!ReplayCommand.replayInProgress) {
            target.addCommandList("back "+ String.valueOf(nrSteps));
        }
        return true;
    }
}