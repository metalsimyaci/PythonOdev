import codecs
#dosya işlemlerinde kullanılacak dosya değişkeni
FILENAME="userinformation.txt"

# Dosya yazma fonksiyonu
# content olarak belitilen içeriği dosyaya yazar.
# dosya mevcut dizine ekleme modu (yoksa oluşturur, varsa üzerine ekler) ile oluşturulur
def writeFile(content):
    with codecs.open(FILENAME,"a",'utf-8') as dosya:
        dosya.writelines(content)
#Kullanıcı bilgilerini kullanıcıdan alarak dosyaya yazar
def writeUserInformation():    
    name = input("Adınız giriniz:")
    surname = input("Soyadınızı giriniz:")
    ageString = input("Yaşınızı giriniz:")
    writeFile("Ad:"+name+",Soyad:"+surname+",Yas:"+ageString+"\n")
    print("Kullanıcı bilgileri başarı ile alındı")

#Dosyadan kullanıcı bilgilerini okuyarak ekrana yazar
def readUserIformation():
    print("\n\n**** Kullanıcı Bilgileri ***")
    with codecs.open(FILENAME, "r",'utf-8') as dosya:
        print(dosya.read())
        
#Kullanıcı işlem menüsünü görüntüler
def menu():
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
            readUserIformation()
        elif ans =="3":
            exit()
        else:
            print("\n ** Lütfen geçerli bir seçim yağınız **\n")
menu()