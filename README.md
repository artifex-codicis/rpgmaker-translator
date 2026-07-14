# rpgmaker-translator
Automated translation tool for RPG Maker games (CSV &amp; JSON) with code protection
# RPG Maker Translator

Automated translation tool for RPG Maker games. Extracts text, translates it, and writes it back — **without breaking control codes, file names, or plugin tags**.

## Features

- **Two formats supported:** Hendrix Localization CSV and raw RPG Maker JSON files
- **Full text coverage:** dialogue (codes 401/405), choices (102), database (item/skill descriptions, actor names/profiles), and System.json interface (menu commands, terms, battle text)
- **Control code protection:** masks `\C[3]`, `%1`, `\N[1]`, `\V[10]` and other codes so the translator can't corrupt them
- **Safe by design:** never touches file names, switch/variable labels, or plugin note tags — so the game keeps working
- **Automatic backup** of the entire data folder before translating
- **Error handling:** skips broken files instead of crashing the whole run
- **DeepL powered** for higher quality (Google Translate fallback available)

## Requirements

- Python 3.x
- Libraries: `deepl`, `deep-translator`
- A DeepL API key (free tier available at deepl.com)

Install dependencies:

## Usage

Run the main script:
It will ask:
1. **Format** — `csv` or `json`
2. **Source / target language** — e.g. `en` → `ru`
3. **Folder path** (JSON) or **file path** (CSV) of the game data
4. **DeepL API key**

The tool creates a backup, translates all text, protects control codes, and writes the result back.

## Important note

Machine translation produces a **draft**. For languages with complex grammar (like Russian), the output still needs human post-editing for correct declensions, gender, and text that fits the message window. This tool handles the technical heavy lifting — extraction, code protection, and reassembly — so a human editor can focus on polishing the text.

## License

MIT — free to use and modify.
