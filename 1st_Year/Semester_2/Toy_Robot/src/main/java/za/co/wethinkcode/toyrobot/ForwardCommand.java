package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;

public class ForwardCommand extends Command {

    public ForwardCommand(String argument) {
        super("forward", argument);
    }

    @Override
    public boolean execute(Robot target) {
        int nrSteps = Integer.parseInt(getArgument());

        IWorld.UpdateResponse response = target.getWorld().updatePosition(nrSteps);
        switch (response) {
            case FAILED_OUTSIDE_WORLD:
                target.setStatus("Sorry, I cannot go outside my safe zone.");
                break;
            case FAILED_OBSTRUCTED:
                target.setStatus("Sorry, there is an obstacle in the way.");
                break;
            default:
                target.setStatus("Moved forward by " + nrSteps + " steps.");
                break;
        }

        //Check if replay is in progress
        if (!ReplayCommand.replayInProgress) {
            target.addCommandList("forward " + String.valueOf(nrSteps));
        }
        return true;
    }
}

