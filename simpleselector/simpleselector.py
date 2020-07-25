class SelectionMenu:
    import colorama, keyboard, os
    def clear():
        if SelectionMenu.os.name == 'nt':
            SelectionMenu.os.system('cls')
        else:
            SelectionMenu.os.system('clear')
    options = []
    opt_return = ''
    cur_option = 0
    out_i = 0
    selected = 0
    title = ''
    running = False
    rich = False
    def dec_option(args):
        global cur_option, options, out_i, running
        if running == True:
            if not cur_option == len(options) - 1:
                cur_option += 1
            else:
                cur_option = 0
            SelectionMenu.reload()
    def inc_option(args):
        global cur_option, options, out_i, running
        if running == True:
            if not cur_option == 0:
                cur_option -= 1
            else:
                cur_option = len(options) - 1
            SelectionMenu.reload()
    def reload():
        if SelectionMenu.rich:
            exec('print(' + SelectionMenu.title + ')')
        else:
            print(SelectionMenu.title)
        print(SelectionMenu.colorama.Fore.GREEN + SelectionMenu.title + SelectionMenu.colorama.Style.RESET_ALL)
        global out_i, selected, cur_option
        if cur_option > len(options):
            cur_option = 0
        for out_i in range(0, len(options)):
            if out_i == cur_option:
                print(SelectionMenu.colorama.Fore.BLUE, SelectionMenu.options[out_i], SelectionMenu.colorama.Style.RESET_ALL)
                selected = out_i
            else:
                print(options[out_i])
    def showSelectionMenu():
        global out_i, running, cur_option
        running = True
        cur_option = 0
        SelectionMenu.reload()
        SelectionMenu.keyboard.wait('enter')
        running = False
        input()
        return options[selected]
        SelectionMenu.clear()
    keyboard.on_press_key('down', dec_option)
    keyboard.on_press_key('up', inc_option)
