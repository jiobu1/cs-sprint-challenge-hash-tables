# Your code here
def finder(files, queries):
    """
    YOUR CODE HERE
    """

    # does not pass large test/takes too long to run

    result = []

    file_path = {}

    for path in files:
        filename = path.split('/')[-1]
        file_path[filename] = path

    for k, v in file_path.items():
        if k in queries:
            result.append(v)


    # q = {}
    # result = []
    # for i in queries:
    #     if i in q:
    #         q[i] +=1
    #     else:
    #         q[i] = 1

    # for x  in files:
    #     for k in q:
    #         if k in x:
    #             result.append(x)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
