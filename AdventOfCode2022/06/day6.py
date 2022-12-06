input_data = open('input.txt', 'r').read()


def check_marker(n_marker):
    count = 0
    for i in range(len(input_data)):
        marker = input_data[i:i+n_marker]

        if len(set(marker)) == len(marker):
            count += n_marker
            break
        else:
            count += 1
    return count

print(check_marker(4))
print(check_marker(14))