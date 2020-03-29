import os 
import sys
def rename_files(root, items):              
    for filename in items:              
        try:
            os.rename( os.path.join(root,filename), os.path.join(root, filename.lower())) #zmienia nazwe pliku, path.join to pełna ścieżka do pliku/katalogu
        except OSError:
            pass

def lowercase_rename(dir):
    for root, dirs, files in os.walk(dir, topdown=False): #walk przechodzi od tego folderu w dół (można powiedzieć, że root to korzeń drzewa)
        rename_files(root, dirs)                          #do tego walk wypisuje nam wszystkie nazwy aktualnych folderów i folderów i plików w nich
        rename_files(root, files)                         #topdown - chcemy zmieniać nazwy plików od końca, czyli najpierw w najniższym folderze, potem tym wyżej, itd.


k = sys.argv
if len(k) != 2: 
    print("Niepoprawny format wejściowy")
else:
    lowercase_rename(k[1])
