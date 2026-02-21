from pathlib import Path
import json

def create_json(exp_name: str):
    cardList = []
    try:
        with open(f"expansion_info/textFiles/{exp_name}.txt",'r', encoding="utf-8") as f:
            for line in f:
                number, name, rarity = line.strip().split(',')

                cardList.append({
                    "name": name.strip(),
                    "number": number.strip(),
                    "rarity": rarity.strip()
                })
    except FileNotFoundError:
        try:
            open(f"expansion_info/jsonFiles/{exp_name}")
        except FileNotFoundError:
            raise FileNotFoundError("No such files exist for that set")
        return
    with open(f"expansion_info/jsonFiles/{exp_name}.json", 'w', encoding='utf-8') as f:
        json.dump(cardList, f, indent=4, ensure_ascii=False)


folder = Path("expansion_info/textFiles")

for file in folder.iterdir():
    expansion_name = file.name.split('.')[0] # first bit of the file (black_bolt)
    create_json(expansion_name)
