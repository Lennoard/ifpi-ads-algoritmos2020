def eval_loop():
    while True:
        i = input('> ')
        if i == 'done':
            break
        else:
            try:
                print(eval(i)) 
            except Exception as e:
                print(str(e))



if __name__ == "__main__":
    eval_loop()