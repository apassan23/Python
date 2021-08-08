import pickle

# pickling, unpickling
# byte stream


def readFile(fname):
    with open(fname, 'rb') as file:
        # unpickling
        data = pickle.load(file)
        print(max(data), min(data))


def writeFile(fname, content):
    file = open(fname, 'ab')
    # pickling
    pickle.dump(content, file)  # same as file.write(content)
    file.close()


x = [-1, 12, 32, 91]
fname = 'dummy_pickle.txt'
writeFile(fname, x)
readFile(fname)
