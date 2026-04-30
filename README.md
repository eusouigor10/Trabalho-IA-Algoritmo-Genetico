# Instância algoritmo genético
Esta é uma implementação de um Algoritmo Genético voltado para a resolução do Problema do Caixeiro Viajante, buscando encontrar rotas otimizadas para visitar um conjunto de pontos e retornar à origem. Trata-se de uma instância não perfeita do algoritmo, o que significa que, embora não garanta encontrar o ótimo global absoluto em todas as execuções, ele apresenta resultados consistentemente próximos do resultado ideal. O sistema mantém uma população estável de 100 indivíduos ao longo das gerações, garantindo uma base genética constante para a evolução das rotas.

## Seleção e elitismo
Para a escolha dos progenitores que darão origem à próxima geração, o algoritmo permite a aplicação de dois métodos distintos: a seleção por roleta, fundamentada na fitness de cada indivíduo, ou a seleção por torneio, que realiza uma disputa direta entre 2 elementos para definir o vencedor. Como forma de proteger as melhores soluções já encontradas, utiliza-se uma estratégia de elitismo que preserva automaticamente os 5 melhores indivíduos de cada ciclo evolutivo.

## Operação genética
As operações genéticas são regidas por probabilidades específicas, sendo definidas em 0.8 para o crossover, 0.1 para a reprodução e 0.1 para a mutação. O processo de crossover é executado através de uma lógica de corte que isola o primeiro e o último quartos do caminho, realizando a troca entre essas partes para compor o novo indivíduo. Este método permite que o descendente herde características estruturais importantes de ambos os pais sem violar a restrição de visitar cada cidade apenas uma vez.

## Evolução da mutação
A lógica de mutação passou por um processo de evolução durante o desenvolvimento do projeto. Originalmente, a operação foi concebida através da troca simples de apenas uma cidade no caminho, evoluindo posteriormente para a troca de duas cidades simultaneamente. Por fim, implementou-se a mutação por inversão, que se mostrou consideravelmente mais eficiente para este problema. Nesta última abordagem, dois pontos do caminho são sorteados e todo o segmento contido entre eles tem sua ordem invertida, o que auxilia o algoritmo a escapar de mínimos locais com maior eficácia.

## Critério de parada
A execução encerra-se quando o sistema detecta que as melhorias tornaram-se insignificantes ou quando atinge um teto de iterações pré-estabelecido. Embora esta abordagem não garanta a perfeição absoluta em todos os cenários, ela é capaz de entregar resultados que se aproximam significativamente do trajeto ideal de forma consistente.
