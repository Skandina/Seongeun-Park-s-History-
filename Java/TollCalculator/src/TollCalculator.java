
public class TollCalculator {

    int[] IsItRushHour;
    
    public TollCalculator(Car car) {
       
        this.IsItRushHour = new int[car.GetArray().length];
        for (int o = 0; o < car.GetArray().length; o++) {
            this.IsItRushHour[o] =car.GetArray()[o];
        }  
    }

    public TollCalculator(Motorbike Motorbike) {
       
        this.IsItRushHour = new int[Motorbike.GetArray().length];
        for (int o = 0; o < Motorbike.GetArray().length; o++) {
            this.IsItRushHour[o] =Motorbike.GetArray()[o];
        }  
    }
    
    public int getTotalFee(int x){
        int totalFee = 0;
       
        for (int i = 0; i < IsItRushHour.length; i++) {

            if (IsItRushHour[i] >= 800 && IsItRushHour[i] <= 900) {
                totalFee += 18;
            System.out.println("Rush Hour : 18kr");

            } else if (IsItRushHour[i] >= 1600 && IsItRushHour[i] <= 1700) {
                totalFee += 18;
            System.out.println("Rush Hour : 18kr");

            } else {
                // x == 1 means it's car. 
                if (x == 1) {
                totalFee += 11;
                System.out.println("Normal Time : 11kr");
                } 

                // x == 2 means it's Motorbike. 
                if (x == 2) {
                totalFee += 8;
                System.out.println("Normal Time : 8kr");
                }
            }

            if (totalFee>60) {
                totalFee = 60; 
            }
        }
        return totalFee;
        
}

}
