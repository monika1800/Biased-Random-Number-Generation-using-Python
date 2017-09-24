from time import time
import time as t


def generate(mod, iterate):
    multiplier, seed = validation(mod, iterate)
    output = [seed]
    current_iteration = -1
    switch = False

    while current_iteration != seed and current_iteration != 0:
        if not switch:
            current_iteration = (seed * multiplier) + iterate
            switch = True
        else:
            current_iteration = (current_iteration * multiplier) + iterate
            if current_iteration > mod:
                current_iteration %= mod
            output.append(current_iteration)

    result = int(str(''.join([str(i) for i in output]))[-1])
    return result


def input_values():
    x = y = 0
    while not x and not y:
        try:
            x, y = int(str(time() - int(time()))[-1]), int(str(time() - int(time()))[-2])
        except ValueError:
            input_values()
    return x, y


def validation(mod, iterate):
    rel = 0
    while not rel:
        multiplier, seed = input_values()
        rel = 0 <= iterate < mod and 0 <= seed < mod and multiplier in [1, 3, 7, 9]

    return multiplier, seed


def main():
    start = t.ctime().split(" ")[3]
    list1 = []
    list2 = []
    m = 10
    i = 0
    loop = True
    times = 100
    while loop:
        t.sleep(0.00000000000001)
        num = generate(m, i)
        # print num
        if num >= 5:
            if len(list1) < 73:
                list1.append(num)
        else:
            if len(list2) < 27:
                list2.append(num)
        if len(list1) == 73 and len(list2) == 27:
            loop = False
    end = t.ctime().split(" ")[3]
    len_min=len(list2)
    len_max=len(list1)
    print("Length of Minimum List: {}\nLength of Maximum List: {} ".format(len_min,len_max))
    print("Minimum List\n{}".format(list2))
    print("Maximum List\n{}".format(list1))


if __name__== '__main__':main()