def user_prompt(string, options):
    while True:
        try:
            choice = int(input(string))
            if options >= choice > 0:
                return choice
        except:
            print("Not one of your options. :")
