package za.co.wethinkcode.toyrobot.world;

import za.co.wethinkcode.toyrobot.Position;

public class SquareObstacle implements Obstacle {

    int x;
    int y;

    public SquareObstacle(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int getBottomLeftX() {
        return this.x;
    }

    @Override
    public int getBottomLeftY() {
        return this.y;
    }

    @Override
    public int getSize() {
        return 5;
    }

    @Override
    public boolean blocksPosition(Position position) {

        if (position.getX() <= (this.x + 4) && position.getX() >= this.x) {
            if (position.getY() <= (this.y + 4) && position.getY() >= this.y) {
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean blocksPath(Position a, Position b) {
        if ((a.getX() < this.x && this.x < b.getX()) || (a.getX() >= this.x && this.x >= b.getX())) {
            if (b.getY() <= (this.y + 4) && b.getY() >= this.y) {
                return true;
            }
        }
        if ((a.getY() <= this.y && this.y <= b.getY()) || (a.getY() >= this.y && this.y >= b.getY())) {
            if (b.getX() <= (this.x + 4) && b.getX() >= this.x) {
                return true;
            }
        }
        return false;
    }
}
