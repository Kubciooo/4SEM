import math
from functools import reduce
from collections import defaultdict
from PIL import Image
import sys


_size_data = 0
_dim = 0


def image_to_pixels(image):
    "funkcja zwracająca listę pixeli obrazu"
    result = []
    for y in range(image.height):
        for x in range(image.width):
            (r,g,b) = image.getpixel((x,y))
            result.append((r,g,b))
    return result


def pixels_to_image(image, data):
    "funkcja zamieniająca listę pixeli na obraz o rozmiarach podanego"
    im = image.copy() 
    i = 0 
    for y in range(image.height):
        for x in range(image.width):
            (r,g,b) = data[i]
            i+=1
            im.putpixel((x,y),(int(r),int(g),int(b)))
    return im

def generate_codebook(data, size_codebook, epsilon = 0.00001):
    "funkcja generująca codebook rozmiaru <size_codebook> ze zbieżnością <epsilon>"
    global _size_data, _dim
    _size_data = len(data) # wielkość całego obrazu
    _dim = len(data[0]) # RGB - 3 
    codebook = []
    error = 0
    average_vector = average_vector_of_vectors(data, _dim, _size_data)
    codebook.append(average_vector)
    closest_code_list = []
    average_distance = avg_distortion_c0(average_vector,data)    
    while len(codebook) < size_codebook: 
        codebook, average_distance,closest_code_list, error = split_codebook(data, codebook, epsilon, average_distance)
    
    return closest_code_list, avg_distortion_c_list(closest_code_list, data), error, codebook


def split_codebook(data, codebook, epsilon, initial_average_distance):
    """Funkcja, która tworzy nowy codebook długości 2 razy większej od podanego codebooka.
       Każdy kod w codebooku zamieniamy na (kod+epsilon) i (kod-epsilon) i potem je optymalizujemy 
    """
    print("Aktualny rozmiar codebooka: ",len(codebook))
    print("="*100)
    global _size_data, _dim
    new_codevectors = []
    for code in codebook: 
        code1 = create_new_codevector(code,epsilon) 
        code2 = create_new_codevector(code, -epsilon)
        new_codevectors.extend((code1,code2))
    average_distance = 0 
    error = epsilon + 1
    codebook = new_codevectors
    num_iter  = 0
    while error > epsilon:
        print(f"iteracja numer {num_iter} o errorze {error}")
        # szukamy najbliższego wektora z codebook do naszego wektora z data
        closest_code_list = [None] * _size_data
        vectors_near_code = defaultdict(list)
        vector_indexes_near_code = defaultdict(list)
        for i, vector in enumerate(data): # dla każdego wektora w data szukamy najbliższego wektora z naszego słownika do niego 
            min_dist = None
            closest_code_index = None
            for i_c, code in enumerate(codebook): 
                d = euclid_squared(vector, code)  # d = odległość wektora z data do wektora z codebook 
                if min_dist is None or min_dist > d:  # min_dist to najmniej odległy wektor z codebook do aktualnego wektora z data 
                    min_dist = d
                    closest_code_list[i] = code
                    closest_code_index = i_c
            vectors_near_code[closest_code_index].append(vector) #dodajemy wektor z data do listy najbliższych wektorów wektora z codebooka 
            vector_indexes_near_code[closest_code_index].append(i) #dodajemy indeks wektora z data, aby móc potem się do niego odnieść

        for i in range(len(codebook)):
            vectors = vectors_near_code.get(i) or []
            if len(vectors) > 0: 
                new_center = average_vector_of_vectors(vectors, _dim) #teraz każdy wektor "v" z codebook ma być średnim wektorem z wektorów z data, których najbliższym z codebook jest "v" 
                codebook[i] = new_center #nadpisujemy nowym wektorem 
                for j in vector_indexes_near_code[i]:
                    closest_code_list[j] = new_center #teraz nadpisujemy wyjściową tablicę wektórów z data(bierzemy te najbliżej "v") naszym nowym wektorem "v"
        previous_average_distance = average_distance if average_distance > 0 else initial_average_distance  #sprawdzamy błąd
       # print(closest_code_list)
        average_distance = avg_distortion_c_list(closest_code_list, data) 
        error = (previous_average_distance - average_distance) / previous_average_distance
        num_iter += 1

    print("*"*100)
    print("Zawartość codebooka:")
    print(codebook)
    #print(closest_code_list)
    print("*"*100)
    return codebook, average_distance, closest_code_list, error



def avg_distortion_c0(c0, data, size=None):
    "średnie zniekształcenie podstawowego obrazu - średnią odległość między wektorami z data, a początkowym średnim wektorem 'c0'"
    size = size or _size_data
    return reduce(lambda s, d:  s + d / size,(euclid_squared(c0, vec)for vec in data),0.0)   

def avg_distortion_c_list(c_list, data, size=None):
    "Funckja zwracająca stosunek sygnału do szumu"
    size = size or _size_data
    return reduce(lambda s, d:  s + d / size,(euclid_squared(c_i, data[i]) for i, c_i in enumerate(c_list)),0.0)



def create_new_codevector(code_vector, moving_factor):
    return [x * (1.0+moving_factor) for x in code_vector]

def euclid_squared(a, b):
    return sum((x_a - x_b) ** 2 for x_a, x_b in zip(a, b))

def average_vector_of_vectors(vectors, dim=None, size = None):
    "funkcja wyliczająca średni wektor"
    s = size or len(vectors)
    d = dim or len(vectors[0])
    average_vector = [0.0] * d
    for v in vectors:
        for i, x in enumerate(v):
            average_vector[i] += x / s
    
    return average_vector


 
if __name__ == "__main__":
    im = Image.open(sys.argv[1])
    x = image_to_pixels(im)
    #print(x)
    (a,b,c,d) = generate_codebook(x,2**int(sys.argv[3]))
    if int(sys.argv[3]) == 0: 
        a = [d[0] for i in range(len(x))]
        b = avg_distortion_c_list(a, x) 
        c = 0.00001
    im2 = pixels_to_image(im,a)
    print("_"*100)
    print("Błąd średniokwadratowy: ",c)
    print("stosunek sygnału do szumu:", 1/b)
    im2.save(sys.argv[2])
    im2.show()
