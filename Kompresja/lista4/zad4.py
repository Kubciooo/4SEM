import numpy as np
from PIL import Image
from zad1 import entropy
import sys
#P0 = nic
#P1 = A -> pixel[i][j] -= pixel[i-1][j]
#P2 = B -> pixel[i][j] -= pixel[i][j-1]
# P3 = C -> pixel[i][j] -= pixel[i-1][j-1]
#P4 = A + B - C

def P1(image):
    im = image.copy()
    for y in range(image.height):
        for x in range(1,image.width):
            (r1,g1,b1) = image.getpixel((x-1,y))
            (r2,g2,b2) = image.getpixel((x,y))
            im.putpixel((x,y), (abs(r2-r1)%256,abs(g2-g1)%256,abs(b2-b1)%256))
    return im

def P2(image):
    im = image.copy()
    for x in range(image.width):
        for y in range(1,image.height):
            (r1,g1,b1) = image.getpixel((x,y-1))
            (r2,g2,b2) = image.getpixel((x,y))
            im.putpixel((x,y), (abs(r2-r1)%256,abs(g2-g1)%256,abs(b2-b1)%256))
    return im


def P3(image):
    im = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            (r1,g1,b1) = image.getpixel((x-1,y-1)) if x>0 and y>0 else (0,0,0)
            (r2,g2,b2) = image.getpixel((x,y))
            im.putpixel((x,y), (abs(r2-r1)%256,abs(g2-g1)%256,abs(b2-b1)%256))
    return im

def P4(image):
    im = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            (ra,ga,ba) = image.getpixel((x-1,y)) if x>0 else (0,0,0)
            (rb,gb, bb) = image.getpixel((x,y-1)) if y >0 else (0,0,0)
            (rc,gc,bc) = image.getpixel((x-1,y-1)) if x>0 and y>0 else (0,0,0)
            (r,g,b) = image.getpixel((x,y))
            rw = abs(r- (ra+rb-rc))%256
            gw = abs(g - (ga+gb-gc))%256
            bw = abs(b - (ba+bb-bc))%256
            im.putpixel( (x,y),(rw,gw,bw))
    return im

def P5(image):
    im = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            (ra,ga,ba) = image.getpixel((x-1,y)) if x>0 else (0,0,0)
            (rb,gb, bb) = image.getpixel((x,y-1)) if y >0 else (0,0,0)
            (rc,gc,bc) = image.getpixel((x-1,y-1)) if x>0 and y>0 else (0,0,0)
            (r,g,b) = image.getpixel((x,y))
            rw = abs(r- (ra+int((rb-rc)/2)))%256
            gw = abs(g - (ga+ int((gb-gc)/2) ))%256
            bw = abs(b - (ba+ int( (bb-bc)/2)))%256
            im.putpixel( (x,y),(rw,gw,bw) )
    return im

def P6(image):
    im = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            (ra,ga,ba) = image.getpixel((x-1,y)) if x>0 else (0,0,0)
            (rb,gb, bb) = image.getpixel((x,y-1)) if y >0 else (0,0,0)
            (rc,gc,bc) = image.getpixel((x-1,y-1)) if x>0 and y>0 else (0,0,0)
            (r,g,b) = image.getpixel((x,y))
            rw = abs(r- (rb+int((ra-rc)/2)))%256
            gw = abs(g - (gb+ int((ga-gc)/2) ))%256
            bw = abs(b - (bb+ int( (ba-bc)/2)))%256
            im.putpixel( (x,y),(rw,gw,bw) )
    return im

def P7(image):
    im = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            (ra,ga,ba) = image.getpixel((x-1,y)) if x>0 else (0,0,0)
            (rb,gb, bb) = image.getpixel((x,y-1)) if y >0 else (0,0,0)
            (r,g,b) = image.getpixel((x,y))
            rw = abs(r- (int( (ra+rb)/2) ))%256
            gw = abs(g- (int( (ga+gb)/2) ))%256
            bw = abs(b- (int( (ba+bb)/2) ))%256
            im.putpixel( (x,y),(rw,gw,bw) )
    return im

def P8(image):
    im = image.copy()
    for y in range(image.height):
        for x in range(image.width):
            (ra,ga,ba) = image.getpixel((x-1,y)) if x>0 else (0,0,0)
            (rb,gb, bb) = image.getpixel((x,y-1)) if y >0 else (0,0,0)
            (rc,gc,bc) = image.getpixel((x-1,y-1)) if x>0 and y>0 else (0,0,0)
            (r,g,b) = image.getpixel((x,y))
            rw = abs(r- (ra+rb-rc))%256
            gw = abs(g - (ga+gb-gc))%256
            bw = abs(b - (ba+bb-bc))%256
            if rc >= max(ra,rb) and gc >= max(ga,gb) and bc >= max(ba,bb):
                rw = abs(r -  min(ra,rb))%256
                gw = abs(g - min(ga,gb))%256
                bw = abs(b - min(ba,bb))%256
            elif rc <= min(ra,rb) and gc <= min(ga,gb) and bc <= min(ba,bb):
                rw = abs(r - max(ra,rb))%256
                gw = abs(g - max(ga,gb))%256
                bw = abs(b - max(ba,bb))%256
            im.putpixel( (x,y),(rw,gw,bw) )
    return im

    
def get_optimal_entropy(image):
    entropies = dict()
    im1= P1(image)
    entropies["P1"] = entropy(im1)
    im2 = P2(image)
    entropies["P2"] = entropy(im2)
    im3 = P3(image)
    entropies["P3"] = entropy(im3)
    im4 = P4(image)
    entropies["P4"] = entropy(im4)
    im5 = P5(image)
    entropies["P5"] = entropy(im5)
    im6 = P6(image)
    entropies["P6"] = entropy(im6)
    im7 = P7(image)
    entropies["P7"] = entropy(im7)
    im8 = P8(image)
    entropies["P8"] = entropy(im8)
    v=list(entropies.values())
    k=list(entropies.keys())
    print("Dla całego obrazu najlepszą metodą jest: ",k[v.index(min(v))],' o entropii równej', min(v))

def get_optimal_color_entropy(image, RGB):
    "aby uzykać R - RGB = 0, B -> RGB = 1, B -> RGB = 2"
    entropies = dict()
    colors = ["R", "G", "B"]
    im1= P1(image)
    entropies["P1"] = entropy([color for color in im1.getdata(RGB)])
    im2 = P2(image)
    entropies["P2"] = entropy([color for color in im2.getdata(RGB)])
    im3 = P3(image)
    entropies["P3"] = entropy([color for color in im3.getdata(RGB)])
    im4 = P4(image)
    entropies["P4"] = entropy([color for color in im4.getdata(RGB)])
    im5 = P5(image)
    entropies["P5"] = entropy([color for color in im5.getdata(RGB)])
    im6 = P6(image)
    entropies["P6"] = entropy([color for color in im6.getdata(RGB)])
    im7 = P7(image)
    entropies["P7"] = entropy([color for color in im7.getdata(RGB)])
    im8 = P8(image)
    entropies["P8"] = entropy([color for color in im8.getdata(RGB)])

    v=list(entropies.values())
    k=list(entropies.keys())
    print("Dla koloru ", colors[RGB]," najlepszą metodą jest: ",k[v.index(min(v))],' o entropii równej', min(v))


def print_entropy(image):
    colors = [color for color in  image.getdata()]
    print("Entropia całego obrazu: ", entropy(colors))
    colors_R = [color for color in image.getdata(0)]
    colors_G = [color for color in image.getdata(1)]
    colors_B = [color for color in image.getdata(2)]
    print("Entropia R: ", entropy(colors_R), ', entropia G: ', entropy(colors_G), ", entropia B: ", entropy(colors_B))


im = Image.open(sys.argv[1])

print("P0")
print_entropy(im)
print("P1")
im1= P1(im)
print_entropy(im1)
print("P2")
im2 = P2(im)
print_entropy(im2)
print("P3")
im3 = P3(im)
print_entropy(im3)
print("P4")
im4 = P4(im)
print_entropy(im4)
print("P5")
im5 = P5(im)
print_entropy(im5)
print("P6")
im6 = P6(im)
print_entropy(im6)
print("P7")
im7 = P7(im)
print_entropy(im7)
print("P8")
im8 = P8(im)
print_entropy(im8)
print("="*100)
print("Początkowa entropia: ")
print_entropy(im)
print("="*100)

get_optimal_entropy(im)
get_optimal_color_entropy(im,0)
get_optimal_color_entropy(im,1)
get_optimal_color_entropy(im,2)