#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename: str) -> list[list[int]]:
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        for line in f.readlines():
            clean = line.strip()
            clean = clean.split(';')
            liste = [int(s) for s in clean]
            l.append([liste])
    return l

def get_list_k(data: list[list[int]], k: int) -> list[int]:
    ''' return kth list of list data'''
    return data[k]

def get_first(l):
    ''' return first element of list l'''
    return l[0]

def get_last(l):
    ''' return last element of list l'''
    return l[len(l)]

def get_max(l):
    ''' return max element of list l'''
    return max(l)

def get_min(l):
    ''' return min element of list l'''
    return min(l)

def get_sum(l):
    ''' return sum of list l'''
    return sum(l)


#### Fonction principale


def main():
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
