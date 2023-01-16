from math import ceil
while True:
   # Lê o número de palavras do conto, o máximo de linhas por página e o máximo de caracteres por linha
   # Caso não seja possível a leitura, acabaram os casos de teste (EOF)
   try: 
      n, l, c = [int(x) for x in input().split()]
   except: 
      break
   
   # Lê as palavras do conto e armazena somente os tamanhos, que é a informação de interesse
   tamPalavras = [len(x) for x in input().split()]
   
   # Inicia o número de caracteres da linha atual como 0
   caracteres = 0
   # Inicia o total de linhas utilizadas pelo conto como 1
   totalLinhas = 1
   
   # Analise das n palavras
   for i in range(n):
      # Adiciona o tamanho da palavra atual ao total de caracteres da linha atual
      caracteres += tamPalavras[i] 
      # Se o numero de caracteres da linha atual + 1 (referente ao espaço) + o tamanho da pŕoxima palavra
      # for maior que o limite de caracteres por linha
      try:
          if caracteres + 1 + tamPalavras[i+1] > c:
             # Cria-se uma nova linha, acrescendo em 1 a variável
             totalLinhas += 1
             # Zera o total de caractéres da linha atual
             caracteres = 0
          # Se não for o caso, adiciona mais um caracter para a linha atual, referente ao espaço
          else: 
             caracteres += 1
      # Se for levantado o erro, significa que a útlima palavra já foi analisada e não existe uma próxima
      except:
          break
   
   # Ao final da análise, é apresentado o teto da divisão entre o total de linhas utilizados pelo conto e
   # O número máximo de linhas por página, resultando no total de páginas utilizadas
   print(ceil(totalLinhas / l))
