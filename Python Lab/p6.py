# f1 = open("file1.txt", "r")
# L = list()
# for i in f1:
#     L.append(int(i))
# L.sort()
# f2 = open("file2.txt", "w")
# for i in range(len(L)):
#     f2.write(str(L[i]))
#     f2.write("\n")

# infile = open("file1.txt", "r")
# words = []
# for line in infile:
#     temp = line.split()
# for i in temp:
#     words.append(i)
# infile.close()
# words.sort()
# outfile = open("file2.txt", "w")
# for i in words:
#     outfile.write(i)
#     outfile.write(" ")
# outfile.close()


# f2 = open("file2.txt", "w")
# with open("file1.txt", "r") as myfile:
#     data = myfile.read()
# data_1 = data[::-1]
# for i in range(len(data_1)):
#     f2.write(data_1[i])
