item = {0:{'name': 'Agaton', 'last_name': 'Kowalski', 'phone_no': '666 666 666', 'email': 'panto@prot.com'} }
item1 = {1:{'name': 'Kimbla', 'last_name': 'Cardano', 'phone_no': '786 555 444', 'email': 'rtaanto@greprot.net'} }
item2 = {2:{'name': 'Hinata', 'last_name': 'Hyuga', 'phone_no': '586 555 444', 'email': 'hinatao@konoha.net'} }
item3 = {3:{'name': 'Kakashi', 'last_name': 'Hatake', 'phone_no': '486 555 444', 'email': 'kakashi.h@konoha2.net'} }
item4 = {3:{'name': 'Alucard', 'last_name': 'Dracula', 'phone_no': '486 555 444', 'email': 'transylwaniantrip@sailwithus.net'} }
items_list = [item, item1, item2, item3, item4]
def user_input(message):
    while True:
        c = input(f"{message}:").lstrip().rstrip()
        if len(c) >= 1:
            break
    print(f"your input is '{c}'")
    return c


def ui_check(input, checktype):
    if checktype == 'name':
        for n in input:
            if not(n.isalpha()) and (n != ' '):
                print('Name cant contains numbers!')
                return -1
        input = input.split(' ')
        inpres = []
        print(input)
        for i, inp in enumerate(input):
            inp = inp[0].upper()+inp[1:].lower()
            inpres.append(inp.rstrip().lstrip())
        input = inpres
        print(f"name res is: {input}")
        return ' '.join(input)

    elif checktype == 'last_name':
        if input.count('-') > 0:
            input = input.split('-')
        else:
            input = input.split(' ')
        for n in input:
            if not n.isalpha():
                print(f"Last Name have to contains only letter! '{n}'")
                return -1
        inpres = []
        for i, inp in enumerate(input):
            # print(f"name parts: {inp}")
            inp = inp[0].upper() + inp[1:].lower()
            inpres.append(inp.rstrip().lstrip())
        input = inpres
        return '-'.join(input)

    elif checktype == 'phone_no':
        input = input.lstrip().rstrip().replace('-', '')
        if input == 'NO PHONE':
            return 'NO PHONE'
        just_digits = ''
        for n in input:
            if n.isdigit():
                just_digits += n

        if len(just_digits) == 9:
            input = just_digits[:3]+' '+just_digits[3:6]+' '+just_digits[6:]
        elif len(just_digits) == 11:
            input = '+' + just_digits[:2] + ' ' + just_digits[2:5] + ' ' + just_digits[5:8]+' '+just_digits[8:]
        else:
            # 11 < len(just_digits) < 9:
            print(f"Correct phone number contains 9 digits and optional 2 digits prefix!")
            return -1
        return input

    elif checktype == 'email':
        input = input.lstrip().rstrip()
        if input == 'NO @':
            return 'NO @'
        if input.count('@') != 1 or input[-4] != '.':
            print("email have to contains excatly one '@'  and domain '.com', '.net'!")
            return -1
        return input
    return -1


def add_customer(db):
    rec_def = ['name', 'last_name', 'phone_no', 'email']
    info_list = ['Input customer name',
                 'Input customer last name',
                 "Input customer phone number ('NO PHONE' for phoneless customer)",
                 "Input customer email ('NO @' for emailless customer)"]
    rec = {}
    for i, n in enumerate(rec_def):
        # print(f"Try to get {i} which is {n} ")
        uicheck = -1
        while uicheck == -1:
            ui_name = user_input(info_list[i])
            uicheck = ui_check(ui_name, n)
            # print(f"UICHECK RES: {uicheck}")
        rec[n] = uicheck

    slot = get_avail_slot(items_list)
    print(f"GATHERED INFO: name{rec}")
    print(f"Saved at #{slot}")
    return db.append({slot: rec})


def print_db(db):
    for it in items_list:
        # print(it)
        for k, v in it.items():
            # info_string = [it[k]]
            print(f"#{k}: {it[k]['name']} {it[k]['last_name']} {it[k]['phone_no']} {it[k]['email']}")
            # for kk, vv in it[k].items():
            #     print(kk)
def get_avail_slot(db):
    slot = len(db)
    for i, item in enumerate(db):
        # print(i, item)
        for k, v in item.items():
            # print(i, k)
            if i < k:
                slot = i
                # print(f"Free slot {i}")
                return slot
    return slot

def serve_menu():
    menu_pos = ['a', 'r', 'p', 'q']
    menu_message = 'q - quit , a - add customer, r - remove customer, p - print all data, number - print customer (if exists)'
    ui = user_input(menu_message)
    if ui.isdigit():
        return int(ui)
    elif ui.isalpha() and (ui.lower() in menu_pos):
        return ui.lower()
    else:
        print(f"command '{ui}' not found")
        return -1
def print_item(db, itemno):
    res = f'Item {itemno} Not found'
    for i, item in enumerate(db):
        # print(i, item)
        for k, v in item.items():
            if k == itemno:
                res  = f'#{itemno}: '
                # print(i, item[k].items())
                for kk, vv in item[k].items():
                    # res += kk+ ' : ' + vv +' '
                    res += ' : ' + vv +' '
                # print(f"Will be returned: {res}, {i}")
                return res, i
    return res, None

def remove_item(db, itemno):
    # print("type db:",  type(db), "type itemno: ", type(itemno) )
    res, idx = print_item(db, itemno)
    if idx is None:
        print(f'Item {itemno} Not found')
        return db
    # print(res, idx)
    message = 'Remove? (Y/N)'
    choice = user_input(message)
    # while (choice.lower() != 'y') or (choice.lower() != 'n'):
    #     choice = user_input(message)
    #     print(f"CHOICE {choice}")
    if choice.lower() == 'y':
       db.pop(idx)
       print(f"Item #{itemno} deleted")

    return db

def main():
    menu_input = ''
    while menu_input != 'q':
        menu_input = serve_menu()
        # print(menu_input)
        if menu_input == 'a':
            add_customer(items_list)
        elif menu_input == 'r':
            message = 'Item no to remove:'
            ui = user_input(message)
            if (isinstance(int(ui), int)):
                remove_item(items_list, int(ui))
            else:
                print('Not a number or item doesnt exists')
            # print("remove will be runn")
        elif menu_input == 'p':
            print_db(items_list)
        elif menu_input == 'q':
            print("quit")
        elif isinstance(menu_input, int):
            # print("Position from list print")
            print(print_item(items_list, menu_input)[0]+'\n')

    # add_customer(items_list)
    # print_db(items_list)
    # for k in items_list:
    #     for kk, vv in k.items():
    #         print(kk)

    # print(get_avail_slot(items_list))

main()