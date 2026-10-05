"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    res = {i:[] for i in range(num_rows)}
    is_going_down = True
    current_row = 0
    for i, c in enumerate(s):
        res[current_row].append(c)

        if current_row == num_rows - 1 :
            is_going_down = False
        elif current_row == 0:
            is_going_down = True

        if is_going_down:
            current_row += 1
        else:
            current_row -= 1

    l = []
    for i in range(num_rows):
        l.extend(res[i])

    return ''.join(l)

if __name__ == '__main__':
    assert convert(s = "PAYPALISHIRING", num_rows = 3) == "PAHNAPLSIIGYIR"
    assert convert(s = "PAYPALISHIRING", num_rows = 4) == "PINALSIGYAHRPI"
    assert convert(s = "A", num_rows = 1) == "A"
