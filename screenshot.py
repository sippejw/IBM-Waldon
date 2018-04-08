import pyscreenshot
def runner():
    im = pyscreenshot.grab(bbox=(500, 250, 850, 580))  # X1,Y1,X2,Y2
    im.save("/Users/jacksonsippe/Desktop/IBM Waldon/Questions/image.png")
