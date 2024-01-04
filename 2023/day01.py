from pathlib import Path
# Part 1
def part1(data):
    total = 0
    for line in data:
        digits = []
        for character in line:
            if character.isdigit():
                digits.append(int(character))
        total += digits[0] * 10 + digits[-1]
    return total

# Part 2
def part2(data):
    ints = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    new_data = []
    for line in data:
        new_data.append("")
        for i in range(len(line)):
            for value, intStr in enumerate(ints, 1):
                if line[i:].startswith(intStr):
                    new_data[-1] += str(value)
                    break
            new_data[-1] += line[i]

    return part1(new_data)


txtName = Path(__file__).stem + ".txt"
file = open(txtName, "r")

print(part1(file))

file.seek(0)
print(part2(file))
file.close()
