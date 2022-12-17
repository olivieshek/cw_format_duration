def format_duration(seconds: int) -> str:
    result = "now"
    if seconds:
        # больше 0 => НЕ сейчас
        m, s = divmod(seconds, 60)  # считаем минуты и секунды
        if m >= 60:
            # есть часы
            ...
        elif m:
            # есть минуты
            m_text = str(m) + ' minute' if str(m).endswith('1') else str(m) + ' minutes'
            s_text = ''
            if s:
                s_text = ' and ' + str(s) + (' second' if str(s).endswith('1') else ' seconds')
            result = m_text + s_text
        else:
            # есть секунды
            s_text = str(seconds) + ' second' if str(seconds).endswith('1') else str(seconds) + ' seconds'
            result = s_text

    return result


print(format_duration(0))
print(format_duration(1))
print(format_duration(59))
print(format_duration(60))
print(format_duration(61))
