def find_folder(stri):
    i = len(stri) - 1
    while i > 0 and stri[i] != "/":
        i -= 1
    return [stri[:i], stri[i:]]