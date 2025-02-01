import sys
import colorama
from colorama import Fore, Style

# Initialize colorama for Windows compatibility
colorama.init()

# Dictionary of Python keywords and their Hausa translations
hausa_keywords = {
    "False": "Karya",
    "None": "Babu",
    "True": "Gaskiya",
    "and": "da",
    "as": "kamar",
    "assert": "tabbatar",
    "async": "aiki lokaci guda",
    "await": "jira",
    "break": "karya",
    "class": "aji",
    "continue": "ci gaba",
    "def": "ayyana",
    "del": "share",
    "elif": "idan ba haka ba",
    "else": "in ba haka ba",
    "except": "banda",
    "finally": "a ƙarshe",
    "for": "don",
    "from": "daga",
    "global": "na duniya",
    "if": "idan",
    "import": "shigo da",
    "in": "a ciki",
    "is": "shine/itace",
    "lambda": "aikin mara suna",
    "nonlocal": "ba na gida ba",
    "not": "ba",
    "or": "ko",
    "pass": "wuce",
    "raise": "taso/kafa",
    "return": "mayar",
    "try": "gwada",
    "while": "yayin da",
    "with": "tare da",
    "yield": "bayar"
}

def translate_keywords(keywords):
    """Translate a list of Python keywords to Hausa."""
    translations = []
    for keyword in keywords:
        translation = hausa_keywords.get(keyword, f"{Fore.RED}Keyword '{keyword}' not found.{Style.RESET_ALL}")
        translations.append(f"{Fore.GREEN}{keyword}{Style.RESET_ALL} – {translation}")
    return translations

def main():
    print(f"{Fore.CYAN}Hausa Python Keywords CLI{Style.RESET_ALL}")
    print("Enter Python keywords separated by spaces to get their Hausa translations.")
    print(f"Type {Fore.YELLOW}'exit'{Style.RESET_ALL} to quit or {Fore.YELLOW}'save'{Style.RESET_ALL} to store results in a file.")

    translations_history = []

    while True:
        user_input = input("\nEnter keywords: ").strip()

        if user_input.lower() == "exit":
            print(f"{Fore.MAGENTA}Exiting...{Style.RESET_ALL}")
            sys.exit()

        if user_input.lower() == "save":
            with open("translations.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(translations_history))
            print(f"{Fore.BLUE}Translations saved to 'translations.txt'.{Style.RESET_ALL}")
            continue

        keywords = user_input.split()
        translations = translate_keywords(keywords)

        for translation in translations:
            print(translation)
            translations_history.append(translation)

if __name__ == "__main__":
    main()
