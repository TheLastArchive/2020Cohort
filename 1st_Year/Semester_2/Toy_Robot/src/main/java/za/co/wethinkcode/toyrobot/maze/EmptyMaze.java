package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.Obstacle;
import java.util.List;
import java.util.ArrayList;

public class EmptyMaze extends AbstractMaze {
    List<Obstacle> obstacleList = new ArrayList<>();

    @Override
    public boolean blocksPath(Position a, Position b) {
        //No obstacles so always return true
        return true;
    }

    public List<Obstacle> generateMaze() {
        return obstacleList;
    }

    public void clearObstacles() { obstacleList.clear(); }
}
