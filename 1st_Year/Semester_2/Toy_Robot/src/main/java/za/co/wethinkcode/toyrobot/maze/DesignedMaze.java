package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.world.Obstacle;
import za.co.wethinkcode.toyrobot.world.SquareObstacle;
import java.util.Random;
import java.util.ArrayList;
import java.util.List;

public class DesignedMaze extends AbstractMaze {

    Random random = new Random();
    public List<Obstacle> obstacleList = new ArrayList<>();

    public DesignedMaze() {
        generateMaze();
    }

    @Override
    public boolean blocksPath(Position a, Position b) {
        return false;
    }

    public List<Obstacle> generateMaze() {
        //TODO
        //Generates random obstacles for testing purposes

        for (int i = 0; i < 500; i++) {
            int x = random.nextInt(201) - 100;
            int y = random.nextInt(401) - 200;
            //Ensure that no obstacles are generated in a small area around the origin
            while ((x < 10 && x > -10) && (y < 10 && y > -10)) {
                x = random.nextInt(201) - 100;
                y = random.nextInt(401) - 200;
            }

            obstacleList.add(new SquareObstacle(x, y));
        }
        return obstacleList;
    }

    public List<Obstacle> getObstacles() { return this.obstacleList; }

    public void clearObstacles() { obstacleList.clear(); }
}

