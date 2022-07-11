public class Motorbike implements Vehicle  {
    int[] IsItRushHour;

    public int getFee() {
        return 8;
    }
    
    public Motorbike (int[] IsItRushHour){
        this.IsItRushHour = IsItRushHour;
    }
    
    public int[] GetArray(){
        return this.IsItRushHour;
    }
    
    public void PrintDetail() {
        
        System.out.println("The fee for Motorbike is " + getFee()+" kr for Normal time, 18kr for Rush Hour");
        System.out.println("The maximum fee for one day is 60kr");
        System.out.println("Your Motorbike passed the road "+ IsItRushHour.length + " time(s) today");

    }


}
