/*Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader. */
import java.util.*;

class LeadersInArr {
    static ArrayList<Integer> getLeaders(int[] arr) {
        ArrayList<Integer> result = new ArrayList<>();
        int n = arr.length;
        int max_right = arr[n-1]; // max_right = 2
        result.add(max_right); 
        for (int i=n-2; i>=0; i--) { // i=3
            if (arr[i]>=max_right) { // 5<4
                max_right = arr[i];//max_right = 5
                result.add(max_right);
            }
        }
        Collections.reverse(result);
        return result;
    }
    public static void main(String[] args) {       
        int[] arr = {16, 17, 4, 3, 5, 2};
        ArrayList<Integer> result = getLeaders(arr);
        for (int x : result) {
            System.err.print(x + " ");
        }


        

    }
}
