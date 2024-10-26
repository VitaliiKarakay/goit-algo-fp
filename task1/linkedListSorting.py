class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sort_list(head):
    if not head or not head.next:
        return head

    def get_middle(node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(left, right):
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.value < right.value:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

    middle = get_middle(head)
    right_head = middle.next
    middle.next = None
    left = merge_sort_list(head)
    right = merge_sort_list(right_head)
    return merge(left, right)


def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next
