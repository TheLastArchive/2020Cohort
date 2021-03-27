package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.world.Obstacle;
import java.util.List;
import java.util.ArrayList;

public abstract class AbstractMaze implements Maze {
    List<Obstacle> obstacleList = new ArrayList<>();

    public AbstractMaze() {

    }

    public void selectMaze(String arg) {

        Maze maze = new RandomMaze();

        switch (arg) {
            case "EmptyMaze":
                maze = new EmptyMaze();
                this.obstacleList = maze.generateMaze();
                break;
            case "SimpleMaze":
                maze = new SimpleMaze();
                this.obstacleList = maze.generateMaze();
                break;
            case "DesignedMaze":
                maze = new DesignedMaze();
                this.obstacleList = maze.generateMaze();
                break;
            case "RandomMaze":
            default:
                this.obstacleList = maze.generateMaze();
        }
    }

    public List<Obstacle> getObstacles() { return this.obstacleList; }

//    public boolean blocksPath(Position a, Position b) {
//        if ((a.getX() < this.x && this.x < b.getX()) || (a.getX() >= this.x && this.x >= b.getX())) {
//            if (b.getY() <= (this.y + 4) && b.getY() >= this.y) {
//                return false;
//            }
//        }
//        if ((a.getY() <= this.y && this.y <= b.getY()) || (a.getY() >= this.y && this.y >= b.getY())) {
//            if (b.getX() <= (this.x + 4) && b.getX() >= this.x) {
//                return false;
//            }
//        }
//        return true;
//    }
}
