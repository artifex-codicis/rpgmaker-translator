import re
import csv
import shutil
import os
import deepl
def translate_csv():
    filename = input("Enter filename: ")
    api_key = input("Enter api key:")
    try:
      with open(filename,encoding="utf-8") as f:
         rows = list(csv.reader(f,delimiter=";"))
    except FileNotFoundError:
       print(f"File {filename} not found.")
       exit()

    name,ext = os.path.splitext(filename)
    backup_name = name + "_backup" + ext

    if not os.path.exists(backup_name):
        shutil.copy(filename, backup_name)
        print(f"File {backup_name} copied.")

    source = input("From: ").lower()
    target = input("To: ").lower()
    source_col=source.capitalize()
    target_col=target.capitalize()
    def translate(text):
        if not text.strip():
            return text
        codes = []

        def hide(match):
            codes.append(match.group(0))
            return "ZZ%dZZ"  % (len(codes) - 1)


        masked = re.sub(r"\\[A-Za-z]\[\d+\]|%\d+|\\[.|!><^{}]",hide,text)
        try:
           translator =deepl.Translator(api_key)
           result = translator.translate_text(masked,target_lang= target.upper()).text
        except Exception as e:
           print(e)
           return text
        for i in range(len(codes)):
            result = result.replace("ZZ%dZZ" % i,codes[i])
        return result


    header = rows[0]
    data = rows[1:]
    try:
       source_text = header.index(source_col)
       target_text = header.index(target_col)
    except ValueError:
        print("Invalid input")
        exit()

    d = 0
    for row in data:
         row[target_text] = translate(row[source_text])
         d = d + 1
         if d % 100 == 0:
             print("done")
    with open (filename,"w",encoding="utf-8",newline="") as f:
        csv.writer(f,delimiter=";").writerows([header]+data)
    print("Готово")