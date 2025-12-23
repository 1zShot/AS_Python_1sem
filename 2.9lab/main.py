def read_matrices_from_file(filename):
    mats = []
    try:
        with open(filename, 'r') as f:
            l = f.readlines()
            idx = 0
            while idx < len(l):
                if not l[idx].strip():
                    idx += 1
                    continue
                rows, cols = map(int, l[idx].strip().split())
                mat = []
                for j in range(idx + 1, idx + 1 + rows):
                    r = list(map(int, l[j].strip().split()))
                    mat.append(r)               
                mats.append((rows, cols, mat))
                idx += rows + 1                
    except FileNotFoundError:
        print(f"Файл не найден!")
        return None
    except Exception as err:
        print(f"Ошибка при чтении файла: {err}")
        return None
    
    return mats

def write_matrices_to_file(filename, mats):
    try:
        with open(filename, 'w') as f:
            for rows, cols, mat in mats:
                f.write(f"{rows} {cols}\n")
                for r in mat:
                    f.write(" ".join(map(str, r)) + "\n")
    except Exception as err:
        print(f"Ошибка при записи в файл: {err}")

def print_file_content(filename):
    try:
        with open(filename, 'r') as f:
            txt = f.read()
            print(txt)
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")

def swap_odd_matrices(file1, file2):
    mats1 = read_matrices_from_file(file1)
    mats2 = read_matrices_from_file(file2)
    if mats1 is None or mats2 is None:
        return False
    min_cnt = min(len(mats1), len(mats2))
    swapped = 0
    for k in range(0, min_cnt, 2):
        mats1[k], mats2[k] = mats2[k], mats1[k]
        swapped += 1
    write_matrices_to_file(file1, mats1)
    write_matrices_to_file(file2, mats2)
    return True
name1 = input("\nВведите имя первого файла): ").strip()
name2 = input("Введите имя второго файла): ").strip()
print_file_content(name1)
print_file_content(name2)
if swap_odd_matrices(name1, name2):
    print("ПОСЛЕ ОБМЕНА:")
    print_file_content(name1)
    print_file_content(name2)
    print("победа")
else:
    print("ошибока")
