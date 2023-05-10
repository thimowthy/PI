from elements.ponto import Ponto

def orientacaoSeg(p,q,r=Ponto(0,0)):

	prodVet = -((p.x-r.x)*(q.y-r.y)-(q.x-r.x)*(p.y-r.y))
	if prodVet == 0:
		return 0
	else:
		return 1 if prodVet > 0 else -1

def orientacaoVirada(pq,qr):
	
	p = pq.p1
	q = pq.p2
	r = qr.p2

	return orientacaoSeg(q,r,(p.x,p.y))

def noSegmento(p1,p2,p3):

	if min(p1.x,p3.x) <= p2.x <= max(p1.x,p3.x):
		if min(p1.y,p3.y) <= p2.y <= max(p1.y,p3.y):
			return True
	return False

def calculaExtremo(pontos):							# RETURNS THE POINT WITH THE HIGHEST VALUE OF X (SECOND CRITERIA IS THE HIGHEST VALUE OF Y )
	extremo = pontos[0]

	for i in pontos:
		if i.x > extremo.x:
			extremo = i
		elif i.x == extremo.x and i.y < extremo.y:
			extremo = i
		
	return extremo

def calculaSlope(pontos):
	
	pontos[1].slope = (pontos[1].y-pontos[0].y)/(pontos[1].x-pontos[0].x)
	menor = pontos[1].slope
	for i in range(2,len(pontos)):
		pontos[i].slope = (pontos[i].y-pontos[0].y)/(pontos[i].x-pontos[0].x) if (pontos[i].x-pontos[0].x) else -99999999999999999999
		if pontos[i].slope < menor:
			menor = pontos[i].slope
	
	return menor

def determinante(p1,p2,p3):
	return (p1.x*p2.y + p1.y*p3.x + p2.x*p3.y) - (p2.y*p3.x + p1.x*p3.y + p1.y*p2.x)


if __name__ == "__main__":
	pontos = [(0,0),(10,0),(10,1),(4,1),(4,6),(6,6),(6,3),(10,3),(10,10),(0,10)]
	pontos = [Ponto(x[0],x[1]) for x in pontos]

	#x = Poligono([segReta(p1,p2) for p1,p2 in pairwise(pontos)])
	#print(estaDentro(x, Ponto(5,5)))
	
	p, q, r = Ponto(0, 0), Ponto(2,0), Ponto(0,2)
	print(orientacaoSeg(p, q, r))