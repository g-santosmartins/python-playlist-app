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
    nomeEncontrado = musica[2]
    if (nome == nomeEncontrado):
      return True
    else:
      return False

def buscaMusica(nome):
  for musica in musicasCadastradas:
    # print(musica)
    nomeEncontrado = musica[2]
    if (nome == nomeEncontrado):
      print("Musica Encontrada")
      return musica
    # else:
    #   print("Musica não encontrada")
      

def buscaAutor(autor):
  listaMesmoAutor = []
  for musica in musicasCadastradas:
    autorEncontrado = musica[1]
    # print(autorEncontrado)
    if(autor == autorEncontrado):
      print("Autor Encontrado")
      listaMesmoAutor.append(musica)
  return listaMesmoAutor
    

#Metodos dos sistema
def novo():
  newmctitulo= input('informe o titulo da musica >>')
  newmccantor= input('informe o cantor da musica >>')
  newmcestilo= input('informe o estilo da musica >>')

  newmc = Musica(newmcestilo,newmccantor,newmctitulo)
  if(consultar(newmc.titulo)==1):
    return
  else:
    musicasCadastradas.append([newmc.estilo, newmc.cantor,newmc.titulo ])



def consultar(cns=''):
  if(cns==''):
    busca = input("Digite o nome da música>>")
    resultadoDaBusca = buscaMusicaValidar(busca)
  else:
    resultadoDaBusca = buscaMusicaValidar(cns)

  if(resultadoDaBusca):
    print("Música já cadastrada")
    return 1
  else:
    print("Música não cadastrada")
    return 0

def listar():
  for i in range(0, len(musicasCadastradas)):
    print(musicasCadastradas[i])

def gerarPlaylistPorMusica():
  while True:
    querMais = input("Deseja adicionar música? S ou Enter/N>>")
    if(querMais == "N"
     or querMais == "n"
     or querMais == "Não" 
     or querMais == "nao" 
     or querMais == "não"):
      print("saindo aqui")
      break
    else:
      busca = input("Digite o nome da Música>>")
      resultadoDaBusca = buscaMusica(busca)
      print(resultadoDaBusca)
      if(resultadoDaBusca):
        playlistPorMusica.append(resultadoDaBusca)
        faixa("NOSSA PLAYLIST POR MÚSICA")
        for musica in playlistPorMusica:
          print(musica)
      else:
        print("Música não encontrada, tente outra")
     
  # for musica in playlistPorMusica:
  #   print(musica)


def gerarPlaylistPorCantor():
  while True:
    querMais = input("Deseja adicionar música? S ou Enter/N>>")
    if(querMais == "N"
     or querMais == "n"
     or querMais == "Não" 
     or querMais == "nao" 
     or querMais == "não"):
      print("saindo aqui")
      break
    busca = input("Digite o nome do Autor>>")
    resultadoDaBusca = buscaAutor(busca)
    print(resultadoDaBusca)
    if(resultadoDaBusca):
      playlistPorAutor.append(resultadoDaBusca)
      faixa("NOSSA PLAYLIST POR Cantor")
      for musica in playlistPorAutor:
        print(musica)
    else:
      print("Música não encontrada, tente outra")
     

def faixa(texto):
    print('<>' * 20)
    print(f'{texto.upper()}'.center(40))
    print('<>' * 20)

# data to be set
playlistPorMusica = []
playlistPorAutor = []
musicasCadastradas=[]

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