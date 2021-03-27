package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.Robot;
import za.co.wethinkcode.toyrobot.maze.Maze;

import java.util.ArrayList;
import java.util.List;

/**
 * Your Text and Turtle worlds must implement this interface.
 */
public interface IWorld {

    /**
     * Enum used to track direction
     */
    enum Direction {
        //Why change the direction names?????????
        UP,
        RIGHT,
        DOWN,
        LEFT
    }

    /**
     * Enum that indicates response for updatePosition request
     */
    enum UpdateResponse {
        SUCCESS, //position was updated successfully
        FAILED_OUTSIDE_WORLD, //robot will go outside world limits if allowed, so it failed to update the position
        FAILED_OBSTRUCTED, //robot obstructed by at least one obstacle, thus cannot proceed.
    }

    Position CENTRE = new Position(0,0);

    /**
     * Updates the position of your robot in the world by moving the nrSteps in the robots current direction.
     * @param nrSteps steps to move in current direction
     * @return true if this does not take the robot over the world's limits, or into an obstacle.
     */
    UpdateResponse updatePosition(int nrSteps);

    /**
     * Updates the current direction your robot is facing in the world by cycling through the directions UP, RIGHT, BOTTOM, LEFT.
     * @param turnRight if true, then turn 90 degrees to the right, else turn left.
     */
    void updateDirection(boolean turnRight);

    /**
     * Retrieves the current position of the robot
     */
    Position getPosition();

    /**
     * Gets the current direction the robot is facing in relation to a world edge.
     * @return Direction.UP, RIGHT, DOWN, or LEFT
     */
    Direction getCurrentDirection();

    /**
     * Checks if the new position will be allowed, i.e. falls within the constraints of the world, and does not overlap an obstacle.
     * @param position the position to check
     * @return true if it is allowed, else false
     */
    boolean isNewPositionAllowed(Position position);

    /**
     * Checks if the robot is at one of the edges of the world
     * @return true if the robot's current is on one of the 4 edges of the world
     */
    boolean isAtEdge();

    /**
     * Reset the world by:
     * - moving current robot position to center 0,0 coordinate
     * - removing all obstacles
     * - setting current direction to UP
     */
    void reset();

    /**
     * @return the list of obstacles, or an empty list if no obstacles exist.
     */
    List<Obstacle> getObstacles();

    /**
     * Gives opportunity to world to draw or list obstacles.
     */
    void showObstacles();

    /**
     * generates obstacles
     */
    void generateObstacles(Maze maze);

    /**
     * Moves the turtle, does nothing for text world
     * @param oldPosition the old position of the robot
     * @param newPosition the new position of the robot.
     */
    void moveRobot(Position oldPosition, Position newPosition);

    /**
     * takes the shortest path solved by mazerun and moves the robot along it
     * @param newPath List of coordinates of the shortest path in increments of 5
     */
    void traverseMaze(ArrayList<ArrayList<Integer>> newPath);
}
