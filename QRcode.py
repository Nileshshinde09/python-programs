'''
    QRcode Generator
'''
import qrcode
class Qrcode(): 
    def __init__(self,data,name) -> None:
        
        img = qrcode.make(data)
        img.save(name+'.png')


if __name__=="__main__":
    URL_link = input("Enter the link or URL :")
    QRName = input("Enter name for QRCode :")
    Qrcode(URL_link,QRName)


             