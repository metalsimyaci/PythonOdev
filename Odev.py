def writeFile(content):
    dosya = open("userinformation.txt","a")
    dosya.writelines(content)
    dosya.close()
def writeUserInformation():    
    name = input("Adınız giriniz:")
    surname = input("Soyadınızı giriniz:")
    ageString = input("Yaşınızı giriniz:")
    writeFile("Adı:"+name+",Soyadı:"+surname+",Yaşı:"+ageString+"\n")
    print("Kullanıcı bilgileri başarı ile alındı")
def ReadUserIformation():
    print("\n\n**** Kullanıcı Bilgileri ***")
    with open("userinformation.txt", "r") as dosya:
        print(dosya.read())
def Menu():
    ans=True
    while ans:
        print("""
        ****** Ödev İşlem Menüsü **********
        
        1. Kullanıcı Bilgisi al
        2. Kullanı Bilgisi Görüntüle
        3. Çıkış

        ***********************************
        """)
        ans = input("Ne yapmak istersiniz?")
        if ans =="1":
            writeUserInformation()
        elif ans =="2":
            ReadUserIformation()
        elif ans =="3":
            exit()
        else:
            print("\n ** Lütfen geçerli bir seçim yağınız **\n")
Menu()