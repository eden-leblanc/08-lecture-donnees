"""
Module de lecture et de manipulation de données.
Contient la fonction read_data() pour lire un fichier CSV
et des fonctions pour manipuler des listes numériques.
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename: str):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            clean = line.strip().split(';')
            liste = []
            for s in clean:
                s = s.strip()
                if s:
                    liste.append(int(s))
            l.append(liste)
    return l

def get_list_k(data: list[list[int]], k: int) -> list[int]:
    ''' return kth list of list data'''
    return data[k]

def get_first(l):
    ''' return first element of list l'''
    if l:
        return l[0]
    return None

def get_last(l):
    ''' return last element of list l'''
    if l:
        return l[-1]
    return None

def get_max(l):
    ''' return max element of list l'''
    if l:
        return max(l)
    return None


def get_min(l):
    ''' return min element of list l'''
    if l:
        return min(l)
    return None

def get_sum(l):
    ''' return sum of list l'''
    return sum(l)


#### Fonction principale


def main():
    '''function main'''
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
