# Time complexity O(nlogn)
# Space complexity O(n)

def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        if not head:
            return 
        while head is not None:
            arr.append(head.val)
            head = head.next

        dummy_node = ListNode(0)
        curr = dummy_node

        for i in sorted(arr):
            curr.next = ListNode(i)
            curr = curr.next
        return dummy_node.next