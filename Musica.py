# Implemente uma classe Música que contenha o título, cantor, estilo e os métodos:
# • Construtor: que receba os valores dos atributos por parâmetro
# • Exibir: que deverá retornar uma string com todas as informações da música.

class Musica:
  def __init__(self, estilo, cantor, titulo) -> None:
       self.estilo = estilo
       self.cantor = cantor 
       self.titulo = titulo

  def __str__(self):
    return f'Estilo: {self.estilo} - Cantor: {self.cantor} - Titulo{self.titulo}'
      