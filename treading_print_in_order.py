"""
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.



Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.


Constraints:

nums is a permutation of [1, 2, 3].

"""

import threading


class Foo:

    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self):
        print_first()
        self.first_done.set()

    def second(self):
        self.first_done.wait()
        print_second()
        self.second_done.set()

    def third(self):
        self.second_done.wait()
        print_third()


def print_first(): print("first", end="")


def print_second(): print("second", end="")


def print_third(): print("third", end="")


def manual_test():
    # for nums = [1, 3, 2]

    foo = Foo()

    thread1 = threading.Thread(target=foo.first)
    thread2 = threading.Thread(target=foo.second)
    thread3 = threading.Thread(target=foo.third)

    thread1.start()
    thread3.start()
    thread2.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    manual_test()

# test with pytest
from itertools import permutations
import pytest


@pytest.mark.parametrize("order", permutations([1, 2, 3]))
@pytest.mark.timeout(2)
def test_foo_order(order, capsys):
    foo = Foo()
    task_map = {1: foo.first,
                2: foo.second,
                3: foo.third}

    threads = []

    for num in order:
        t = threading.Thread(target=task_map[num])
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    captured = capsys.readouterr()

    assert captured.out == "firstsecondthird"
