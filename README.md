# algorithms
practicing algorithms

from  Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges 
https://www.youtube.com/watch?v=oBt53YbR9Kk

    O(1) - Constant Time: The algorithm's performance does not depend on the input size. It has a fixed execution time regardless of how large the input is.

    O(log n) - Logarithmic Time: The algorithm's runtime grows at most logarithmically with the input size. Algorithms with this complexity often divide the input into smaller portions in each step, like binary search.

    O(n) - Linear Time: The algorithm's performance scales linearly with the input size. If the input size doubles, the algorithm's runtime will roughly double as well.

    O(n log n) - Linearithmic Time: The algorithm's runtime grows slightly faster than linear but is still more efficient than quadratic or cubic algorithms. Many efficient sorting algorithms, such as merge sort and quicksort, fall into this category.

    O(n^2) - Quadratic Time: The algorithm's runtime grows quadratically with the input size. If the input size doubles, the algorithm's runtime will roughly quadruple.

    O(n^3) - Cubic Time: The algorithm's runtime grows cubically with the input size. This is less efficient than quadratic time and typically seen in algorithms with nested loops.

    O(2^n) - Exponential Time: The algorithm's runtime grows exponentially with the input size. Algorithms with this complexity are highly inefficient for large inputs.

    O(n!) - Factorial Time: The algorithm's runtime grows factorial with the input size, making it extremely inefficient for even moderately large inputs.

Fundamental Concepts:

    Arrays: Arrays are collections of elements, each identified by an index or a key. They have constant-time access to elements by index, but inserting or deleting elements in the middle can be time-consuming.

    Linked Lists: Linked lists consist of nodes where each node contains data and a reference (or link) to the next node. They are efficient for insertions and deletions but have slower random access.

    Stacks: Stacks are linear data structures with a Last-In-First-Out (LIFO) order. Common operations include push (adding an element) and pop (removing the top element).

    Queues: Queues are linear data structures with a First-In-First-Out (FIFO) order. Common operations include enqueue (adding an element) and dequeue (removing the front element).

    Trees: Trees are hierarchical data structures with a root node and child nodes. Common types include binary trees (each node has at most two children) and binary search trees (BSTs) that maintain a sorted order.

    Graphs: Graphs consist of nodes (vertices) and edges connecting them. They can be directed (edges have a direction) or undirected (edges have no direction). Graph algorithms like breadth-first search (BFS) and depth-first search (DFS) are used to traverse and analyze graphs.

    Hash Tables: Hash tables (or hash maps) are data structures that store key-value pairs. They provide constant-time average-case access to values based on their keys. Hashing functions are used to map keys to specific locations in the table.

Common Algorithms:

    Sorting Algorithms:
        Quicksort: A divide-and-conquer algorithm that recursively partitions the array into smaller segments and sorts them.
        Mergesort: Another divide-and-conquer algorithm that divides the array into smaller segments, sorts them, and then merges them together.

    Searching Algorithms:
        Binary Search: An efficient algorithm for finding a specific element in a sorted array by repeatedly dividing the search space in half.

    Graph Algorithms:
        Breadth-First Search (BFS): A traversal algorithm that explores all nodes at the current depth level before moving to the next level. It's used for finding shortest paths and exploring nearby nodes.
        Depth-First Search (DFS): A traversal algorithm that explores as far as possible along a branch before backtracking. It's used for topological sorting, cycle detection, and more.

Time and Space Complexity Analysis:

    Big O Notation: Big O notation is used to describe the upper bound (worst-case) of an algorithm's time or space complexity in terms of the input size (n). Common complexities include O(1) (constant time), O(log n) (logarithmic time), O(n) (linear time), O(n log n) (linearithmic time), O(n^2) (quadratic time), and more.

    Best-Case, Average-Case, Worst-Case: These scenarios help analyze how an algorithm performs under different input conditions:
        Best Case: The minimum possible time or space complexity for a particular input.
        Average Case: The expected time or space complexity over a range of inputs.
        Worst Case: The maximum possible time or space complexity for a particular input.