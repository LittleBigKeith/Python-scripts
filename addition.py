def draw_horizontal_line():
    print('-' * (len(tape) * 2 + 1))

def print_current_tape():
    draw_horizontal_line()
    print('|', '|'.join(value for value in tape), '|', sep = '')
    draw_horizontal_line()
    try:
        current_pos
        current_state
        print(' ' * (current_pos * 2), '^')
        print(' ' * (current_pos * 2), current_state)
    except NameError:
        pass

while True:
    user_input = input('Enter 2 numbers separated by a comma (,):').split(',')
    try:
        user_input[0] = int(user_input[0])
        user_input[1] = int(user_input[1])
        break
    except ValueError:
        continue
    except IndexError:
        continue
        
print(user_input[0], ',', user_input[1], sep='')

tape = ['0'] * 1 + ['1'] * user_input[0] + ['0'] * 1 + ['1'] * user_input[1] + ['0'] * 1
print_current_tape()

TM_program = {}
with open('addition.txt') as TM_program_file:
    for instruction in TM_program_file.readlines():
        if instruction.startswith('#'):
            first_line = instruction.split()
            initial_state = first_line[3]
            continue
        elif instruction.isspace():
            continue
        current_state, current_val, new_state, new_val, direction = instruction.split()
        TM_program[current_state, current_val] = new_state, new_val, direction

print(TM_program)
print(initial_state)

current_state = initial_state;
current_pos = tape.index('1')
current_val = tape[current_pos]
total_step = 0

print_current_tape()
while (current_state, current_val) in TM_program: 
    new_state, new_val, direction = TM_program[current_state, current_val]

    tape[current_pos] = new_val
    current_state = new_state
    current_pos = current_pos + 1 if direction == 'R' else current_pos - 1
    current_val = tape[current_pos]
    total_step += 1

    print_current_tape()

print('Total steps:', total_step)


