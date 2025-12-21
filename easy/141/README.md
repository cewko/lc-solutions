# 141. Linked List Cycle



A cycle exists in a linked list when a node can be reached again by continuously following the next pointers. In other words, if you keep traversing the list by moving from one node to the next, and you eventually arrive at a node you've already visited, then the list has a cycle.

The problem uses an internal variable pos to denote which node the tail connects back to (creating the cycle), but this variable is not provided as input to your function. You only receive the head of the linked list.

Your function should return true if a cycle exists anywhere in the linked list, and false if the linked list has no cycle (meaning it eventually terminates with a node pointing to null).

**Example 1**

    Input: head = [3,2,0,-4], pos = 1
    Output: true