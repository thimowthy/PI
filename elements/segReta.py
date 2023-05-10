from elements.ponto import Ponto
from elements.orientacao import orientacaoSeg, noSegmento

class SegmentoReta:

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def __str__(self):
		return (str(self.p1) + " -> "+ str(self.p2))

	def intercepta(self, rs):			# CHECKS IF TWO SEGMENTS INTERSECT

		p = self.p1
		q = self.p2
		r = rs.p1
		s = rs.p2
		
		dp = orientacaoSeg(s, p, r)
		dq = orientacaoSeg(s, q, r)
		dr = orientacaoSeg(q, r, p)
		ds = orientacaoSeg(q, s, p)
		
		if not any([not dp, not dq, not ds, not dr]) and (dp!=dq) and (dr!=ds):
			return True
		elif dp == 0 and noSegmento(s,p,r):
			return True
		elif dq == 0 and noSegmento(s,q,r):
			return True
		elif dr == 0 and noSegmento(q,r,p):
			return True
		elif ds == 0 and noSegmento(q,s,p):
			return True
		else:
			return False
		
if __name__ == "__main__":
	rs = SegmentoReta(Ponto(0,0), Ponto(5,5))
	