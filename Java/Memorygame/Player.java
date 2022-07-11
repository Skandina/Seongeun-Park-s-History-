public class Player {
    
    private String name;
    private int score;
    private boolean myTurn; // active or inactive 

    public Player(String name, boolean myTurn) {
        this.name = name;
        this.myTurn = myTurn;
        this.score = 0;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void resetScore() {
        this.score = 0;
    }
    public int addScore() {
        return this.score++;
    }

    public void setMyTurn(boolean myTurn) {
        this.myTurn = myTurn;
    }
    
    
    public String getName() {
        return this.name;
    }

    public int getScore() {
        return this.score;
    }

    public boolean isMyTurn() {
        return this.myTurn;
    }

    public boolean No() {
        return this.myTurn = false;
    }

    public boolean Yes() {
        return this.myTurn = true;
    }
}