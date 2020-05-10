# operator B
B = [
    [0.4,0.6,0],
    [0.2,0.1,0.7],
    [0.4,0.3,0.3]
]

# the current state
v = [0.1,0.3,0.6]

#
# your solution is here
#

#B*v
v1=[0,0,0]
for i in range(3):
    for j in range(3):
        v1[i] += B[i][j]*v[j]
print(v1)
