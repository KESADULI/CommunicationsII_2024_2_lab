import numpy as np
from gnuradio import gr

class blk (gr.sync_block ):

	def __init__ ( self ): # only default arguments here
		gr.sync_block.__init__(
			self,
			name =" Promedios_de_tiempos ", # will show up in GRC
			in_sig =[ np.float32 ],
			out_sig =[ np.float32]
		)
		self.acum_anterior = 0
		self.Ntotales = 0
		self.acum_anterior1 = 0
		self.cum_anterior2 = 0

	def work (self , input_items , output_items ):
		x = input_items[0] # Senial de entrada .
		y0 = output_items[0] # Promedio de la senial
		
		# Calculo del promedio
		N = len(x)
		self.Ntotales = self.Ntotales + N
		acumulado = self.acum_anterior + np.cumsum(x)
		self.acum_anterior = acumulado[N -1]	
		y0[:]= acumulado/self.Ntotales
		
		return y0
