/*Given an array arr[], the task is to print every alternate element of the array starting
 from the first element.
 nput: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12
 */

import java.util.*;

class AltElement {
    static ArrayList<Integer> getAlternates(int[] arr) {
        ArrayList<Integer> result = new ArrayList<>();

        //Iterating over all the elements
        for (int i=0; i<arr.length; i+=2) {
            result.add(arr[i]);
        }
        return result;
    }
    public static void main(String[] args) {
        int[] arr = {-5, 1, 4, 2, 12};
        ArrayList<Integer> res = getAlternates(arr);
        
        //printing the output:
        for (int x : res) {
            System.out.print(x + " ");
        }
    }
}
