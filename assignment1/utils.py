def remove_emptys(in_list):
    return filter(len, filter(None, in_list))

def cleaned_text(text):
    if ';' in text:
        print('Terminator: ;')
    return text.replace(" ", '').replace(';', '').replace('"', '').replace("'", '')