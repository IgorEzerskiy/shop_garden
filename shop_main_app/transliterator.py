ukrainian_to_english = {
    'а': 'a', 'б': 'b',
    'в': 'v', 'г': 'h',
    'д': 'd', 'е': 'e',
    'є': 'ye', 'ж': 'zh',
    'з': 'z', 'и': 'y',
    'і': 'i', 'ї': 'yi',
    'й': 'y', 'к': 'k',
    'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r',
    'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f',
    'х': 'kh', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ь': '',
    'ю': 'yu', 'я': 'ya',
    'ґ': 'g',
}


def transliterate_ua_to_en(text):
    lower_text = text.lower().strip()
    transliterated_text = ''

    for char in lower_text:
        if char in ukrainian_to_english:
            transliterated_text += ukrainian_to_english[char]
        else:
            transliterated_text += char

    return transliterated_text
