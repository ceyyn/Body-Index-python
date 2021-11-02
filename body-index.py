renk = "\033[94m"
varsayilan = "\033[0m"
alt = "\033[4m"
while True:
    leng = float(input("Enter your lenght as  meter: "))
    heigh = float(input("Enter your height as kilogram : "))
    temp = leng * leng
    x = heigh / temp

    if x < 45:
        y = "2. sınıf Obez"
        if x < 35 :
            y = "1. sınıf Obez"
            if x < 30:
                y = "Fazla kilolu"
                if x < 25:
                    y = "İdeal"
                    if x < (19):
                        y = "Zayıf"
    elif x > 45:
        y = "3. Sınıf Aşırı Obez"
    else:
        y = "Değer algılanamadı."
    print(varsayilan+"\n                                  İndex : " +renk + alt + str(y)+varsayilan)