package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Play;
import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.Robot;
import za.co.wethinkcode.toyrobot.maze.Maze;

import java.util.List;
import java.util.ArrayList;

public class TextWorld extends AbstractWorld {

    private List<Obstacle> obstacleList = new ArrayList<>();

    public Maze maze;

    public TextWorld(Maze maze) {
        //IntelliJ told me to add this and it fixed the errors
        //I have no idea what it does
        super(maze);
        this.maze = maze;
    }
    @Override
    public void updateDirection(boolean right) {
    /**This function doesn't actually update the direction, it just calculates
    the new one and passes the index to the setDirection function
     @param right boolean for right (True) or left (False)
     @return index for the next enum
    */
        int index;
        if (!right) {
            //ordinal returns the index of an enum
            index = getCurrentDirection().ordinal() - 1;
            if (index < 0) {
                index = 3;
            }
        }
        else {
            index = getCurrentDirection().ordinal() + 1;
            if (index > 3) { index = 0; }
            }
        //This function actually updates the direction. Java is cool.
        setDirection(index);
    }

    public void moveRobot(Position oldPosition, Position newPosition) {
        /** This function does nothing in text world*/
    }


    public void generateObstacles(Maze maze) {
        /** Generates a random number of obstacles and stores them
          in the obstacleList list.*/

        this.obstacleList = maze.generateMaze();
        showObstacles();
    }

    @Override
    public List<Obstacle> getObstacles() {
        return obstacleList;
    }

    @Override
    public void showObstacles() {
        Play.printOutput("There are some obstacles:");
        for (Obstacle obst : obstacleList) {
            Play.printOutput("- At position " + obst.getBottomLeftX() +  "," + obst.getBottomLeftY()
            + " (to " + (obst.getBottomLeftX() + 4) + "," + (obst.getBottomLeftY() + 4) + ")");
        }
    }

    public void traverseMaze(ArrayList<ArrayList<Integer>> path) {
        for (ArrayList<Integer> point : path) {
            setPosition(point.get(0), point.get(1));
        }
    }

}

