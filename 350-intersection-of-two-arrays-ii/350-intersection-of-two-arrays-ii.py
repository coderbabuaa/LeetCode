class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
                cnt1 = Counter(nums1)
                cnt2 = Counter(nums2)
                ans = []
                for i in cnt1:
                    if i in cnt2:
                        ans += [i for x in range(min(cnt1[i], cnt2[i]))]
                return ans