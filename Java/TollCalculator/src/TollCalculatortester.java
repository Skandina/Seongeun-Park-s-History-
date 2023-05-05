public class TollCalculatortester {

    public static void main(String[] args) {

        /* Giving its passing time for each vehicles.  */
        int[] arraycar1 = {930, 1000, 1510, 1650};
        int[] arraycar2 = {800, 1130, 1440, 1700, 1800};
        int[] arraycar3 = {1200, 1600};
        int[] arraybike1 = {1000, 1100, 1630, 1710, 1720, 1730};
        int[] arraybike2 = {1430}; 
        
        Car car1 = new Car(arraycar1);
        Car car2 = new Car(arraycar2);
        Car car3 = new Car(arraycar3);
        Motorbike motorbike1 = new Motorbike(arraybike1);
        Motorbike motorbike2 = new Motorbike(arraybike2); 

        TollCalculator totalfee1 = new TollCalculator(car1);
        car1.PrintDetail();
        System.out.println("Total fee is : " + totalfee1.getTotalFee(1) + "kr");
        System.out.println("");
        
        TollCalculator totalfee2 = new TollCalculator(car2);
        car2.PrintDetail();
        System.out.println("Total fee is : " + totalfee2.getTotalFee(1) + "kr");
        System.out.println("");
        
        TollCalculator totalfee3 = new TollCalculator(car3);
        car3.PrintDetail();
        System.out.println("Total fee is : " + totalfee3.getTotalFee(1) + "kr");
        System.out.println("");
        
        TollCalculator totalfee4 = new TollCalculator(motorbike1);
        motorbike1.PrintDetail();
        System.out.println("Total fee is : " + totalfee4.getTotalFee(2) + "kr");
        System.out.println("");
        
        TollCalculator totalfee5 = new TollCalculator(motorbike2);
        motorbike2.PrintDetail();
        System.out.println("Total fee is : " + totalfee5.getTotalFee(2) + "kr");
        System.out.println(""); 
        
        }

    
        
}
