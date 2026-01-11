import json, os

def collect(folder):
    data = {}
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file), encoding="utf8") as f:
                    data.update(json.load(f))
    return data

en = collect("localization/en_us")

def check_lang(lang):
    other = collect(f"localization/{lang}")
    missing = [k for k in en if k not in other]
    
    if missing:
        print(f"\nMissing keys for {lang}:")
        for k in missing:
            print("  •", k)
    else:
        print(f"No missing keys for {lang} ✅")

# check all languages
for lang in os.listdir("localization"):
    if lang != "en_us":
        check_lang(lang)