#!/usr/bin/python2

import tsort, os, filecmp

def main():
    testcases = [f for f in os.listdir("test") if f[:3] == "inp"]
    os.chdir("test")
    count = 0
    for fname in testcases:
        edges_list = []

        with open(fname, "r") as f:
            n, m = map(int, f.readline().split(" ")[:2])
            for i in xrange(m):
                u, v = map(int, f.readline().split(" ")[:2])
                edges_list.append((u, v))

        out = tsort.tsort(edges_list, n)

        fout = open(fname.replace("inp", "myout"), "w")
        for i in out:
            fout.write(str(i) + " ")

        fout.close()

        if filecmp.cmp(fname.replace("inp", "myout"), fname.replace("inp", "out")):
            count += 1
        else:
            print "failed at", fname

    print "passed", count, "/", len(testcases)

if __name__ == "__main__":
    main()