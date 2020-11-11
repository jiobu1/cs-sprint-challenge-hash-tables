1.  Hashing Functions
* Takes an input string and returns an index/number
* Deterministic - same input should always result in the same output
* Minimal duplication - to minimize collisions
* Fast - getting the hash must be O(1)

- hash tables use hash functions to get/store/delete values in O(1)time

2. Collision resolution
* Via chaining
* To solve collisions, chain values together by using linked lists
* If value already exists, add a new item/node to the linked list


3. Performance of a basic hash table operations
* O(1) - unless there are lots of collisions and then it will be an O(n) depending on the number of hash table entries

4. Load factor
* Load factor determines when to expand/shrink a table
* load factor = num elements/ num slots

5. Automatic resizing
* create functions that expands or shrinks the table based on the load size

6. Various use cases for hash tables
* We need to look up  some data quickly
* Some data that was slow to generate or obtain

* In lieu of linear search...
* It doesn't matter if _n_ is small. O(n) vs O(1)

**Any time-consuming process:**
* Memoization (caching)
* Network caching
* Indexing
* Removing duplicates from lists
* Detecting duplicates
* Counting duplicates
