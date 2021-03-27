package za.co.wethinkcode.toyrobot;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import za.co.wethinkcode.toyrobot.world.IWorld;
import za.co.wethinkcode.toyrobot.world.TextWorld;
import za.co.wethinkcode.toyrobot.maze.Maze;
import za.co.wethinkcode.toyrobot.maze.EmptyMaze;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

class RobotTest {

    private final PrintStream standardOut = System.out;
    private final InputStream standardIn = System.in;
    private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

    @BeforeEach
    public void setUp() {
        System.setOut(new PrintStream(outputStreamCaptor));
    }

    @AfterEach
    public void tearDown() {
        System.setOut(standardOut);
        System.setIn(standardIn);
    }

    @Test
    void initialPosition() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertEquals(world.CENTRE, world.getPosition());
        assertEquals(IWorld.Direction.UP, world.getCurrentDirection());
    }

    @Test
    void dump() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertEquals("[0,0] CrashTestDummy> Ready", robot.toString());
    }

    @Test
    void shutdown() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        ShutdownCommand command = new ShutdownCommand();
        assertFalse(robot.handleCommand(command));
    }

    @Test
    void forward() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        ForwardCommand command = new ForwardCommand("10");
        assertTrue(robot.handleCommand(command));
        Position expectedPosition = new Position(world.CENTRE.getX(), world.CENTRE.getY() + 10);
        assertEquals(expectedPosition, world.getPosition());
        assertEquals("Moved forward by 10 steps.", robot.getStatus());
    }

    @Test
    void forwardforward() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertTrue(robot.handleCommand(new ForwardCommand("10")));
        assertTrue(robot.handleCommand(new ForwardCommand("5")));
        assertEquals("Moved forward by 5 steps.", robot.getStatus());
    }

    @Test
    void tooFarForward() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertTrue(robot.handleCommand(new ForwardCommand("1000")));
        assertEquals(world.CENTRE, world.getPosition());
        assertEquals("Sorry, I cannot go outside my safe zone.", robot.getStatus());
    }

    @Test
    void left() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertTrue(robot.handleCommand(new LeftCommand()));
        assertEquals(IWorld.Direction.LEFT, world.getCurrentDirection());
    }
    @Test
    void leftleft() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertTrue(robot.handleCommand(new LeftCommand()));
        assertTrue(robot.handleCommand(new LeftCommand()));
        assertEquals(IWorld.Direction.DOWN, world.getCurrentDirection());
    }

    @Test
    void right() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertTrue(robot.handleCommand(new RightCommand()));
        assertEquals(IWorld.Direction.RIGHT, world.getCurrentDirection());
    }

    @Test
    void rightright() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertTrue(robot.handleCommand(new RightCommand()));
        assertTrue(robot.handleCommand(new RightCommand()));
        assertEquals(IWorld.Direction.DOWN, world.getCurrentDirection());
    }

    @Test
    void leftright() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        assertTrue(robot.handleCommand(new LeftCommand()));
        assertTrue(robot.handleCommand(new RightCommand()));
        assertEquals(IWorld.Direction.UP, world.getCurrentDirection());
    }

    @Test
    void help() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        Command command = new HelpCommand();
        assertTrue(robot.handleCommand(command));
        assertEquals("I can understand these commands:\n" +
                "OFF  - Shut down robot\n" +
                "HELP - provide information about commands\n" +
                "FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\n" +
                "SPRINT - move forward in descending values from a specified value\n" +
                "REPLAY - Replay all movement commands given to the robot\n" +
                "#REPLAY MUTATORS# - reversed, range (digit or digit-digit" +
                "MAZERUN - Solve the given maze, can solve to top, bottom, left, or right.", robot.getStatus());
    }
}