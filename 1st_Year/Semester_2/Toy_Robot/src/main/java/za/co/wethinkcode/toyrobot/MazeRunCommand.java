package za.co.wethinkcode.toyrobot;
import za.co.wethinkcode.toyrobot.maze.SimpleMazeRunner;
import za.co.wethinkcode.toyrobot.world.IWorld;

class MazeRunCommand extends Command {

    public MazeRunCommand(String argument) {
        super("mazerun", argument);
    }

    public boolean execute(Robot target) {

        target.setStatus("Starting maze run..");
        SimpleMazeRunner mazerun = new SimpleMazeRunner();
        IWorld.Direction direction;

        switch (getArgument().toLowerCase().replaceAll("[\\[\\],]", "")) {
            case "mazerun":
            case "mazerun top":
                direction = IWorld.Direction.UP;
                break;
            case "mazerun bottom":
                direction = IWorld.Direction.DOWN;
                break;
            case "mazerun left":
                direction = IWorld.Direction.LEFT;
                break;
            case "mazerun right":
                direction = IWorld.Direction.RIGHT;
                break;
            default:
                target.setStatus("Invalid command");
                return true;
        }
        mazerun.mazeRun(target, direction);

        return true;
    }
}
