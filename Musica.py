# Implemente uma classe Música que contenha o título, cantor, estilo e os métodos:
# • Construtor: que receba os valores dos atributos por parâmetro
# • Exibir: que deverá retornar uma string com todas as informações da música.

class Musica:
  def __init__(self, titulo, cantor, estilo) -> None:
       self.estilo = estilo
       self.cantor = cantor 
       self.titulo = titulo

  def __str__(self):
    return f'Titulo{self.titulo} - Cantor: {self.cantor} - Estilo: {self.cantor}'
      