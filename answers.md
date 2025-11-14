# CMPS 2200 Recitation 08

## Answers

**Name:**Justin Green


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
Each edge gets pushed and each vertex gets popped. The cost of a heap push or pop is O(log n). If e = number of edges and v = number of vertices, then our work is O((v + e)log n).

For our span, our heap operations are sequential but our edge relaxations in each pop can be done in parallel. However, the algorithm is sequential because each heap pop depends on the previous. This means that our span depends on the number of heap pops we complete in order to find the shortest path. As established, each heap push or pop costs O(log n) time so our span is going to O(n log n) for n heap pops.


- **2b)**
I'm not exactly sure what I am supposed to be typing for this because there isn't a question for 2b, put rather code implentation of get_path in main. When I run the test function, it returns sbc. In my algorithm, each vertex is enqueued and dequeued at most once and each edge is examined once. This gives us work of O(v + e) where v = number of vertices and e = number of edges. The span is O(L) where L is the length of the longest shortest-path distance because each level of the BFS can be done in parallel since all nodes at the same distance discover their neighbors independently. Each layer has a constant cost because the same operations are being completed as we go through each level of the BFS. Therefore, our total span depends on the number of levels we must traverse finding the longest shortest path.
