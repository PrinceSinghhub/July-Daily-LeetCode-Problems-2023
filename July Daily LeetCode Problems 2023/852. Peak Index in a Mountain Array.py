class Solution:
    def peakIndexInMountainArray(self, arr):

        start = 0
        end = len(arr) - 1

        while start < end:

            mid = start + (end - start) // 2

            if (arr[mid] > arr[mid + 1]):
                end = mid

            if (arr[mid] < arr[mid + 1]):
                start = mid + 1

        return start  # also return end point becouse start and end are at same point