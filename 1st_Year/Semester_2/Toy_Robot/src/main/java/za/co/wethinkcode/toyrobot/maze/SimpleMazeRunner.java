package za.co.wethinkcode.toyrobot.maze;

import za.co.wethinkcode.toyrobot.Position;
import za.co.wethinkcode.toyrobot.Robot;
import za.co.wethinkcode.toyrobot.world.IWorld;
import za.co.wethinkcode.toyrobot.world.Obstacle;

import java.util.*;

public class SimpleMazeRunner implements MazeRunner {

    private int cost = 0;
    public List<Obstacle> obstacleList = new ArrayList<>();
    IWorld world;
    int index = 1;
    ArrayList<Integer> exit = new ArrayList<>(2);
    String directionString;

    /**
     * Handles the collection of necessary data as well as solving the maze. I make use of a
     * Breadth First Search (BFS) algorithm
     * @param target the instance of Robot to use to run the maze
     * @param edgeDirection the edge to try and reach, one of Direction.UP, RIGHT, DOWN, or LEFT
     * @return boolean if mazerun was successful or not
     */
    public boolean mazeRun(Robot target, IWorld.Direction edgeDirection) {

        this.obstacleList = target.getWorld().getObstacles();
        checkArgs(edgeDirection);
        //All the variables used to solve the maze
        ArrayList<ArrayList<ArrayList<Integer>>> openCells = findOpenCells();
        Map<ArrayList<Integer>, ArrayList<ArrayList<Integer>>> connectedCells = connectOpenCells(openCells);
        Queue<ArrayList<ArrayList<Integer>>> queue = createQueue();
        ArrayList<ArrayList<Integer>> paths = new ArrayList<>();

        do {
            ArrayList<ArrayList<Integer>> currentPath;
            //Remove the first element of the queue and assign it to the current path
            currentPath = queue.poll();
            ArrayList<Integer> node;
            node = currentPath.get(currentPath.size() - 1);
            //Check if node hasn't been visited
            if (!paths.contains(node)) {
                ArrayList<ArrayList<Integer>> neighbours;
                //Get the list of points connected to that node
                neighbours = connectedCells.get(node);
                for (ArrayList neighbour : neighbours) {
                    ArrayList<ArrayList<Integer>> newPath = new ArrayList<>();
                    newPath.addAll(currentPath);
                    newPath.add(neighbour);
                    queue.add(newPath);
                    //Check if the connected point is the exit
                    if (neighbour.get(index).equals(exit.get(index))) {
                        world = target.getWorld();
                        world.traverseMaze(newPath);
                        target.setStatus("I am at the " + directionString + " edge. (Cost: " + newPath.size() + " steps)");
                        return true;
                    }
                }
                //Add the node to the list of checked paths
                paths.add(node);
            }
        }
        while (queue.size() > 0);

        target.setStatus("I am lost. (Cost: 0 steps)");
        return false;
    }

    /**
     * Set's the exit coordinate based on the edgeDirection parameter
     * @param edgeDirection The desired edge of the maze to be reached
     */
    private void checkArgs(IWorld.Direction edgeDirection) {

        switch (edgeDirection) {
            case RIGHT:
                exit.add(100);
                exit.add(0);
                directionString = "right";
                index = 0;
                break;
            case DOWN:
                exit.add(0);
                exit.add(-200);
                directionString = "bottom";
                break;
            case LEFT:
                exit.add(-100);
                exit.add(0);
                directionString = "left";
                index = 0;
                break;
            case UP:
            default:
                exit.add(0);
                exit.add(200);
                directionString = "top";
                break;
        }
    }

    /** Checks the entire maze in indices of 5 and checks where
     * all the unobstructed cells are.
     * @return openCells List of all the available locations
     */
    private ArrayList<ArrayList<ArrayList<Integer>>> findOpenCells() {

        //Trust me. I'm an engineer
        ArrayList<ArrayList<ArrayList<Integer>>> openCells = new ArrayList<>();
        ArrayList<ArrayList<Integer>> newList;
        //Start in the bottom left corner and move to the top right
        for (int y = -200; y < 201; y += 5) { //Iterate 5 points at a time to save time,
            for (int x = -100; x < 101; x += 5) { //can be set to 1 for more accurate results if needed
                if (!blocksPosition(new Position(x, y))) {
                    //Check if y is still less than 200 to ensure points out of bounds aren't considered.
                    if (y != 200 && !blocksPosition(new Position(x, y + 5))) { //Check the point 5 units up
                        newList = new ArrayList<>();
                        //Add checked point to the list
                        newList.add(addItemsToList(x, y));
                        //Add the point above it
                        newList.add(addItemsToList(x, y + 5));
                        openCells.add(newList);
                    }
                    //Repeat the above checks with the x-coordinate
                    if (x != 100 && !blocksPosition(new Position(x + 5, y))) {
                        newList = new ArrayList<>();
                        newList.add(addItemsToList(x, y));
                        newList.add(addItemsToList(x + 5, y));
                        openCells.add(newList);
                    }
                }
            }
        }
        return openCells;
    }

    /**
     * Takes the list of all available cells with their adjacent cells and connects them
     * using a hashmap where every possible position is a key and every possible position connected to
     * that point as the value.
     * @param openCells Is the list of all open cells with their adjacent cells
     * @return connectedCells Is a hashmap where every key is an open cell
     * with the value being it's adjacent cell
     */
    private Map connectOpenCells(ArrayList<ArrayList<ArrayList<Integer>>> openCells) {

        Map<ArrayList<Integer>, ArrayList<ArrayList<Integer>>> connectedCells = new HashMap<>();
        ArrayList<Integer> temp1;
        ArrayList<Integer> temp2;

        for (ArrayList<ArrayList<Integer>> openCell : openCells) {
            temp1 = openCell.get(0);
            temp2 = openCell.get(1);
            ArrayList<ArrayList<Integer>> tempList = new ArrayList<>();
            ArrayList<ArrayList<Integer>> mapValue;

            //check if the map already contains the key, if not then add it, else append
            //the value to the key. Java doesn't have defaultdicts which makes me sad.
            if (!connectedCells.containsKey(temp1)) {
                tempList.add(temp2);
                connectedCells.put(temp1, tempList);
                tempList = new ArrayList<>();
            }
            else {
                //Can't append to map value, get the value(list of coordinates) and append to it
                //before adding it back in
                mapValue = connectedCells.get(temp1);
                mapValue.add(temp2);
                connectedCells.put(temp1, mapValue);
            }
            //Do the same with the next value
            if (!connectedCells.containsKey(temp2)) {
                tempList.add(temp1);
                connectedCells.put(temp2, tempList);
            }
            else {
                mapValue = connectedCells.get(temp2);
                mapValue.add(temp1);
                connectedCells.put(temp2, mapValue);
            }
        }
        return connectedCells;
    }

    /** Creates an Arraylist of 2 points and returns it
     * @param x,y are the 2 points to be added to the list
     * @return output is the ArrayList containing the 2 points
     */
    public ArrayList<Integer> addItemsToList(int x, int y) {

        ArrayList<Integer> output = new ArrayList<>();
        output.add(x);
        output.add(y);
        return output;
    }

    /**
     * This is the most jank method I've ever created
     * @return queue An arraylist that holds an arraylist that holds an arraylist of integers
     */
    private Queue<ArrayList<ArrayList<Integer>>> createQueue() {

        Queue<ArrayList<ArrayList<Integer>>> queue = new LinkedList<>();
        ArrayList<ArrayList<Integer>> layer1 = new ArrayList<>();
        ArrayList<Integer> layer2 = new ArrayList<>();
        layer2.add(0);
        layer2.add(0);
        layer1.add(layer2);
        queue.add(layer1);

        return queue;
    }

    public boolean blocksPosition(Position position) {

        for (Obstacle obst : obstacleList) {
            if (position.getX() <= (obst.getBottomLeftX() + 4) && position.getX() >= obst.getBottomLeftX()) {
                if (position.getY() <= (obst.getBottomLeftY() + 4) && position.getY() >= obst.getBottomLeftY()) {
                    return true;
                }
            }
        }
        return false;
    }

    public int getMazeRunCost() { return this.cost; }

}
