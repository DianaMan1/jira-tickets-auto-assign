def get_maximum_number_of_tickets_to_be_assigned(out_of: int):
    max_out_of = 5
    if(out_of < 5):
        max_out_of = out_of
    
    max_number = None
    while max_number is None:
        user_input = input(f'Insert the maximum number of tickets to be assigned(out of {max_out_of}): ')
        if not user_input.isdigit():
            continue
        if int(user_input) > max_out_of:
            continue
        max_number = user_input
    return int(max_number)
