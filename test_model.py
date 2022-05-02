

def waiting_num(ticket_num, current_num):
    return ticket_num - current_num

number = []

def store_ticket_num(ticket_num):
    number.append(ticket_num)
    return number
        

def get_number():
    y_number = number.pop()
    y_number_int = int(y_number)
    return y_number_int