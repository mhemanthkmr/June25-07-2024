# task13 finding duplicate with hashing O(n)

sample_list = [1,2, 3, 4, 5, 3, 2, 6, 7, 8, 1]
N=max(sample_list)
hash= [0] * (N + 1)
duplicates = []


for i in sample_list:
     if hash[i] == 0:
            hash[i] = 1
     elif hash[i] == 1:
            duplicates.append(i)
            hash[i] += 1
print("duplicates:",duplicates)