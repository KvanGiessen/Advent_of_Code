
def convert_input(full_list, pointer, nr_parameters):
    if full_list[pointer] == 99:
        nr_parameters = 0
        return full_list, nr_parameters
    a, b, c, d = full_list[pointer:pointer + (nr_parameters + 1)]
    if a == 1:
        full_list[d] = full_list[b] + full_list[c]
        nr_parameters = 3
        return full_list, nr_parameters
    if a == 2:
        full_list[d] = full_list[b] * full_list[c]
        nr_parameters = 3
        return full_list, nr_parameters


def loop_over(full_list):
    pointer = 0
    nr_parameters = 3
    while True:

        full_list, nr_parameters = convert_input(full_list, pointer, nr_parameters)
        if nr_parameters == 0:
            break
        pointer += (nr_parameters + 1)

    return full_list

if __name__ == '__main__':
    for noun in range(0, 100):
        for verb in range(0, 100):
            input_list = [1,noun, verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]

            if loop_over(input_list)[0] == 19690720:
                print(noun, verb)
                print(100 * noun + verb)
