'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        accum = 0
        idx = 0
        j = len(arr) -1
        for i, num in enumerate(arr):
            accum += (2 if num == 0 else 1)
            if(accum > j):
                idx = i;
                break

        flag = accum - j - 1;
        for i in range(idx,-1,-1):
            if flag:
                arr[j] = 0
                j -= 1
                flag = 0;
            else:
                if (arr[i]) != 0:
                    arr[j] = arr[i]
                    j -= 1
                else:
                    arr[j] = 0
                    arr[j -1] = 0
                    j -= 2