def extract_punctuation(input_file, output_file):
    p=".,!?;:—-()[]{}\"'«»…"
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            txt=f.read()
        res=""
        for ch in txt:
            if ch in p:
                res+=ch
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(res)
        print(f"Знаки препинания сохранены в {output_file}")
        print(f"Найдено знаков: {len(res)}")
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
inp=input("Введите имя файла: ")
out=input("Введите имя файла: ")
extract_punctuation(inp, out)
with open(out, 'r', encoding='utf-8') as f:
    c=f.read()
    print(c)
