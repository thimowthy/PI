from elements.ponto import Ponto
from elements.orientacao import orientacaoSeg, calculaExtremo

# def calculaExtremo(pontos):
# 	extremo = pontos[0]
# 	for i in pontos:
# 		if i.x > extremo.x:
# 			extremo = i
# 		elif i.x == extremo.x and i.y < extremo.y:
# 			extremo = i

# 	return extremo

def dist(p1, p2):										# RETURNS THE DISTANCE BETWEEN TWO POINTS
	return ((p2.x-p1.x)**2 + (p2.y-p1.y)**2)**0.5

def Jarvis(pontos):										# RETURN THE CONVEX HULL OF A SET OF POINTS
	
	if len(pontos) > 3:
		p = calculaExtremo(pontos)
		envoltoria = [p]
		next = pontos[0]

		while True:
			for ponto in pontos:
				if orientacaoSeg(p, next, ponto) < 0 and ponto != p:
					next = ponto
				elif orientacaoSeg(p, next, ponto) == 0:
					if dist(p, next) < dist(p, ponto):
						next = ponto
			if next == envoltoria[0]:
				break
			envoltoria.append(next)
			p = next

		return envoltoria


if __name__ == "__main__":

	p, q, r = Ponto(0, 0), Ponto(2,0), Ponto(0,2)

	pontos = [(2,2),(3,2),(3,5),(2,4),(2,8),(4,2),(1,6),(5,4),(6,9),(3,3),(1,4),(4,4)]
	pontos = [Ponto(x[0],x[1]) for x in pontos]

	print([str(i) for i in Jarvis(pontos)])
	
	print(orientacaoSeg(p, q, r))