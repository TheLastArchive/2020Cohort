package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.Obstacle;
import za.co.wethinkcode.toyrobot.world.SquareObstacle;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class RandomMaze extends AbstractMaze {

    List<Obstacle> obstacleList = new ArrayList<>();
    Random random = new Random();

    @Override
    public boolean blocksPath(Position a, Position b) {
        return false;
    }

    public List<Obstacle> generateMaze() {
        for (int i = 0; i < random.nextInt(11); i++) {
            int x = random.nextInt(201) - 100;
            int y = random.nextInt(401) - 200;
            obstacleList.add(new SquareObstacle(x, y));
        }
        return obstacleList;
    }

    public void clearObstacles() { obstacleList.clear(); }
}
