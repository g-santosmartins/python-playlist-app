# Para a opção 1, peça o título da música, o nome do cantor dessa música e o estilo da música. Não
# permitir cadastrar músicas repetidas, faça a verificação pelo título da música.
# Para a opção 2, faça a busca pelo nome da música e informe se a música está cadastrada ou não,
# mostrando os outros campos. Emita a mensagem de “Música não cadastrada” caso não encontre a
# música.
# Para a opção 3, exiba todos as músicas cadastradas, apresentando o título, o nome do cantor e o
# estilo.
# Para a opção 4, peça ao usuário o nome música, verifique se a música está cadastrada na lista de
# músicas e crie uma lista com as músicas desejadas. Emita a mensagem de “ ́Música não cadastrada”agenda = []
from Musica import Musica
def menu():
    return input('1. Cadastrar\n'
                 '2. Consultar\n'
                 '3. Listar\n'
                 '4. Gerar Playlist por Música\n'
                 '5. Gerar Playlist por Cantor\n'
                 '6. Encerrar\n'
                 'Opção >> ')
# Utils
def buscaMusicaValidar(nome):
  for musica in musicasCadastradas:
    # print(musica)
    nomeEncontrado = musica[0]
    if (nome == nomeEncontrado):
      print("Musica Encontrada")
      return True
    else:
      print("Musica não encontrada")
      return False

def buscaMusica(nome):
  for musica in musicasCadastradas:
    # print(musica)
    nomeEncontrado = musica[0]
    if (nome == nomeEncontrado):
      print("Musica Encontrada")
      return musica
    # else:
    #   print("Musica não encontrada")
      

def buscaAutor(autor):
  for musica in musicasCadastradas:
    autorEncontrado = musica[1]
    # print(autorEncontrado)
    if(autor == autorEncontrado):
      print("Autor Encontrado")
      return musica
    


#Metodos dos sistema
def novo():
  pass

def consultar():
  busca = input("Digite o nome da música>>")
  resultadoDaBusca = buscaMusicaValidar(busca)
  if(resultadoDaBusca):
    print("Música já cadastrada")
    return
  print("Música não cadastrada")

def listar():
  for i in musicasCadastradas:
    print(i)

def gerarPlaylistPorMusica():
  while True:
    querMais = input("Deseja adicionar música? S/N>>")
    busca = input("Digite o nome da Música>>")
    resultadoDaBusca = buscaAutor(busca)
    if(resultadoDaBusca):
      playlistPorMusica.append(resultadoDaBusca)
      faixa("NOSSA PLAYLIST POR MÚSICA")
      for musica in playlistPorMusica:
        print(musica)
    else:
      print("Música não encontrada, tente outra")
     
    if(querMais != "N" or "nao" or "Não" or "Nao" or  "no" or "n" or "No"):
      break

  # for musica in playlistPorMusica:
  #   print(musica)


def gerarPlaylistPorCantor():
  while True:
    querMais = input("Deseja adicionar música? S/N>>")
    busca = input("Digite o nome da Música>>")
    resultadoDaBusca = buscaAutor(busca)
    if(resultadoDaBusca):
      playlistPorMusica.append(resultadoDaBusca)
      faixa("NOSSA PLAYLIST POR Cantor")
      for musica in playlistPorMusica:
        print(musica)
    else:
      print("Música não encontrada, tente outra")
     


def faixa(texto):
    print('<>' * 20)
    print(f'{texto.upper()}'.center(40))
    print('<>' * 20)

playlistPorMusica = []
musicasCadastradas = [
  ["Helpless", "John Mayer", "Blues"],
  ["Helpless", "John Mayer", "Blues"],
  ["Helpless", "John Mayer", "Blues"],
  ["Helpless", "John Mayer", "Blues"],
  ["Helpless", "John Mayer", "Blues"],
  ["Helpless", "John Mayer", "Blues"],
  ["Helpless", "John Mayer", "Blues"],
]

while True:
    faixa('Menu de Opções')
    op = menu()
    if op == '1':
        faixa('Cadastrar nova música>>')
        novo()
    elif op == '2':
        faixa('Consultar música>>')
        consultar()
    elif op == '3':
        faixa('Listar todas as músicas>>')
        listar()
    elif op == '4':
        faixa('Criar playlist por música>>')
        gerarPlaylistPorMusica()
    elif op == '5':
        faixa('Criar uma playlist por cantor>>')
        gerarPlaylistPorCantor()
    elif op == '6':
        break
    else:
        print('Opção inválida!!')