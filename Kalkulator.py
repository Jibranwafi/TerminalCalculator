


def add(a, b):
    c = a + b
    return "%s + %s = %s"%(int(a), int(b), int(c))

def subtract(a, b):
    c = a - b
    print(a,"-", b,"=",c)
''' 
def multiplication(a, b):
    c = int(a)*int(b) 
    print (a, "*", b, "=", c)
'''
    
def division(v1, v2):
    return 0


def main():
    v1 = float(input("Masukan variabel 1: "))
    v2 = float(input("Masukan variabel 2: "))
    print("Pilih operasi yang ingin di pakai\n"
          "1 = add\n"
          "2 = subtract\n"
          "3 = multiplication\n"
          "4 = division")
    operasi = int(input(">> "))
    if operasi == 1:
        print(add(v1, v2))
    elif operasi == 2:
        subtract(v1, v2)
        
    elif operasi == 3:
        c = int(v1)*int(v2)
        print(f"{v1}*{v2}={c}")
        while c:
            am = input("kali lagi? [y/n]")
            if am == "y":
                var = int(input("variable = "))
                c *= var
                print(f"{v1}*{v2} = {c}")
            elif am == "n":
                return main()
            else:
                print("error")
                break
        
    elif operasi == 4:
        division(v1, v2)
    else:
        print(f"Tidak ada pilihan {operasi} didalam kalkulator ini")
        
    option = input("Gunakan lagi? [y/n] ")
    if option == "y":
        main()
    else:
        print("Selesai")

if __name__ == '__main__':
    main()
