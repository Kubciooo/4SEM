import zad5
from collections import defaultdict
from PIL import Image
import numpy as np
import sys



def quantizate_z(im):
    x = zad5.image_to_pixels(im)
    #print(x)
    (a,b,c,d) = zad5.generate_codebook(x,2**int(sys.argv[2]))
    if int(sys.argv[2]) == 0: 
        a = [d[0] for i in range(len(x))]
        b = zad5.avg_distortion_c_list(a, x) 
        c = 0.00001
    im2 = zad5.pixels_to_image(im,a)
    return im2



def filter_y_and_z(x):
    # początkowo przefiltruj y i z. Y -> filter dolno, z-> fiter górno
    avg = [int(x[0][i]/2) for i in range(3)]
    y = list()
    y.append(tuple(avg))
    z = list()
    z.append(tuple(avg))
    for i in range(1,len(x)):
        avg = [int((x[i-1][j] + x[i][j])/2) for j in range(3)]
        avg2 = [int((x[i][j] - x[i-1][j])/2) for j in range(3)]
        y.append(tuple(avg))
        z.append(tuple(avg2))
    return y,z

def find_closest_vector(codebook, vector):
    #wycięta część zadania 5
    min_dist = None
    closest_code = None
    for i_c, code in enumerate(codebook): 
        d = zad5.euclid_squared(vector, code)
        if min_dist is None or min_dist > d:
            min_dist = d
            closest_code  = code
    return closest_code


def differential_encode(pixels_array, vectors):
    res = []
    #wynik
    previous_x = (0,0,0)
    #poprzedni x
    for pixel in pixels_array:
        new_difference = []
        new_difference = tuple([pixel[j] - previous_x[j] for j in range(3)])
        quantized_difference = find_closest_vector(vectors, new_difference) if vectors is not None else new_difference
        temp = [previous_x[j] + quantized_difference[j] for j in range(3)]
        previous_x = tuple(temp)
        res.append(quantized_difference)
    return res
 
def differential_decode(pixels_array):
    previous_x = (0,0,0)
    new_pixels = []
    for pixel in pixels_array:
        new_pixel = tuple(pixel[j] + previous_x[j] for j in range(3))
        previous_x = new_pixel
        new_pixels.append(new_pixel)
    return new_pixels


def mse(x,y):
    #błąd średniokwadratowy 
    return 1/len(x) * np.sum([zad5.euclid_squared(x[n],y[n]) for n in range(len(x))])


def mse_color(x,y,RGB):
    #błąd średniokwadratowy dla jednego koloru
    return 1/len(x) * np.sum([(x[n][RGB]-y[n][RGB])**2 for n in range(len(x))])


def signal_to_noise(x,y):
    t = np.array([(x[n][0])**2 + (x[n][1])**2 + (x[n][2])**2 for n in range(len(x))], dtype='int64')
    return 10*np.log10((1/len(x) * np.sum(t) * 1/mse(x,y)))

def decode(y,z):
    #dekodowanie zakodowanego sygnału
    x_new = list() 
    for i in range(len(y)):
        if i % 2 == 1: 
            avg = [int(y[i+1][j] - z[i+1][j]) for j in range(3)] if i+1 < len(y) else [int(y[i][j] - z[i][j]) for j in range(3)]
        else: 
            avg = [int(y[i][j] + z[i][j]) for j in range(3)]
        x_new.append(tuple(avg))
    return x_new



if __name__ == "__main__":
    image = Image.open(sys.argv[1])
    x = zad5.image_to_pixels(image)
    y,z = filter_y_and_z(x)
    y_img = zad5.pixels_to_image(image,y)
    z_img = zad5.pixels_to_image(image,z)
    z2 = quantizate_z(z_img)
    z = zad5.image_to_pixels(z2)


    yx = differential_encode(y,None)
    cb = zad5.generate_codebook(yx,2**int(sys.argv[2]),0.00001)[3]
    for i in range(len(cb)):
        cb[i] = tuple(cb[i])

    y2 = differential_encode(y,cb)
    y3 = differential_decode(y2)
    y4 = decode(y3, z)
    print("Błąd średniokwadratowy: ", mse(x,y4))
    print("Błąd średniokwadratowy dla R:", mse_color(x,y4,0))
    print("Błąd średniokwadratowy dla G:", mse_color(x,y4,1))
    print("Błąd średniokwadratowy dla B:", mse_color(x,y4,2))

    print("Stosunek sygnału do szumu: ",signal_to_noise(x,y4),'dB')
    y_img = zad5.pixels_to_image(image,y4)
    y_img.show()


