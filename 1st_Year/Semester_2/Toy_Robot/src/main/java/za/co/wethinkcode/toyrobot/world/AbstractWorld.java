package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.maze.Maze;

public abstract class AbstractWorld implements IWorld {

    private final Position TOP_LEFT = new Position(-100,200);
    private final Position BOTTOM_RIGHT = new Position(100,-200);
    private Position position;
    private Direction currentDirection;
    public static final Position CENTRE = new Position(0,0);
    Maze maze;

    public AbstractWorld(Maze maze) {
        this.maze = maze;
        this.position = CENTRE;
        this.currentDirection = Direction.UP;
    }

    public Position getPosition() {
        return this.position;
    }

    public Direction getCurrentDirection() {
        return this.currentDirection;
    }

    public UpdateResponse updatePosition(int nrSteps) {
        int newX = this.position.getX();
        int newY = this.position.getY();

        switch (this.currentDirection) {
            case UP:
                newY += nrSteps;
                break;
            case DOWN:
                newY -= nrSteps;
                break;
            case RIGHT:
                newX += nrSteps;
                break;
            case LEFT:
                newX -= nrSteps;
                break;
        }

        Position newPosition = new Position(newX, newY);
        if (!isNewPositionAllowed(newPosition)) {
            if (newPosition.isIn(TOP_LEFT, BOTTOM_RIGHT)) {
                return UpdateResponse.FAILED_OBSTRUCTED;
            } else {
                return UpdateResponse.FAILED_OUTSIDE_WORLD;
            }
        }
        else {
            moveRobot(this.position, newPosition);
            this.position = newPosition;
            return UpdateResponse.SUCCESS;
        }

    }
                                          //values() allows me to change the enum by index
    public void setDirection(int index) { this.currentDirection = Direction.values()[index]; }


    public boolean isNewPositionAllowed(Position position) {

        if (!position.isIn(TOP_LEFT,BOTTOM_RIGHT)) { return false; }
        for (Obstacle obst : getObstacles()) {
            if (obst.blocksPosition(position) || obst.blocksPath(this.position, position)) { return false; }
        }

        return true;
    }

    public void setPosition(int x, int y) { this.position = new Position(x, y); }

    public boolean isAtEdge() {

        return (this.position.getY() == 200 ||
            this.position.getY() == -200 ||
            this.position.getX() == 100 ||
            this.position.getX() == -100);
    }

    public void reset() {

        maze.clearObstacles();
        this.position = new Position(0, 0);
        setDirection(0);

    }
}