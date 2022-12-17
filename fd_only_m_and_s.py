def format_duration(seconds: int) -> str:
    result = "now"
    if seconds:
        if seconds >= 60:
            m, s = divmod(seconds, 60)
            m_text = str(m) + ' minute' if str(m).endswith('1') else str(m) + ' minutes'
            s_text = ''
            if s:
                s_text = ' and ' + str(s) + (' second' if str(s).endswith('1') else ' seconds')
            result = m_text + s_text
        else:
            s_text = str(seconds) + ' second' if str(seconds).endswith('1') else str(seconds) + ' seconds'
            result = s_text

    return result


print(format_duration(0))
print(format_duration(10))
print(format_duration(60))
print(format_duration(75))
print(format_duration(120))
print(format_duration(130))
