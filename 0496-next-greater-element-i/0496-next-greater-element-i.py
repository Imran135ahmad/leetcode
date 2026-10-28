class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st=[]
        ng={}
        for n in nums2:
            while st and st[-1]<n:
                ng[st.pop()]=n
            st.append(n)
        res=[]
        for i in nums1:
            res.append(ng.get(i,-1))
        return res