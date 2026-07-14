from translator_json import translate_json
from translator_csv import translate_csv




choice = input("csv/json: ").lower()
if choice == "json":
        translate_json()
elif choice == "csv":
        translate_csv()
else:
        print("Please enter a valid choice.")