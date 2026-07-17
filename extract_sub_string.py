import textwrap
def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width):
        result += string[i:i+max_width] + "\n"
    return result.rstrip()
if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)
