from linkedList import LinkedList
from linkedListSorting import reverse_list, merge_sort_list, merge_two_sorted_lists


def test_reverse_list():
    ll = LinkedList()
    ll.from_list([1, 2, 3, 4, 5])
    ll.head = reverse_list(ll.head)
    assert ll.to_list() == [5, 4, 3, 2, 1], "Error in reverse_list"


def test_merge_sort_list():
    ll = LinkedList()
    ll.from_list([4, 2, 1, 3])
    ll.head = merge_sort_list(ll.head)
    assert ll.to_list() == [1, 2, 3, 4], "Error in merge_sort_list"


def test_merge_two_sorted_lists():
    ll1 = LinkedList()
    ll1.from_list([1, 3, 5])
    ll2 = LinkedList()
    ll2.from_list([2, 4, 6])
    merged_head = merge_two_sorted_lists(ll1.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    assert merged_list.to_list() == [1, 2, 3, 4, 5, 6], "Error in merge_two_sorted_lists"


if __name__ == "__main__":
    test_reverse_list()
    test_merge_sort_list()
    test_merge_two_sorted_lists()
    print("All tests are passed!")
