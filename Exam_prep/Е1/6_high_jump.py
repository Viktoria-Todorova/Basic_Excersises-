jump_wanted = int(input())
jump_success = jump_fail = jumps= 0
start_jump = jump_wanted - 30
while True:
    jump = int(input())
    jumps += 1
    current_jump = start_jump

    if jump > start_jump :
        jump_success += 1
        start_jump += 5
        jump_fail = 0
    elif jump <= start_jump:
        jump_fail +=1

    if jump_fail == 3:
        print(f"Tihomir failed at {start_jump}cm after {jumps} jumps.")
        break

    if jump_wanted < start_jump:
        print(f"Tihomir succeeded, he jumped over {current_jump}cm after {jumps} jumps.")
        break







