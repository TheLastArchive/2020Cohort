package za.co.wethinkcode.toyrobot;

import java.util.ArrayList;
import java.util.regex.*;
import java.util.Collections;
import java.util.List;

public class ReplayCommand extends Command{

    public static boolean replayInProgress = false;
    int startingIndex;
    int endingIndex;
    int commandCount;
    ArrayList<String> tempCommandList;
    List<String> executeCommandList;
    boolean reverse = false;

    public ReplayCommand(String arguments) {
        super("replay", arguments);
    }

    @Override
    public boolean execute(Robot target) {

        if (!checkArgs(target)) { return true; }

        executeCommandList = tempCommandList.subList(startingIndex, endingIndex);
        if (reverse) { Collections.reverse(executeCommandList);}

        replayInProgress = true;
        int i = 0;
        for (String command : executeCommandList ) {
            Command replayCommand = Command.create(command);
            target.handleCommand(replayCommand);
            if (i != (executeCommandList.size() - 1)) {
                Play.printStatus(target);
            }
            i++;
            commandCount++;
        }
        Play.printStatus(target);
        target.setStatus("replayed " + commandCount + " commands.");
        replayInProgress = false;
        return true;
    }

    private boolean checkArgs(Robot robot) {

        //remove commas and closing square brackets since they get left in the string.
        String [] argList = getArgument().replaceAll("[\\],]", "")
                .toLowerCase().trim().split(" ");
        tempCommandList = robot.getCommandList();
        startingIndex = 0;
        endingIndex = tempCommandList.size();

        for (int i = 1; i < argList.length; i++) {
            if (argList[i].equals("reversed")) {
                reverse = true;
            }
            else if (checkRange(argList[i])) {
                startingIndex = tempCommandList.size() - (Integer.parseInt(argList[i]));
                endingIndex = tempCommandList.size();
            }
            else if (checkRangeDouble(argList[i])) {
                String[] indexes = argList[i].split("-");
                //Check if input is invalid i.e 'replay 2-4'
                if (Integer.parseInt(indexes[0]) < Integer.parseInt(indexes[1])) {
                    robot.setStatus("Invalid range");
                    return false;
                }
                startingIndex = tempCommandList.size() - Integer.parseInt(indexes[0]);
                endingIndex = tempCommandList.size() - Integer.parseInt(indexes[1]);
            }
            else {
                robot.setStatus("Invalid argument");
                return false;
            }
        }

        return true;
    }

    private boolean checkRange(String arg) {
        //Checks if arg is a digit (number up to 2 digits long)
        Pattern pattern = Pattern.compile("\\d{1,2}");
        Matcher matcher = pattern.matcher(arg);
        return matcher.matches();
    }

    private boolean checkRangeDouble(String arg) {
        //Check for the pattern digit-digit (number up to 2 digits long)
        Pattern pattern = Pattern.compile("\\d{1,2}-\\d{1,2}");
        Matcher matcher = pattern.matcher(arg);
        return matcher.matches();
    }
}
