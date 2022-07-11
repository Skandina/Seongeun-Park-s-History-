public class SortTest {
    public static void main(String[] args) {

        int[] test1 = {-1, -95, 49, 0, 18, 9};
        int[] test2 = {3, 80, -15, 27, -100};
        int[] test3 = {104, 0, -294, -153, -24};
        int[] test4 = {201, -491, 1000, 0, 500};
        int[] test5 = {5, 35, -34, 33, -31, 0};

        int[] final1 = Sorter.sort(test1);
        int[] final2 = Sorter.sort(test2);
        int[] final3 = Sorter.sort(test3);
        int[] final4 = Sorter.sort(test4);
        int[] final5 = Sorter.sort(test5);

        Sorter.PrintSort(final1);
        Sorter.PrintSort(final2);
        Sorter.PrintSort(final3);
        Sorter.PrintSort(final4);
        Sorter.PrintSort(final5);

    }
    
    

}
