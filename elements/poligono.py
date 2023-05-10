from elements.ponto import Ponto
from elements.segReta import SegmentoReta
from itertools import pairwise
from elements.orientacao import calculaExtremo

class Poligono:

	def __init__(self, pontos):
		self.n = len(pontos)
		self.pontos = list(pontos)
		self.lados = [SegmentoReta(p[0], p[1]) for p in pairwise(pontos)] + [SegmentoReta(Ponto(pontos[-1].x, pontos[-1].y), Ponto(pontos[0].x, pontos[0].y))]
					# self.lados = LIST OF SEGMENTS AS FOLLOWS: [(p1,p2), (p2,p3), (p3,p4) ... (pn, p1)] 
		
	def __str__(self):
		return (" -> ".join(str(seg) for seg in pairwise(self.pontos)))
	
	def contem(self, ponto):					# COUNT THE NUMER OF INTERSECTS BETWEEN THE SEGMENT (ponto, maximal) AND THE POLIGON,
		ext = calculaExtremo(self.pontos)		# IF THE COUNT IS ODD, THE POINT IS INSIDE, OTHERWISE, THE POINTS IS OUTSIDE THE POLIGON
		fora = Ponto(ext.x+5543254+2, ext.y+2)
		r = SegmentoReta(fora, ponto)
		c = 0
		for seg in self.lados:
			if r.intercepta(seg):
				c += 1
		return c%2==1



if __name__ == "__main__":
	p, q, r, s = Ponto(0, 0), Ponto(2,0), Ponto(0,2), Ponto(2,2)

	G = Poligono([p,q,r,s])
	print([str(i) for i in G.lados])

	k = Ponto(1,1)
	print(G.contem(k))