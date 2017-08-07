# coding: utf-8
import random

def main():
    f = open("data1.txt", "w")
    for i in range(30):
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        write_str = "({},{})".format(x, y)
        f.write(write_str)
        if i != 29:
            f.write("\n")
    f.close()


if __name__ == "__main__":
    main()
