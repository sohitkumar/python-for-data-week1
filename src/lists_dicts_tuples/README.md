# Lists, Dicts, Tuples — Problems

## 1) Remove Duplicates (Preserve Order)
- Input: [1, 2, 2, 3, 1, 4]
- Expected Output: [1, 2, 3, 4]

## 2) Count Word Occurrences
- Input: ["a", "b", "a", "c", "b", "a"]
- Expected Output: {"a": 3, "b": 2, "c": 1}

## 3) Sort Dicts by Age then Name
- Input: [{"name":"Bob","age":30},{"name":"Alice","age":30},{"name":"Raj","age":25}]
- Expected Output: [{"name":"Raj","age":25},{"name":"Alice","age":30},{"name":"Bob","age":30}]

## 4) Extract Even Numbers
- Input: [1, 2, 3, 4, 5, 6]
- Expected Output: [2, 4, 6]

## 5) Tuples to Dict
- Input: [("a",1),("b",2)]
- Expected Output: {"a":1,"b":2}

---

## More Practice Problems

### 6) Unique Elements (Preserve Order)
- Input: ["a", "b", "a", "c", "b"]
- Expected Output: ["a", "b", "c"]

### 7) Top-K Frequent Elements
- Input: list = [1,1,2,3,3,3,4], k = 2
- Expected Output: [3, 1]

### 8) Group by Key (Dicts)
- Input: [{"name":"Ann","dept":"HR"},{"name":"Bob","dept":"IT"},{"name":"Cara","dept":"HR"}]
- Expected Output: {"HR":[{"name":"Ann","dept":"HR"},{"name":"Cara","dept":"HR"}], "IT":[{"name":"Bob","dept":"IT"}]}

### 9) Flatten Nested Lists (Deep)
- Input: [[1,2],[3,[4, [5]]]]
- Expected Output: [1,2,3,4,5]

### 10) Merge Dicts with Sum
- Input: {"a":1,"b":2} and {"b":3,"c":4}
- Expected Output: {"a":1,"b":5,"c":4}

### 11) Invert Dict (Handle Collisions)
- Input: {"a":1,"b":1,"c":2}
- Expected Output: {1:["a","b"], 2:["c"]}

### 12) Filter Tuples by Score
- Input: [("Ann",85),("Bob",72),("Cara",90)], threshold = 80
- Expected Output: ["Ann","Cara"]

### 13) Stable Multi-Key Sort
- Input: [{"name":"Bob","age":30},{"name":"Alice","age":30},{"name":"Raj","age":25}]
- Expected Output: sort by age asc, then name asc

### 14) Deduplicate List of Dicts by Key
- Input: [{"id":1,"n":"A"},{"id":1,"n":"A2"},{"id":2,"n":"B"}]
- Expected Output: [{"id":1,"n":"A"},{"id":2,"n":"B"}] (keep first occurrence by `id`)

### 15) Zip Lists to Dict of Lists
- Input: keys=["a","b"], values=[[1,2],[3,4]]
- Expected Output: {"a":[1,2],"b":[3,4]}

### 16) Partition List by Predicate
- Input: [1,2,3,4,5,6], predicate = even
- Expected Output: ([2,4,6],[1,3,5])

### 17) Safe Get Nested Value
- Input: d = {"a":{"b":{"c":10}}}, path = ["a","b","c"]
- Expected Output: 10 (or default if missing)

### 18) Count Unique by Key
- Input: [{"id":1,"dept":"HR"},{"id":2,"dept":"IT"},{"id":3,"dept":"HR"}]
- Expected Output: {"HR":2, "IT":1}

### 19) Rotate List Right by k
- Input: [1,2,3,4,5], k=2
- Expected Output: [4,5,1,2,3]

### 20) Chunk List into Size n
- Input: [1,2,3,4,5], n=2
- Expected Output: [[1,2],[3,4],[5]]
