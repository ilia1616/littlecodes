import os
infos = ''
file_name = "file.txt"
def run_():
    while True:
        num = input('enter "1" to get info\nenter "2" to enter info in log file\n enter "3" to show the log file\nenter "4" to clear page\nenter "0" to exit\nnumber: ')
        numb = int(num)
        f = open(file_name, 'at')
        if numb == 1:
            infos = input('enter you informaitons: ')
        elif numb == 2:
            f.write(str(infos + '\n'))
            f.close()
        elif numb == 3:
            f = open(file_name, 'r')
            print('----------------------------------------')
            print(f.read())
            print('----------------------------------------')
        elif numb == 4:
            os.system('cls')
        elif numb == 0:
            break
        else:
            print('your number is wrong!')
        print('-----------------------------------------------------------------------')

if __name__ == '__main__':
    run_()