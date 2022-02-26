# Задание 1

import re


def email_parse(email: str) -> dict:
    """
        Парсит переданную email-строку на атрибуты и возвращает словарь
        :param email: строковое входное значение обрабатываемого email
        :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
        """
    RE_MAIL = re.compile(r"^(?P<username>\w[\w!#$%&'*+/=?^_`{|}~-]*\w)@(?P<domain>\w[\w-]*\w\.\w+)$",
                         re.IGNORECASE | re.ASCII)
    match_email = RE_MAIL.match(email)
    if not match_email:
        raise ValueError(f'wrong email: {email}')
    dict_out = match_email.groupdict()
    return dict_out


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')