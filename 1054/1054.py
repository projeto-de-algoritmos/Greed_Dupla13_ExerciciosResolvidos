def maiorPulo(pedras):
	pulo, nPedras = 0, len(pedras)
	for i in range(nPedras):
	    # Se não é a última pedra e a próxima pedra é grande
		if i+1 < nPedras and pedras[i+1][0] == 'B':
			# O pulo vai ser o máximo entre ele e a distancia da próxima pedra menos a distancia da pedra atual
			pulo = max(pulo, pedras[i+1][1] - pedras[i][1])
		# Se não for a penúltima pedra
		elif i+2 < nPedras:
			# O pulo vai ser o máximo entre ele e a distancia da segunda pedra próxima menos a distancia da pedra atual
			pulo = max(pulo, pedras[i+2][1] - pedras[i][1])
		
		# Se não for a penultima pedra e a segunda pedra seguinte é grande
		if i+2 < nPedras and pedras[i+2][0] == 'B':
			# O pulo vai ser o máximo entre ele e a distancia da próxima pedra menos a distancia da pedra seguinte
			pulo = max(pulo, pedras[i+2][1] -  pedras[i+1][1])
		# Se não for a antepenultima pedra
		elif i+3 < nPedras:
		    # O pulo vai ser o máximo entre ele e a distancia da terceira pedra próxima menos a distancia da próxima pedra
			pulo = max(pulo, pedras[i+3][1] -  pedras[i+1][1]) 
	return pulo

# Lẽ o número de casos de teste e executa o for T vezes
T = int(input())
for caso in range(T):
    # Lê o número de pedras e a distância entre a margem esquerda e direita
	N, D = (int(n) for n in input().split())
	# Lê a descrição das N pedras
	entrada = [pedra for pedra in input().split()]
	
	# Adiciona uma pedra grande na lista de pedras representando a margem esquerda
	pedras = [['B', 0]]
	
	for pedra in entrada:
	    # Adiciona cada pedra como uma lista [tipo, distancia] à lista de pedras
	    pedras.append([pedra[0], int(pedra[2:])])
	
	# Adiciona uma pedra grande ao final representando a margem direita    
	pedras.append(['B', D])
	
	# Apresenta o maior pulo do sapo
	print('Case %d: %d' % (caso+1, maiorPulo(pedras)))
