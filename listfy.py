import itertools
import os

# Common suffixes and extra words
common_suffixes = ['123', '1234', '!', '@123', '2024']
common_words = ['password', 'admin', 'qwerty', 'welcome', 'love', 'iloveyou', 'user', 'test']
separators = ['', '_']  # Minimal for speed

leet_map = {'a': '4', 'A': '4', 'e': '3', 'E': '3', 'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}

# === INPUT HELPERS ===

def ask_optional_input(prompt):
    user_input = input(f"{prompt} (Press Enter to skip): ").strip()
    return user_input if user_input else None

def birthdate_variants(birthdate):
    variants = set()
    digits = ''.join(filter(str.isdigit, birthdate))
    if len(digits) == 8:
        day = digits[:2]
        month = digits[2:4]
        year = digits[4:]
        short_year = year[-2:]
        variants.update([day, month, year, short_year, day + month, month + day, day + month + year, year + month + day])
    variants.add(digits)
    return variants

# === MUTATIONS ===

def simple_mutations(word):
    return {word.lower(), word.upper(), word.capitalize()}

def aggressive_uppercase(word):
    """Optimized: Only single uppercase positions"""
    variants = set()
    word = word.lower()
    for p in range(len(word)):
        temp = list(word)
        temp[p] = temp[p].upper()
        variants.add(''.join(temp))
    return variants

def add_symbols(word):
    """Optimized: Only suffix symbols"""
    return {word + sym for sym in common_suffixes}

def leet_mutation(word):
    """Optimized: Replace each char once where possible"""
    variants = set()
    word = list(word)
    for i, char in enumerate(word):
        if char in leet_map:
            temp = word.copy()
            temp[i] = leet_map[char]
            variants.add(''.join(temp))
    return variants

def combine_words_fast(words):
    """Optimized: Only 2-word combos"""
    combined = set()
    for subset in itertools.permutations(words, 2):
        for sep in separators:
            combined.add(sep.join(subset))
    return combined

def apply_suffixes_fast(words):
    result = set()
    for word in words:
        result.add(word)
        for suffix in common_suffixes:
            result.add(word + suffix)
    return result

def append_common_words_fast(words):
    result = set()
    for word in words:
        result.add(word)
        for cw in common_words:
            result.add(word + cw)
    return result

# === CLEAN & STATS ===

def clean_wordlist(input_words, min_len=8, max_len=20):
    cleaned = {pw for pw in input_words if min_len <= len(pw) <= max_len and pw.isascii()}
    return cleaned

def show_stats(input_file):
    count = 0
    lengths = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            pw = line.strip()
            count += 1
            lengths.append(len(pw))
    avg_len = sum(lengths) / count if count else 0
    print(f"\n📊 Stats for {input_file}:")
    print(f"  Total passwords: {count}")
    print(f"  Avg length: {avg_len:.2f}")
    print(f"  Shortest length: {min(lengths) if lengths else 0}")
    print(f"  Longest length: {max(lengths) if lengths else 0}")
    print(f"  File size: {os.path.getsize(input_file)//1024} KB\n")

# === MAIN ===

banner = r"""
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
"""

def main():
    print(banner)
    print("🚀 FAST Rockyou-Style Wordlist Generator (Optimized & Speed Enhanced)")

    name = ask_optional_input("Enter your name")
    surname = ask_optional_input("Enter your surname")
    birth_date = ask_optional_input("Enter your birth date (DDMMYYYY)")
    phone_number = ask_optional_input("Enter your phone number")

    additional_info = []
    while True:
        info = ask_optional_input("Enter additional info (Press Enter to skip)")
        if info:
            additional_info.append(info)
        else:
            break

    raw_inputs = [x for x in [name, surname, phone_number] + additional_info if x]
    if birth_date:
        raw_inputs.extend(birthdate_variants(birth_date))

    if not raw_inputs:
        print("❌ No inputs given. Exiting.")
        return

    print(f"📝 Raw input words count: {len(raw_inputs)}")

    mutated_words = set()
    for word in raw_inputs:
        mutated_words.update(simple_mutations(word))

    uppercase_words = set()
    for word in raw_inputs:
        if len(word) <= 15:
            uppercase_words.update(aggressive_uppercase(word))

    leet_words = set()
    for word in raw_inputs:
        if len(word) <= 15:
            leet_words.update(leet_mutation(word))

    symbol_words = set()
    for word in raw_inputs:
        symbol_words.update(add_symbols(word))

    combined_words = combine_words_fast(mutated_words)

    with_suffix = apply_suffixes_fast(combined_words)
    with_common = append_common_words_fast(with_suffix)

    final_words = mutated_words | uppercase_words | leet_words | symbol_words | combined_words | with_suffix | with_common

    print(f"🔄 Variants before cleaning: {len(final_words)}")

    cleaned_words = clean_wordlist(final_words, min_len=8, max_len=20)

    print(f"💡 Total passwords after cleaning (8-20 chars): {len(cleaned_words)}")

    output_file = input("Enter output filename (default: custom_rockyou.txt): ").strip()
    if not output_file:
        output_file = 'custom_rockyou.txt'

    with open(output_file, 'w', encoding='utf-8') as f:
        for pw in sorted(cleaned_words):
            f.write(pw + '\n')

    print(f"✅ Done! Saved {len(cleaned_words)} passwords to '{output_file}'")
    show_stats(output_file)

if __name__ == "__main__":
    main()
