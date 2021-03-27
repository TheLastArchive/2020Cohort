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

class CommandTest {

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
    void getShutdownName() {
        Command test = new ShutdownCommand();
        assertEquals("off", test.getName());
    }

    @Test
    void getRightName() {
        Command test = new RightCommand();
        assertEquals("right", test.getName());
    }

    @Test
    void executeRight() {

        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        Command right = Command.create("right");
        assertTrue(right.execute(robot));
        assertEquals("Turned right.", robot.getStatus());
    }

    @Test
    void getLeftName() {
        Command test = new LeftCommand();
        assertEquals("left", test.getName());
    }

    @Test
    void executeLeft() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        Command left = Command.create("left");
        assertTrue(left.execute(robot));
        assertEquals("Turned left.", robot.getStatus());
    }

    @Test
    void executeShutdown() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        Command shutdown = Command.create("shutdown");
        assertFalse(shutdown.execute(robot));
        assertEquals("Shutting down...", robot.getStatus());
    }

    @Test
    void getForwardName() {
        Command test = new ForwardCommand("100");
        assertEquals("forward", test.getName());
        assertEquals("100", test.getArgument());
    }

    @Test
     void executeForward() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        Command forward100 = Command.create("forward 10");
        assertTrue(forward100.execute(robot));
        Position expectedPosition = new Position(world.CENTRE.getX(), world.CENTRE.getY() + 10);
        assertEquals(expectedPosition, world.getPosition());
        assertEquals("Moved forward by 10 steps.", robot.getStatus());
    }

    @Test
    void getHelpName() {
        Command test = new HelpCommand();                                                               //<1>
        assertEquals("help", test.getName());
    }

    @Test
    void executeHelp() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        Command help = Command.create("help");
        assertTrue(help.execute(robot));
        assertEquals("I can understand these commands:\n" +
                "OFF  - Shut down robot\n" +
                "HELP - provide information about commands\n" +
                "FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\n" +
                "SPRINT - move forward in descending values from a specified value\n" +
                "REPLAY - Replay all movement commands given to the robot\n" +
                "#REPLAY MUTATORS# - reversed, range (digit or digit-digit" +
                "MAZERUN - Solve the given maze, can solve to top, bottom, left, or right.", robot.getStatus());
    }

    @Test
    void getSprintName() {
        Command test = new SprintCommand("5");
        assertEquals("sprint", test.getName());
        assertEquals("5", test.getArgument());
    }

    @Test
    void executeSprint() {
        Robot robot = new Robot("CrashTestDummy");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        Command sprint5 = Command.create("sprint 5");
        assertTrue(sprint5.execute(robot));
        Position expectedPosition = new Position(world.CENTRE.getX(), world.CENTRE.getY() + 15);
        assertEquals(expectedPosition, world.getPosition());
        assertEquals("Moved forward by 1 steps.", robot.getStatus());
    }

    @Test
    void createCommand() {
        Command forward = Command.create("forward 10");                                                 //<1>
        assertEquals("forward", forward.getName());
        assertEquals("10", forward.getArgument());

        Command shutdown = Command.create("shutdown");                                                  //<2>
        assertEquals("off", shutdown.getName());

        Command help = Command.create("help");                                                          //<3>
        assertEquals("help", help.getName());
    }

    @Test
    void getReplayName() {
        Command command = new ReplayCommand("Replay");
        assertEquals("replay", command.getName());

    }
    @Test
    void getReplayNameWithArg() {
        Command command = new ReplayCommand("replay reversed");
        assertEquals("replay", command.getName());
        assertEquals("replay reversed", command.getArgument());
    }

    @Test
    void executeReplay() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        robot.addCommandList("forward 1");
        robot.addCommandList("forward 2");
        robot.addCommandList("forward 3");
        Command replay = Command.create("replay");
        assertTrue(replay.execute(robot));
        Position expectedPosition = new Position(world.CENTRE.getX(), world.CENTRE.getY() + 6);
        assertEquals(expectedPosition, world.getPosition());
        assertEquals("replayed 3 commands.", robot.getStatus());
    }

    @Test
    void executeReplayReversed() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        robot.addCommandList("forward 1");
        robot.addCommandList("forward 2");
        robot.addCommandList("forward 3");
        Command replay = Command.create("replay Reversed");
        assertTrue(replay.execute(robot));
        Position expectedPosition = new Position(world.CENTRE.getX(), world.CENTRE.getY() + 6);
        assertEquals(expectedPosition, world.getPosition());
        assertEquals("replayed 3 commands.", robot.getStatus());
    }

    @Test
    void executeReplayRange() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        robot.addCommandList("forward 1");
        robot.addCommandList("forward 2");
        robot.addCommandList("forward 3");
        robot.addCommandList("forward 4");
        robot.addCommandList("forward 5");
        Command replay = Command.create("replay 4");
        assertTrue(replay.execute(robot));
        Position expectedPosition = new Position(world.CENTRE.getX(), world.CENTRE.getY() + 14);
        assertEquals(expectedPosition, world.getPosition());
        assertEquals("replayed 4 commands.", robot.getStatus());
    }

    @Test
    void executeReplayMultiRange() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        robot.addCommandList("forward 1");
        robot.addCommandList("forward 2");
        robot.addCommandList("forward 3");
        robot.addCommandList("forward 4");
        robot.addCommandList("forward 5");
        Command replay = Command.create("replay 4-2");
        assertTrue(replay.execute(robot));
        Position expectedPosition = new Position(world.CENTRE.getX(), world.CENTRE.getY() + 5);
        assertEquals(expectedPosition, world.getPosition());
        assertEquals("replayed 2 commands.", robot.getStatus());
    }

    @Test
    void executeReplayInvalidRange() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        robot.addCommandList("forward 1");
        robot.addCommandList("forward 2");
        robot.addCommandList("forward 3");
        robot.addCommandList("forward 4");
        robot.addCommandList("forward 5");
        Command replay = Command.create("replay 2-4");
        assertTrue(replay.execute(robot));
        assertEquals("Invalid range", robot.getStatus());
    }

    @Test
    void executeReplayInvalidArg() {
        Robot robot = new Robot("Jeff");
        Maze maze = new EmptyMaze();
        IWorld world = new TextWorld(maze);
        robot.setWorld(world);
        robot.addCommandList("forward 1");
        robot.addCommandList("forward 2");
        robot.addCommandList("forward 3");
        robot.addCommandList("forward 4");
        robot.addCommandList("forward 5");
        Command replay = Command.create("replay reversed jeff 3-1");
        assertTrue(replay.execute(robot));
        assertEquals("Invalid argument", robot.getStatus());
    }

    @Test
    void createInvalidCommand() {
        try {
            Command forward = Command.create("say hello");                                              //<4>
            fail("Should have thrown an exception");                                                    //<5>
        } catch (IllegalArgumentException e) {
            assertEquals("Unsupported command: say hello", e.getMessage());                             //<6>
        }
    }
}
