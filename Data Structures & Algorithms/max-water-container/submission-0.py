class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=-1

        while l<r:
            width=r-l
            height = min(heights[l], heights[r])
            if max_area<(height*width):
                max_area=height*width
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return max_area