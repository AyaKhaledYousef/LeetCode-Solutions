
word1 = 'abctyu'
word2 = 'pqr'
def mergeAlternately(word1,word2):

    res = ""
    mn = min(len(word1),len(word2))
    mx = max(len(word1),len(word2))

    for i in range(mn):
        res += word1[i]
        res += word2[i]

    if len(word1) > len(word2):
        res += word1[mn:]

    else:
        res += word2[mn:]

    return res
print(mergeAlternately(word1,word2))
############################################################

# import threading
# import time 

# def word1():
#     w = 'abc'
#     for i in w :
#         print(i)
#         time.sleep(1)

# def word2():
#     w = 'pqr'
#     for i in w :
#         print(i)
#         time.sleep(1)

# thread1=threading.Thread(target=word1)
# thread2=threading.Thread(target=word2)

# thread1.start()
# time.sleep(0.5)
# thread2.start()

# # thread1.join()
# # thread2.join()
