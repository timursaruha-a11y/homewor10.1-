from datetime import datetime

# Импортируем твои существующие функции маскировки.
# Обрати внимание: так как widget и masks лежат в одной папке src,
# импорт будет выглядеть так:
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info_string: str) -> str:
    """
    Обрабатывает строку с типом и номером карты или счета.
    Возвращает строку с замаскированным номером.
    """
    # Разделяем строку на части по пробелу.
    # Например: "Visa Platinum 7000792289606361" -> ["Visa", "Platinum", "7000792289606361"]
    parts = info_string.split()

    # Последний элемент списка - это всегда номер
    number = parts[-1]

    # Все, что до номера - это название (Visa Platinum, Maestro, Счет и т.д.)
    # Соединяем обратно через пробел
    name = " ".join(parts[:-1])

    # Проверяем, является ли номер номером счета.
    # Обычно номера счетов длинные (20 цифр), а карты - 16.
    # Но лучше ориентироваться на слово "Счет" в названии, как в примере.
    if "Счет" in name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку в формате "ДД.ММ.ГГГГ".
    """
    # Преобразуем строку в объект datetime
    # fromisoformat отлично справляется с форматом ISO 8601
    date_obj = datetime.fromisoformat(date_string)

    # Форматируем в нужный вид
    return date_obj.strftime("%d.%m.%Y")