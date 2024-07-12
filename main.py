import tkinter  # GUI oluşturmak için tkinter modülünü içe aktar
from tkinter import *  # tkinter modülünden tüm bileşenleri içe aktar
import speedtest  # İnternet hızını test etmek için speedtest modülünü içe aktar
import tkinter.messagebox  # Mesaj kutuları oluşturmak için tkinter.messagebox modülünü içe aktar

option=''  # Küresel değişken option, kullanıcı tarafından seçilen hız testi türünü saklar

# İndirme hızını test eden fonksiyon
def downloadSpeed():
    global option
    option='İndirme Hızın'
    showSpeed()

# Yükleme hızını test eden fonksiyon
def uploadSpeed():
    global option
    option='Yükleme Hızın'
    showSpeed()

# Ping (gecikme) süresini test eden fonksiyon
def ping():
    global option
    option='Ping/ms gecikmen'
    showSpeed()

# Seçilen hız testi türüne göre hızı gösteren fonksiyon
def showSpeed():
    global option
    st = speedtest.Speedtest()  # Speedtest nesnesi oluştur
    if option == 'İndirme Hızın':
        speed = st.download()  # İndirme hızını ölç

    elif option == 'Yükleme Hızın':
        speed = st.upload()  # Yükleme hızını ölç

    elif option == 'Ping/ms gecikmen':
        servernames = []
        st.get_servers(servernames)  # Sunucuları al
        speed = st.results.ping  # Ping süresini ölç
    
    # Hızı birimlerine göre uygun formatta göster
    speedWithUnits=''
    if(speed < 1000):
        speedWithUnits = str(round(speed, 3)) + " bps"
    elif(speed < 1000000):
        speedWithUnits = str(round(speed / 1000, 3)) + " Kbps"
    elif(speed < 1000000000):
        speedWithUnits = str(round(speed / 1000000, 3)) + " Mbps"
    else:
        speedWithUnits = str(round(speed / 1000000000, 3)) + " Gbps"

    # Sonucu bir mesaj kutusunda göster
    tkinter.messagebox.showinfo("AE SPEED TEST", " Merhaba Senin " + option + " : " + speedWithUnits)

# Ana pencere oluştur
wn = tkinter.Tk()
wn.title("AE SPEED TEST")  # Pencere başlığını ayarla
wn.geometry('1000x300')  # Pencere boyutlarını ayarla
wn.config(bg='black')  # Pencere arka plan rengini ayarla

# Başlık etiketi oluştur
Label(wn, text='Speed Test', bg='black', fg='aqua', font=('FANTASY', 15)).place(x=450, y=10)

# Kullanıcıya seçenekleri anlatan etiket oluştur
Label(wn, text='TEST YAPMAK İSTEDİĞİN SEÇENEĞİ SEÇ', bg='black', fg='green', font=('Courier', 10)).place(x=400, y=60)

# İndirme hızı kontrol butonu oluştur
Button(wn, text="İndirme Hızını Kontrol Et", bg='red', fg='white', font=('Courier', 15), width=60,
       command=downloadSpeed).place(x=150, y=120)

# Yükleme hızı kontrol butonu oluştur
Button(wn, text="Yükleme Hızını Kontrol Et", bg='red', fg='white', font=('Courier', 15), width=60,
       command=uploadSpeed).place(x=150, y=170)

# Ping kontrol butonu oluştur
Button(wn, text="Ping ms kontrol Et", bg='red', fg='white', font=('Courier', 15), width=60,
       command=ping).place(x=150, y=220)

# Pencereyi çalıştır
wn.mainloop()
