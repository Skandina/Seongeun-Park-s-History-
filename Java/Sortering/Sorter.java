public class Sorter {

    public static int[] sort(int[] unsorted) {
        for(int i = 0; i < unsorted.length; i++) {
            for(int j=i+1; j<unsorted.length; j++) {
                if(unsorted[i] > unsorted[j]) {
                    int temp = unsorted[i]; 
                    unsorted[i]=unsorted[j]; 
                    unsorted[j]=temp;
                }
            }
        }

         return unsorted; 
    }
    
    public static void PrintSort(int[] unsorted){
        for (int i = 0; i < unsorted.length; i++) {
            System.out.print(unsorted[i]+" ");
        }
        System.out.println();
    }
}