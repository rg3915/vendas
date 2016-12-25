from urllib.request import urlopen


def get_data(url):
    response = urlopen(url)
    return response.read().decode('utf-8')


def save_data(nome_arquivo, resultado):
    open(nome_arquivo, 'w', enconding='utf-8').write(resultado)


def update_file(nome_arquivo, resultado):
    open(nome_arquivo, 'a', enconding='utf-8').write(resultado)
