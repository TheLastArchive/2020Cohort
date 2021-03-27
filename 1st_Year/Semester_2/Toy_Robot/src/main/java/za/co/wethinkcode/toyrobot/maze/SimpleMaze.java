package za.co.wethinkcode.toyrobot.maze;


import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.Obstacle;
import za.co.wethinkcode.toyrobot.world.SquareObstacle;

import java.util.ArrayList;
import java.util.List;

public class SimpleMaze extends AbstractMaze {
    List<Obstacle> obstacleList = new ArrayList<>();

    public SimpleMaze() {
        generateMaze();
    }

    @Override
    public boolean blocksPath(Position a, Position b) {
        return false;
    }

    public List<Obstacle> generateMaze() {

        this.obstacleList.add(new SquareObstacle(1, 1));
        return this.obstacleList;
    }
    public List<Obstacle> getObstacles() {
        return this.obstacleList;
    }
    public void clearObstacles() { obstacleList.clear(); }
}
