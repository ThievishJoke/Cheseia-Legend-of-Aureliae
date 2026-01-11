import os
import json
from collections import ChainMap
from utility.formatting import Formatting
import re

# ---------------- Configuration ---------------- #
BASE_LANG = "en_us" #default "en_us"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG_ROOT = os.path.join(PROJECT_ROOT, "lang")

# ---------------- Load JSON files ---------------- #
def load_files(folder):
    """Load all JSON files in a folder, returning a dict with namespaced keys."""
    lang_data = {}
    if not os.path.exists(folder):
        return lang_data

    for root, _, files in os.walk(folder):
        for file in files:
            if not file.endswith(".json"):
                continue

            path = os.path.join(root, file)
            with open(path, encoding="utf8") as f:
                content = f.read().strip()
                if not content:
                    print(f"[WARN] Skipping empty JSON file: {path}")
                    continue
                try:
                    data = json.loads(content)
                except json.JSONDecodeError as e:
                    print(f"[ERROR] JSON parse error in {path}: {e}")
                    continue

            # Build namespaced keys: folder/file/key
            rel = os.path.relpath(path, folder)
            namespace = os.path.splitext(file)[0]  # filename without .json
            folder_parts = os.path.relpath(root, folder).split(os.sep)
            folder_parts = [p for p in folder_parts if p != "."]  # skip current dir

            for key, value in data.items():
                namespaced_key = ".".join(folder_parts + [key]) if folder_parts else key
                lang_data[namespaced_key] = value

    return lang_data

# ---------------- Load language with mod support ---------------- #
def load_lang(language):
    """Load the active language with English fallback and mod support."""
    lang_maps = []

    # Base English first for fallback
    lang_maps.append(load_files(os.path.join(LANG_ROOT, BASE_LANG)))

    # Target language override
    if language != BASE_LANG:
        lang_maps.append(load_files(os.path.join(LANG_ROOT, language)))

    # Mods: scan mods/*/localization/<lang>
    mods_dir = os.path.join(PROJECT_ROOT, "mods")
    if os.path.exists(mods_dir):
        for mod_folder in os.listdir(mods_dir):
            for lang in [BASE_LANG, language]:
                mod_path = os.path.join(mods_dir, mod_folder, "localization", lang)
                if os.path.exists(mod_path):
                    lang_maps.append(load_files(mod_path))

    # ChainMap: first maps override later ones
    return ChainMap(*reversed(lang_maps))

# ---------------- Detect available languages ---------------- #
def available_languages():
    langs = []
    if os.path.exists(LANG_ROOT):
        for folder in os.listdir(LANG_ROOT):
            path = os.path.join(LANG_ROOT, folder)
            if os.path.isdir(path):
                langs.append(folder)
    return langs

# ---------------- Active language ---------------- #
ACTIVE_LANG_CODE = "en_us"  # change to e.g., "de_de"
LANG = load_lang(ACTIVE_LANG_CODE)

print(f"Loaded {len(LANG)} keys for {ACTIVE_LANG_CODE}")
print(f"Detected languages: {available_languages()}")

# ---------------- Formatting ---------------- #
FORMAT_MAP = {name: getattr(Formatting, name) for name in dir(Formatting) if name.isupper()}
FORMAT_PATTERN = re.compile(r"\{([A-Z_]+)\}")

def apply_formatting(text):
    return FORMAT_PATTERN.sub(lambda m: FORMAT_MAP.get(m.group(1), m.group(0)), text)

# ---------------- Translation ---------------- #
def translate(key, **kwargs):
    raw = LANG.get(key)

    # fallback to English if key missing
    if raw is None and ACTIVE_LANG_CODE != BASE_LANG:
        english_lang = load_lang(BASE_LANG)
        raw = english_lang.get(key)

    if raw is None:
        print(f"[WARN] Missing translation key: {key}")
        return key

    # --- NEW: handle gender/object selection ---
    if isinstance(raw, dict):
        selector = kwargs.get("gender") or kwargs.get("type") or kwargs.get("variant")
        if selector and selector in raw:
            raw = raw[selector]
        else:
            # fallback to first entry
            raw = next(iter(raw.values()))

    formatted = apply_formatting(raw)

    try:
        return formatted.format(**kwargs)
    except KeyError as e:
        missing = str(e).strip("'")
        print(f"[WARN] Missing variable '{{{missing}}}' in translation key: {key}")
        return formatted

# ---------------- Missing translations helper ---------------- #
def list_missing_translations():
    """List all keys in English that are missing in the active language."""
    english_lang = load_lang(BASE_LANG)
    missing = []
    for key in english_lang.keys():
        if key not in LANG:
            missing.append(key)

    if missing:
        print(f"[INFO] {len(missing)} missing translations in '{ACTIVE_LANG_CODE}':")
        for k in missing:
            print(f" - {k}")
    else:
        print(f"[INFO] No missing translations in '{ACTIVE_LANG_CODE}'.")
    return missing
