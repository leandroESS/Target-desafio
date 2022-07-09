def inverte(string): 
    if len(string) == 0: 
        return string 
    else: 
        return inverte(string[1:]) + string[0] 



if __name__ == '__main__':
    string = input('Digite a string\n')
    print(inverte(string))