'''9.Given list of tuples, remove all the tuples with length K.
Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
Explanation : (4, 5) of len = 2 is removed.
'''

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
K = int((input("enter list otf tuple to be removed:")))

result = [tup for tup in test_list if len(tup) != K]
not_result = [tup for tup in test_list if len(tup) == K]
print("output:",result)
print("Explanation:",not_result)