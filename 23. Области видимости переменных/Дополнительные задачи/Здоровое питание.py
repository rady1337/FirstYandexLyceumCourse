food = {    "жирное": (["масло", "фри", "сало", "бургер",                "гамбургер", "салаты с майонезом", "шпроты"]),    "сладкое": ["шоколад", "чай", "сахар", "мёд", "печенье", "торт", "пирожное"],    "мучное": ["пирожки", "хлеб", "пончики", "оладьи", "булочки", "сухарики"],    "диетическое": ["фрукты", "творог", "овощи", "ягоды", "каша", "зелень", "рис"]}def diet(eats: str):    eats = eats.split(', ')    count = len(list(filter(lambda x: x in food["диетическое"], eats)))    if count >= len(eats) // 2:        return "Так держать, Воин Дракона!"    return "Не ешь столько, По!"