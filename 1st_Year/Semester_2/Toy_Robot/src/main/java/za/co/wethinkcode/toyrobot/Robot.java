package za.co.wethinkcode.toyrobot;

import za.co.wethinkcode.toyrobot.world.IWorld;
import java.util.ArrayList;

public class Robot {

    public IWorld world;
    private String status;
    private String name;
    private ArrayList<String> commandsList = new ArrayList<>();

    public Robot(String name) {
        this.name = name;
        this.status = "Ready";
    }

    public String getStatus() {
        return this.status;
    }

    public boolean handleCommand(Command command) {
        return command.execute(this);
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getName() {
        return name;
    }

    public void setWorld(IWorld world) { this.world = world; }

    public IWorld getWorld() { return this.world; }

    public ArrayList getCommandList() { return this.commandsList; }

    public void addCommandList(String command) { this.commandsList.add(command); }

    @Override
    public String toString() {
       return "[" + this.world.getPosition().getX() + "," + this.world.getPosition().getY() + "] "
               + this.name + "> " + this.status;
    }

}