import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Task data (you can paste your 100 tasks here)
data = """1,Task 1,1,1
2,Task 2,2,2
3,Task 3,3,3
4,Task 4,4,4
5,Task 5,5,5
6,Task 6,6,6
7,Task 7,7,7
8,Task 8,8,8
9,Task 9,9,9
10,Task 10,10,10
11,Task 11,1,11
12,Task 12,2,12
13,Task 13,3,13
14,Task 14,4,14
15,Task 15,5,15
16,Task 16,6,16
17,Task 17,7,17
18,Task 18,8,18
19,Task 19,9,19
20,Task 20,10,20
21,Task 21,1,21
22,Task 22,2,22
23,Task 23,3,23
24,Task 24,4,24
25,Task 25,5,25
26,Task 26,6,26
27,Task 27,7,27
28,Task 28,8,28
29,Task 29,9,29
30,Task 30,10,30
31,Task 31,1,31
32,Task 32,2,32
33,Task 33,3,33
34,Task 34,4,34
35,Task 35,5,35
36,Task 36,6,36
37,Task 37,7,37
38,Task 38,8,38
39,Task 39,9,39
40,Task 40,10,40
41,Task 41,1,41
42,Task 42,2,42
43,Task 43,3,43
44,Task 44,4,44
45,Task 45,5,45
46,Task 46,6,46
47,Task 47,7,47
48,Task 48,8,48
49,Task 49,9,49
50,Task 50,10,50
51,Task 51,1,51
52,Task 52,2,52
53,Task 53,3,53
54,Task 54,4,54
55,Task 55,5,55
56,Task 56,6,56
57,Task 57,7,57
58,Task 58,8,58
59,Task 59,9,59
60,Task 60,10,60
61,Task 61,1,1
62,Task 62,2,2
63,Task 63,3,3
64,Task 64,4,4
65,Task 65,5,5
66,Task 66,6,6
67,Task 67,7,7
68,Task 68,8,8
69,Task 69,9,9
70,Task 70,10,10
71,Task 71,1,11
72,Task 72,2,12
73,Task 73,3,13
74,Task 74,4,14
75,Task 75,5,15
76,Task 76,6,16
77,Task 77,7,17
78,Task 78,8,18
79,Task 79,9,19
80,Task 80,10,20
81,Task 81,1,21
82,Task 82,2,22
83,Task 83,3,23
84,Task 84,4,24
85,Task 85,5,25
86,Task 86,6,26
87,Task 87,7,27
88,Task 88,8,28
89,Task 89,9,29
90,Task 90,10,30
91,Task 91,1,31
92,Task 92,2,32
93,Task 93,3,33
94,Task 94,4,34
95,Task 95,5,35
96,Task 96,6,36
97,Task 97,7,37
98,Task 98,8,38
99,Task 99,9,39
100,Task 100,10,40"""

# Split and insert
for line in data.strip().splitlines():
    id_, name, priority, total_time = line.split(',')
    key = f"task:{id_}"
    r.hset(key, mapping={
        "name": name,
        "priority": int(priority),
        "total_time": int(total_time)
    })

print("✅ All tasks successfully inserted into Redis!")
