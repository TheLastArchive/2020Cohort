package za.co.wethinkcode.toyrobot.world;

import org.turtle.StdDraw;
import org.turtle.Turtle;
import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.maze.Maze;
import java.awt.*;
import java.util.List;
import java.util.ArrayList;


public class TurtleWorld extends AbstractWorld {

    List<Obstacle> obstacleList = new ArrayList<>();
    Turtle turtle = new Turtle(0.0, 0.0, 90);
    Maze maze;

    public TurtleWorld(Maze maze) {
        super(maze);
        this.maze = maze;
    }

    @Override
    public void updateDirection(boolean turnRight) {
        int index;
        if (!turnRight) {
            //ordinal returns the index of an enum
            index = getCurrentDirection().ordinal() - 1;
            if (index < 0) {
                index = 3;
            }
            turtle.left(90);
        }
        else {
            index = getCurrentDirection().ordinal() + 1;
            if (index > 3) { index = 0; }
            turtle.right(90);
        }
        //This function actually updates the direction. Java is cool.
        setDirection(index);
    }

    /**
     * Moves the turtle along the canvas and uses StdDraw.line to visualise the path
     * @param oldPosition the old position of the robot
     * @param newPosition the new position of the robot.
     */
    public void moveRobot(Position oldPosition, Position newPosition) {
        turtle.setColor(Color.red);
        StdDraw.line(oldPosition.getX(), oldPosition.getY(), newPosition.getX(), newPosition.getY());
        turtle.setPosition(newPosition.getX(), newPosition.getY());
        turtle.forward(0);
    }

    /**
     * Generates a random number of obstacles and stores them
     * in the obstacleList list.
     * @param maze The maze object where the obstacleList will be stored
     */
    public void generateObstacles(Maze maze) {

        this.maze = maze;
        this.obstacleList = maze.generateMaze();
        showObstacles();
    }

    @Override
    public List<Obstacle> getObstacles() { return obstacleList; }

    /**
     * Uses the StdDraw to display all the obstacles as well
     * as setting up the canvas and borders.
     */
    @Override
    public void showObstacles() {
        StdDraw.setXscale(-210, 210);
        StdDraw.setYscale(-210, 210);
        StdDraw.setPenColor(Color.black);
        StdDraw.rectangle(0, 0, 100, 200);
        StdDraw.setPenColor(Color.red);

        for (Obstacle obst : obstacleList) {
            StdDraw.filledSquare(obst.getBottomLeftX(), obst.getBottomLeftY(), 2);
        }
        turtle.setSize(0.01);
    }

    /**
     * Uses the shortest path given by mazerun and moves the turtle along
     * the path
     * @param path shortest path found by mazerun
     */
    public void traverseMaze(ArrayList<ArrayList<Integer>> path) {

        //Store the previous point since StdDraw.line requires an initial and final position
        ArrayList<Integer> previousPoint = new ArrayList<>(2);
        //Initialise the point as the origin
        previousPoint.add(0);
        previousPoint.add(0);

        for (ArrayList<Integer> point : path) {
            setPosition(point.get(0), point.get(1));
            StdDraw.line(previousPoint.get(0), previousPoint.get(1), point.get(0), point.get(1));
            turtle.setPosition(point.get(0), point.get(1));
            turtle.forward(0);
            previousPoint.clear();
            previousPoint.add(point.get(0));
            previousPoint.add((point.get(1)));
        }
    }
}
