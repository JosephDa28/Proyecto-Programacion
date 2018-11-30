from math import *

import sys

#Tupla con nombres de las estaciones y sus respectivas coordenadas geograficas
rutas = (("Calle26", (4.617126, -74.071939)), ("Profamilia", (4.621319, -74.069789)), ("Avenida39", (4.627178, -74.068641)), ("Calle45", (4.632655, -74.067666)), ("Marly", (4.636969, -74.066865)), ("Calle57", (4.643053, -74.065801)), ("Calle63", (4.649191, -74.064731)), ("Flores", (4.654843, -74.063077)), ("Calle72", (4.658098, -74.062120)), ("Calle76", (4.663326, -74.061221)), ("Heroes", (4.668309, -74.060212)), ("Calle85", (4.671860, -74.059724)), ("Virrey", (4.676202, -74.058983)), ("Calle100", (4.685606, -74.057353)), ("Calle106", (4.692131, -74.056339)), ("PepeSierra", (4.698403, -74.055299)), ("Calle127", (4.705319, -74.054134)), ("Prado", (4.714349, -74.052605)), ("Alcala", (4.720781, -74.051531)), ("Calle142", (4.726377, -74.050614)), ("Calle146", (4.731601, -74.049726)), ("Mazuren", (4.734492, -74.049245)), ("CardioInfantil", (4.742144, -74.047965)), ("Toberin", (4.746806, -74.047176)), ("PortalNorte", (4.754229, -74.046133)), ("Calle187", (4.763601, -74.044363)), ("Terminal", (4.768818, -74.043506)))


#Tupla con nombres de las estaciones y sus respectivas coordenadas geograficas pero al reves
rutasInversas =  (("Terminal", (4.768818, -74.043506)), ("Calle187", (4.763601, -74.044363)), ("PortalNorte", (4.754229, -74.046133)), ("Toberin", (4.746806, -74.047176)), ("CardioInfantil", (4.742144, -74.047965)), ("Mazuren", (4.734492, -74.049245)), ("Calle146", (4.731601, -74.049726)), ("Calle142", (4.726377, -74.050614)), ("Alcala", (4.720781, -74.051531)), ("Prado", (4.714349, -74.052605)), ("Calle127", (4.705319, -74.054134)), ("PepeSierra", (4.698403, -74.055299)), ("Calle106", (4.692131, -74.056339)), ("Calle100", (4.685606, -74.057353)), ("Virrey", (4.676202, -74.058983)), ("Calle85", (4.671860, -74.059724)), ("Heroes", (4.668309, -74.060212)), ("Calle76", (4.663326, -74.061221)), ("Calle72", (4.658098, -74.062120)), ("Flores", (4.654843, -74.063077)), ("Calle63", (4.649191, -74.064731)), ("Calle57", (4.643053, -74.065801)), ("Marly", (4.636969, -74.066865)), ("Calle45", (4.632655, -74.067666)), ("Avenida39", (4.627178, -74.068641)), ("Profamilia", (4.621319, -74.069789)), ("Calle26", (4.617126, -74.071939)))


#Tupla con nombres de los buses que plantea Guillermo Ramirez y sus respectivas paradas
Buses_Guillermo_Ramirez= (("bus8", {"Calle26":"Vagon1", "Profamilia":"Vagon2", "Avenida39":"Vagon1", "Calle45":"Vagon2", "Marly":"Vagon2", "Calle57":"Vagon3", "Calle63":"Vagon1", "Flores":"Vagon1", "Calle72":"Vagon3", "Calle76":"Vagon2", "Heroes":"Vagon2", "Calle85":"Vagon2", "Virrey":"Vagon2", "Calle100":"Vagon1", "Calle106":"Vagon1", "PepeSierra":"Vagon1", "Calle127":"Vagon1", "Prado":"Vagon2", "Alcala":"Vagon2", "Calle142":"Vagon1", "Calle146":"Vagon1", "Mazuren":"Vagon1", "CardioInfantil":"Vagon2", "Toberin":"Vagon2", "PortalNorte":"Vagon0", "Calle187":"Vagon1", "Terminal":"Vagon1"}), ("busB", {"Calle26":"Vagon2", "Heroes":"Vagon1", "Calle100":"Vagon2", "PortalNorte":"Vagon1"}))




#Lista con las paradas del busB
busB = ["Calle26", "Heroes", "Calle100", "PortalNorte"]

#Lista con las paradas del bus8
bus8 = ["Calle26","Profamilia","Avenida39","Calle45","Marly","Calle57","Calle63","Flores","Calle72","Calle76","Heroes","Calle85","Virrey","Calle100","Calle106","PepeSierra","Prado","Calle127","Alcala","Calle142","Calle146","Mazuren","CardioInfantil","Toberin","PortalNorte","Calle187", "Terminal"]

 





#La funcion Haversine recibe como parametros dos puntos en coordenadas geograficas y saca la distancia entre ellos.

def Haversine (lat1,lon1,lat2,lon2):

	rad = pi/180

	dlat = lat2-lat1

	dlon = lon2-lon1

	R = 6372.795477598

	a = ((sin(rad*dlat/2))**2) + (((cos(rad*lat1))*(cos(rad*lat2))*(sin(rad*dlon/2))**2))

	distancia = 2*R*(asin(sqrt(a)))

	return(distancia)



def Prueba():

	Lista_De_Error = []

	ParadasEnComun = []

	Lista_Rutas_Primer_Elemento = []

	Lista_Rutas_Inversas_Primer_Elemento = []

	Tupla_Coordenadas_Estaciones = []

	Lista_Coordenadas_Estaciones = []

	Lista_De_Error_Buses = []

	Lista_De_Error1 = []

	lista = []



	for i in rutas:

		Lista_Rutas_Primer_Elemento.append(i[0])

   


#No deja seguir el programa hasta que el origen que escribe el usuario sea correcto    

	while True:

		print("Escriba su estacion de origen todo en pegado y con la primera en mayuscula")

		

		origen = (str(input("Escriba su estacion de origen: ")))	

		

		if origen in Lista_Rutas_Primer_Elemento:

				break

	

	

#No deja seguir el programa hasta que el destino que escribe el usuario sea correcto

	while True:



		print("Escriba su estacion de destino todo en pegado y con la primera en mayuscula")

		

		destino = (str(input("Escriba su estacino de destino: ")))

		

		if destino in Lista_Rutas_Primer_Elemento:

				break



	
#Sugiere una ruta directa
	for i in Buses_Guillermo_Ramirez:

		if origen in i[1] and destino in i[1]:

			Lista_De_Error1.append(i[0])



	print("Si desea tomar una ruta directa desde su origen y destino le recomendamos los siguientes buses: {0}".format(Lista_De_Error1))




#Lista con todos los buses para crear un posible error
	for i in Buses_Guillermo_Ramirez:

		Lista_De_Error.append(i[0])




#No deja seguir el programa hasta que el bus escogido pare en el origen y sea correctamente escrito 
	

	while True:

		bus = (str(input("Escriba el bus que desea tomar: ")))

		if bus not in Lista_De_Error:

			print("Escriba el bus que desea tomar como se muestra en este ejemplo; busB") 



		if bus in Lista_De_Error:

			break

	

	

	

#---------------- SI EL USUARIO ESCOGE EL BUS 8 ENTONCES CALCULA EL VIAJE DESDE EL ORIGEN HASTA EL DESTINO CON LAS PARADAS DEL BUS 8 CON SU RESPECTIVO TIEMPO ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	if bus == "bus8":



		Tiempo_Sumado_Por_Los_Transbordo = 0

		Distancia_Sumada_Por_Los_Transbordo = 0


#Considera los dos casos en donde el usuario va del norte al sur o del sur al norte, dependiendo de ello crea una lista con las coordenadas ordenadas desde el origen hasta el destino 
		posicionOrigen = Lista_Rutas_Primer_Elemento.index(origen)

		posicionDestino = Lista_Rutas_Primer_Elemento.index(destino)



		if posicionOrigen < posicionDestino:

		

			for i in Lista_Rutas_Primer_Elemento:

				if i == origen:

					s = Lista_Rutas_Primer_Elemento.index(i)

		            

			for i in Lista_Rutas_Primer_Elemento:

				if i == destino:

					b = Lista_Rutas_Primer_Elemento.index(i)

		                

			ListaDeTuplas_Origen_Destino = list(rutas[s:b+1])

		        

			for i in ListaDeTuplas_Origen_Destino:

				Tupla_Coordenadas_Estaciones.append(i[1])



			for i in Tupla_Coordenadas_Estaciones:

				for z in i:

					Lista_Coordenadas_Estaciones.append(z)

		            



		if posicionDestino < posicionOrigen:

		    

			for i in rutasInversas:

				Lista_Rutas_Inversas_Primer_Elemento.append(i[0])



			for i in Lista_Rutas_Inversas_Primer_Elemento:

				if i == origen:

					s = Lista_Rutas_Inversas_Primer_Elemento.index(i)



			for i in Lista_Rutas_Inversas_Primer_Elemento:

				if i == destino:

					b = Lista_Rutas_Inversas_Primer_Elemento.index(i)



			ListaDeTuplas_Origen_Destino = list(rutasInversas[s:b+1])

		        

			for i in ListaDeTuplas_Origen_Destino:

				Tupla_Coordenadas_Estaciones.append(i[1])

		            

			for i in Tupla_Coordenadas_Estaciones:

				for z in i:

					Lista_Coordenadas_Estaciones.append(z)

		print("Tome el bus 8 hasta  {0}".format(destino))



#------------------- SI EL USUARIO ESCOGE EL BUS B ENTONCES CALCULA EL VIAJE DESDE EL ORIGEN HASTA LA ESTACION MAS CERCANA EN DONDE PARA EL BUS B   ---------------------------------



	if bus == "busB":



#------------------- SI EL ORIGEN Y EL DESTINO ESTAN EN LAS ESTACIONES EN LAS QUE PARA EL BUS B ENTONCES CALCULA LA DISTANCIA DESDE EL ORIGEN AL DESTINO TOMANDO LAS PARADAS DEL BUS B CON SU RESPECTIVO TIEMPO  -------------------------------------------------------------------------------------------------------------------------------------------------------------------



		if origen in busB and destino in busB:

			Tiempo_Sumado_Por_Los_Transbordo = 0

			Distancia_Sumada_Por_Los_Transbordo = 0

			posicionOrigen = Lista_Rutas_Primer_Elemento.index(origen)

			posicionDestino = Lista_Rutas_Primer_Elemento.index(destino)





			if posicionOrigen < posicionDestino :



				for i in Lista_Rutas_Primer_Elemento:

					if i == origen:

						s = Lista_Rutas_Primer_Elemento.index(i)

				    

				for i in Lista_Rutas_Primer_Elemento:

					if i == destino:

						b = Lista_Rutas_Primer_Elemento.index(i)

				        

				ListaDeTuplas_Origen_Destino = list(rutas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])



				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)

			



			if posicionDestino < posicionOrigen :

		

				for i in rutasInversas:

					Lista_Rutas_Inversas_Primer_Elemento.append(i[0])



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == origen:

						s = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == destino:

						b = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				ListaDeTuplas_Origen_Destino = list(rutasInversas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])

				    

				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)

				

			print("Tome el bus B hasta {0}".format(destino))

	

			

#------------------- SI EL ORIGEN Y EL DESTINO NO ESTAN EN LAS PARADAS DEL BUS B ENTONCES CALCULA DESDE EL ORIGEN A LA ESTACION MAS CERCANA EN LA QUE PARA EL BUS B, ASI MISMO, COMO EL DESTINO TAMPOCO ESTA EN LAS PARADAS DEL BUS B, ENTONCES CALCULA LA ESTACION MAS CERCANA DESDE EL DESTINO -------------------------------------------------------------------------------------

		

		if origen not in busB and destino not in busB:



#-- CALCULA LA DISTANCIA Y EL TIEMPO QUE SE TARDA DESDE EL ORIGEN HASTA LA ESTACION MAS CERCANA EN LA QUE PARA EL BUS B PARA QUE DESDE AHI TOME EL BUS 8 Y PUEDA LLEGAR A SU NUEVO ORIGEN EN EL CUAL TOMARA EL BUS B ------------------------------------------------------------------------------------------------------------------------------------------------------------------

	

			amigos = []

			jiji = []

			jojo = []

			blabla = []

			mm = []

			




#Calcula las posiciones del origen y de todas las estaciones en donde para el busB			

			for i in rutas:

				if i[0] == origen:

					PosicionOrigen = rutas.index(i)

				if i[0] == "Calle26":

					PosicionCalle26 = rutas.index(i)

				if i[0] == "Heroes":

					PosicionHeroes = rutas.index(i)

				if i[0] == "Calle100":

					PosicionCalle100 = rutas.index(i)

				if i[0] == "PortalNorte":

					PosicionPortalNorte = rutas.index(i)


#Considera los casos para poder determinar una tupla con las coordenadas y estaciones 

			Ruta1 = list(rutas[ PosicionCalle26 : PosicionOrigen + 1])



			if PosicionOrigen < PosicionHeroes:

				Ruta2 = list(rutas[ PosicionOrigen : PosicionHeroes  + 1])



			if PosicionOrigen > PosicionHeroes:

				Ruta2 = list(rutas[ PosicionHeroes : PosicionOrigen + 1])



			if PosicionOrigen < PosicionCalle100:

				Ruta3 = list(rutas[ PosicionOrigen : PosicionCalle100  + 1])



			if PosicionOrigen > PosicionCalle100:

				Ruta3 = list(rutas[ PosicionCalle100 : PosicionOrigen + 1])



			if PosicionOrigen < PosicionPortalNorte:

				Ruta4 = list(rutas[ PosicionOrigen : PosicionPortalNorte  + 1])

		

			if PosicionOrigen > PosicionPortalNorte:

				Ruta4 = list(rutas[ PosicionPortalNorte : PosicionOrigen + 1])



			Coordenadas_Ruta1 = []

			Coordenadas_Ruta2 = []

			Coordenadas_Ruta3 = []

			Coordenadas_Ruta4 = []


#Crea una lista con las coordenadas desde el origen a cada estacion en donde para el bus B para poder determinar su trayecto
			for i in Ruta1:

				for m in i[1]:

					Coordenadas_Ruta1.append(m)



			for i in Ruta2:

				for m in i[1]:

					Coordenadas_Ruta2.append(m)



			for i in Ruta3:

				for m in i[1]:

					Coordenadas_Ruta3.append(m)



			for i in Ruta4:

				for m in i[1]:

					Coordenadas_Ruta4.append(m)


#Calcula la distancia y el tiempo de trayecto desde el origen hasta cada punto, en donde para el bus B y los guarda en las respectivas variables 
			
			a = 0

			b = 1

			c = 2

			d = 3

			p = int(len(Coordenadas_Ruta1))

			m = (p//2)-1

			k = 0

			velocidad = 45

			r = 0

			tiempo = 30

			for i in range(m):

				t = Haversine(float(Coordenadas_Ruta1[a]),float(Coordenadas_Ruta1[b]),float(Coordenadas_Ruta1[c]),float(Coordenadas_Ruta1[d]))

				a += 2

				b += 2

				c += 2

				d += 2

				k += t

				q = t/velocidad

				r += q

				w = (Coordenadas_Ruta1[a] , Coordenadas_Ruta1[b])

				for i in Ruta1:

					if w == i[1]:

						if  i[0] in bus8:

							tiempo += 45

	

			n = tiempo/60

			s = r*60

			Tiempo_Origen_Calle26 = n + s

			Distancia_Origen_Calle26 = k

			

			

			a1 = 0

			b1 = 1

			c1 = 2

			d1 = 3

			p1 = int(len(Coordenadas_Ruta2))

			m1 = (p1//2)-1

			k1 = 0

			r1 = 0

			tiempo1 = 30

			for i in range(m1):

				t1 = Haversine(float(Coordenadas_Ruta2[a1]),float(Coordenadas_Ruta2[b1]),float(Coordenadas_Ruta2[c1]),float(Coordenadas_Ruta2[d1]))

				a1 += 2

				b1 += 2

				c1 += 2

				d1 += 2

				k1 += t1

				q1 = t1/velocidad

				r1 += q1

				w1 = (Coordenadas_Ruta2[a1] , Coordenadas_Ruta2[b1])

				for i in Ruta2:

					if w1 == i[1]:

						if  i[0] in bus8:

							tiempo1 += 45

	

			n1 = tiempo1/60

			s1 = r1*60

			Tiempo_Origen_Heroes = n1 + s1

			Distancia_Origen_Heroes = k1

			

			a2 = 0

			b2 = 1

			c2 = 2

			d2 = 3

			p2 = int(len(Coordenadas_Ruta3))

			m2 = (p2//2)-1

			k2 = 0

			r2 = 0

			tiempo2 = 30

			for i in range(m2):

				t2 = Haversine(float(Coordenadas_Ruta3[a2]),float(Coordenadas_Ruta3[b2]),float(Coordenadas_Ruta3[c2]),float(Coordenadas_Ruta3[d2]))

				a2 += 2

				b2 += 2

				c2 += 2

				d2 += 2

				k2 += t2

				q2 = t2/velocidad

				r2 += q2

				w2 = (Coordenadas_Ruta3[a2] , Coordenadas_Ruta3[b2])

				for i in Ruta3:

					if w2 == i[1]:

						if  i[0] in bus8:

							tiempo2 += 45

	

			n2 = tiempo2/60

			s2 = r2*60

			Tiempo_Origen_Calle100 = n2 + s2

			Distancia_Origen_Calle100 = k2



			a3 = 0

			b3 = 1

			c3 = 2

			d3 = 3

			p3 = int(len(Coordenadas_Ruta4))

			m3 = (p3//2)-1

			k3 = 0

			r3 = 0

			tiempo3 = 30

			for i in range(m3):

				t3 = Haversine(float(Coordenadas_Ruta4[a3]),float(Coordenadas_Ruta4[b3]),float(Coordenadas_Ruta4[c3]),float(Coordenadas_Ruta4[d3]))

				a3 += 2

				b3 += 2

				c3 += 2

				d3 += 2

				k3 += t3

				q3 = t3/velocidad

				r3 += q3

				w3 = (Coordenadas_Ruta4[a3] , Coordenadas_Ruta4[b3])

				for i in Ruta4:

					if w3 == i[1]:

						if  i[0] in bus8:

							tiempo3 += 45

	

			n3 = tiempo3/60

			s3 = r3*60

			Tiempo_Origen_PortalNorte = n3 + s3

			Distancia_Origen_PortalNorte = k3



			ddd = []

	
#Guarda todas las distancias y los tiempos en dos distintas listas

			jojo.append(Tiempo_Origen_Calle26)

			jojo.append(Tiempo_Origen_Heroes)

			jojo.append(Tiempo_Origen_Calle100)

			jojo.append(Tiempo_Origen_PortalNorte)



			ddd.append(Distancia_Origen_Calle26)

			ddd.append(Distancia_Origen_Heroes)

			ddd.append(Distancia_Origen_Calle100)

			ddd.append(Distancia_Origen_PortalNorte)

	

			c = list(zip(busB, ddd))

			b = list(zip(busB, jojo))



			Lista_Estaciones_Cercanas_Tiempo = []

			Lista_Estaciones_Cercanas_Distancia = []


#Calcula las menores destincias y los menores tiempos para determinar cuales son las estaciones mas cercanas en las que para el bus B al destino 
			for i in b:

				if i[1] == min(jojo):

					Lista_Estaciones_Cercanas_Tiempo.append(i)

					jojo.remove(i[1])

					b.remove(i)





			for x in b:

				if x[1] == min(jojo):

					Lista_Estaciones_Cercanas_Tiempo.append(x)

					jojo.remove(x[1])

					b.remove(x)



#Crea una lista con las estaciones mas cercanas al origen

			for i in c:

				if i[1] == min(ddd):

					Lista_Estaciones_Cercanas_Distancia.append(i)

					ddd.remove(i[1])

					c.remove(i)





			for x in c:

				if x[1] == min(ddd):

					Lista_Estaciones_Cercanas_Distancia.append(x)

					ddd.remove(x[1])

					c.remove(x)

			

			hhh = []

			kkk = []

			mmm = []



			for i in rutas:

				if destino == i[0]:

					hhh.append(i[1])



			for i in rutas:		

				for j in busB:

					if i[0] == j:

						hhh.append(i[1])



			for i in hhh:

				for m in i:

					kkk.append(m)

		
#Calcula la estacion mas cercana en la que para el bus B al destino 
			C = 2

			D = 3

			J = int(len(kkk))

			M = (J//2)-1

			for i in range(M):

				Dist = Haversine(float(kkk[0]),float(kkk[1]),float(kkk[C]),float(kkk[D]))

				C += 2

				D += 2

				mmm.append(Dist) 

		

			Union = list(zip(busB, mmm))



			for i in Union:

				if i[1] == min(mmm):

					Estacion_Mas_Cercana_Al_Destino = str(i[0])



		

		
#Crea un Nuevo Origen posible para calcular el transbordo 


			for i in rutas:

				if i[0] == Lista_Estaciones_Cercanas_Tiempo[0][0]:

					Posicion_Posible_Origen_Nuevo1 = rutas.index(i)



				if i[0] == Lista_Estaciones_Cercanas_Tiempo[1][0]:

					Posicion_Posible_Origen_Nuevo2 = rutas.index(i)

		

				if i[0] == Estacion_Mas_Cercana_Al_Destino:

					Posicion_Estacion_Mas_Cercana_Al_Destino = rutas.index(i)

			

#Si la posicion del origen nuevo es igual a la del posible origen nuevo  				

			if Posicion_Posible_Origen_Nuevo1 != Posicion_Estacion_Mas_Cercana_Al_Destino and Posicion_Posible_Origen_Nuevo2 != Posicion_Estacion_Mas_Cercana_Al_Destino:



				if Posicion_Posible_Origen_Nuevo1 < Posicion_Estacion_Mas_Cercana_Al_Destino:

					Ruta_Posible1 = list(rutas[ Posicion_Posible_Origen_Nuevo1 : Posicion_Estacion_Mas_Cercana_Al_Destino  + 1])



				if Posicion_Estacion_Mas_Cercana_Al_Destino < Posicion_Posible_Origen_Nuevo1:

					Ruta_Posible1 = list(rutas[ Posicion_Estacion_Mas_Cercana_Al_Destino : Posicion_Posible_Origen_Nuevo1  + 1])



				if Posicion_Posible_Origen_Nuevo2 < Posicion_Estacion_Mas_Cercana_Al_Destino:

					Ruta_Posible2 = list(rutas[ Posicion_Posible_Origen_Nuevo2 : Posicion_Estacion_Mas_Cercana_Al_Destino  + 1])



				if Posicion_Estacion_Mas_Cercana_Al_Destino < Posicion_Posible_Origen_Nuevo2:

					Ruta_Posible2 = list(rutas[ Posicion_Estacion_Mas_Cercana_Al_Destino : Posicion_Posible_Origen_Nuevo2 + 1])

				

				Coordenadas_Ruta_Posible1 = []

				Coordenadas_Ruta_Posible2 = []



				for i in Ruta_Posible1:

					for m in i[1]:

						Coordenadas_Ruta_Posible1.append(m)



				for i in Ruta_Posible2:

					for m in i[1]:

						Coordenadas_Ruta_Posible2.append(m)

			

				

				a4 = 0

				b4 = 1

				c4 = 2

				d4 = 3

				p4 = int(len(Coordenadas_Ruta_Posible1))

				m4 = (p4//2)-1

				k4 = 0

				r4 = 0

				tiempo4 = 30

				for i in range(m4):

					t4 = Haversine(float(Coordenadas_Ruta_Posible1[a4]),float(Coordenadas_Ruta_Posible1[b4]),float(Coordenadas_Ruta_Posible1[c4]),float(Coordenadas_Ruta_Posible1[d4]))

					a4 += 2

					b4 += 2

					c4 += 2

					d4 += 2

					k4 += t4

					q4 = t4/velocidad

					r4 += q4

					w4 = (Coordenadas_Ruta_Posible1[a4] , Coordenadas_Ruta_Posible1[b4])

					for i in Ruta_Posible1:

						if w4 == i[1]:

							if  i[0] in busB:

								tiempo4 += 45

	

				n4 = tiempo4/60

				s4 = r4*60

				Tiempo_Ruta_Posible1 = n4 + s4



				a5 = 0

				b5 = 1

				c5 = 2

				d5 = 3

				p5 = int(len(Coordenadas_Ruta_Posible2))

				m5 = (p5//2)-1

				k5 = 0

				r5 = 0

				tiempo5 = 30

				for i in range(m5):

					t5 = Haversine(float(Coordenadas_Ruta_Posible2[a5]),float(Coordenadas_Ruta_Posible2[b5]),float(Coordenadas_Ruta_Posible2[c5]),float(Coordenadas_Ruta_Posible2[d5]))

					a5 += 2

					b5 += 2

					c5 += 2

					d5 += 2

					k5 += t5

					q5 = t5/velocidad

					r5 += q5

					w5 = (Coordenadas_Ruta_Posible2[a5] , Coordenadas_Ruta_Posible2[b5])

					for i in Ruta_Posible2:

						if w5 == i[1]:

							if  i[0] in busB:

								tiempo5 += 45

	

				n5 = tiempo5/60

				s5 = r5*60

				Tiempo_Ruta_Posible2 = n5 + s5



				Tiempo_Total_Ruta_Origen_Nuevo1 = Tiempo_Ruta_Posible1 + float(Lista_Estaciones_Cercanas_Tiempo[0][1])

				Tiempo_Total_Ruta_Origen_Nuevo2 = Tiempo_Ruta_Posible2 + float(Lista_Estaciones_Cercanas_Tiempo[1][1])

				

				

			

			

			

		

				if Tiempo_Total_Ruta_Origen_Nuevo1 < Tiempo_Total_Ruta_Origen_Nuevo2:

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[0][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[0][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[0][1])

					



				else:

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[1][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[1][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[1][1])	

					

			

			else: 

			

				if (Posicion_Posible_Origen_Nuevo1 == Posicion_Estacion_Mas_Cercana_Al_Destino): 

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[1][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[1][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[1][1])

					

				if (Posicion_Posible_Origen_Nuevo2 == Posicion_Estacion_Mas_Cercana_Al_Destino):

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[0][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[0][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[0][1])

					



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

			



			for i in rutas:

				if i[0] == destino:

					PosicionDestino = rutas.index(i)

				

			

			Ruta1_Destino = list(rutas[ PosicionCalle26 : PosicionDestino + 1])



			if PosicionDestino < PosicionHeroes:

				Ruta2_Destino = list(rutas[ PosicionDestino : PosicionHeroes  + 1])



			if PosicionDestino > PosicionHeroes:

				Ruta2_Destino = list(rutas[ PosicionHeroes : PosicionDestino + 1])



			if PosicionDestino < PosicionCalle100:

				Ruta3_Destino = list(rutas[ PosicionDestino : PosicionCalle100  + 1])



			if PosicionDestino > PosicionCalle100:

				Ruta3_Destino = list(rutas[ PosicionCalle100 : PosicionDestino + 1])



			if PosicionDestino < PosicionPortalNorte:

				Ruta4_Destino = list(rutas[ PosicionDestino : PosicionPortalNorte  + 1])

		

			if PosicionDestino > PosicionPortalNorte:

				Ruta4_Destino = list(rutas[ PosicionPortalNorte : PosicionDestino + 1])



			Coordenadas_Ruta1_Destino = []

			Coordenadas_Ruta2_Destino = []

			Coordenadas_Ruta3_Destino = []

			Coordenadas_Ruta4_Destino = []



			for i in Ruta1_Destino:

				for m in i[1]:

					Coordenadas_Ruta1_Destino.append(m)



			for i in Ruta2_Destino:

				for m in i[1]:

					Coordenadas_Ruta2_Destino.append(m)



			for i in Ruta3_Destino:

				for m in i[1]:

					Coordenadas_Ruta3_Destino.append(m)



			for i in Ruta4_Destino:

				for m in i[1]:

					Coordenadas_Ruta4_Destino.append(m)





			

			A = 0

			B = 1

			C = 2

			D = 3

			P = int(len(Coordenadas_Ruta1_Destino))

			M = (P//2)-1

			K = 0

			R = 0

			TIEMPO = 30

			for i in range(M):

				T = Haversine(float(Coordenadas_Ruta1_Destino[A]),float(Coordenadas_Ruta1_Destino[B]),float(Coordenadas_Ruta1_Destino[C]),float(Coordenadas_Ruta1_Destino[D]))

				A += 2

				B += 2

				C += 2

				D += 2

				K += T

				Q = T/velocidad

				R += Q

				W = (Coordenadas_Ruta1_Destino[A] , Coordenadas_Ruta1_Destino[B])

				for i in Ruta1_Destino:

					if W == i[1]:

						if  i[0] in bus8:

							TIEMPO += 45

	

			N = TIEMPO/60

			S = R*60

			Tiempo_Destino_Calle26 = N + S

			Distancia_Destino_Calle26 = K



			A1 = 0

			B1 = 1

			C1 = 2

			D1 = 3

			P1 = int(len(Coordenadas_Ruta2_Destino))

			M1 = (P1//2)-1

			K1 = 0

			R1 = 0

			TIEMPO1 = 30

			for i in range(M1):

				T1 = Haversine(float(Coordenadas_Ruta2_Destino[A1]),float(Coordenadas_Ruta2_Destino[B1]),float(Coordenadas_Ruta2_Destino[C1]),float(Coordenadas_Ruta2_Destino[D1]))

				A1 += 2

				B1 += 2

				C1 += 2

				D1 += 2

				K1 += T1

				Q1 = T1/velocidad

				R1 += Q1

				W1 = (Coordenadas_Ruta2_Destino[A1] , Coordenadas_Ruta2_Destino[B1])

				for i in Ruta2_Destino:

					if W1 == i[1]:

						if  i[0] in bus8:

							TIEMPO1 += 45

	

			N1 = TIEMPO1/60

			S1 = R1*60

			Tiempo_Destino_Heroes = N1 + S1

			Distancia_Destino_Heroes = K1



			A2 = 0

			B2 = 1

			C2 = 2

			D2 = 3

			P2 = int(len(Coordenadas_Ruta3_Destino))

			M2 = (P2//2)-1

			K2 = 0

			R2 = 0

			TIEMPO2 = 30

			for i in range(M2):

				T2 = Haversine(float(Coordenadas_Ruta3_Destino[A2]),float(Coordenadas_Ruta3_Destino[B2]),float(Coordenadas_Ruta3_Destino[C2]),float(Coordenadas_Ruta3_Destino[D2]))

				A2 += 2

				B2 += 2

				C2 += 2

				D2 += 2

				K2 += T2

				Q2 = T2/velocidad

				R2 += Q2

				W2 = (Coordenadas_Ruta3_Destino[A2] , Coordenadas_Ruta3_Destino[B2])

				for i in Ruta3_Destino:

					if W2 == i[1]:

						if  i[0] in bus8:

							TIEMPO2 += 45

	

			N2 = TIEMPO2/60

			S2 = R2*60

			Tiempo_Destino_Calle100 = N2 + S2

			Distancia_Destino_Calle100 = K2

			

			A3 = 0

			B3 = 1

			C3 = 2

			D3 = 3

			P3 = int(len(Coordenadas_Ruta4_Destino))

			M3 = (P3//2)-1

			K3 = 0

			R3 = 0

			TIEMPO3 = 30

			for i in range(M3):

				T3 = Haversine(float(Coordenadas_Ruta4_Destino[A3]),float(Coordenadas_Ruta4_Destino[B3]),float(Coordenadas_Ruta4_Destino[C3]),float(Coordenadas_Ruta4_Destino[D3]))

				A3 += 2

				B3 += 2

				C3 += 2

				D3 += 2

				K3 += T3

				Q3 = T3/velocidad

				R3 += Q3

				W3 = (Coordenadas_Ruta4_Destino[A3] , Coordenadas_Ruta4_Destino[B3])

				for i in Ruta4_Destino:

					if W3 == i[1]:

						if  i[0] in bus8:

							TIEMPO3 += 45

	

			N3 = TIEMPO3/60

			S3 = R3*60

			Tiempo_Destino_PortalNorte = N3 + S3

			Distancia_Destino_PortalNorte = K3

			

			Lista_Distancias = []

			Lista_Tiempos = [] 

	

			Lista_Tiempos.append(Tiempo_Destino_Calle26)

			Lista_Tiempos.append(Tiempo_Destino_Heroes)

			Lista_Tiempos.append(Tiempo_Destino_Calle100)

			Lista_Tiempos.append(Tiempo_Destino_PortalNorte)



			Lista_Distancias.append(Distancia_Destino_Calle26)

			Lista_Distancias.append(Distancia_Destino_Heroes)

			Lista_Distancias.append(Distancia_Destino_Calle100)

			Lista_Distancias.append(Distancia_Destino_PortalNorte)

	

			C = list(zip(busB, Lista_Distancias))

			B = list(zip(busB, Lista_Tiempos))



			Lista_Estaciones_Cercanas_Destino_Tiempo = []

			Lista_Estaciones_Cercanas_Destino_Distancia = []



			for i in B:

				if i[1] == min(Lista_Tiempos):

					Lista_Estaciones_Cercanas_Destino_Tiempo.append(i)

					Lista_Tiempos.remove(i[1])

					B.remove(i)





			for x in B:

				if x[1] == min(Lista_Tiempos):

					Lista_Estaciones_Cercanas_Destino_Tiempo.append(x)

					Lista_Tiempos.remove(x[1])

					B.remove(x)





			for i in C:

				if i[1] == min(Lista_Distancias):

					Lista_Estaciones_Cercanas_Destino_Distancia.append(i)

					Lista_Distancias.remove(i[1])

					C.remove(i)





			for x in C:

				if x[1] == min(Lista_Distancias):

					Lista_Estaciones_Cercanas_Destino_Distancia.append(x)

					Lista_Distancias.remove(x[1])

					C.remove(x)

			



			for i in rutas:

				if i[0] == Lista_Estaciones_Cercanas_Destino_Tiempo[0][0]:

					Posicion_Posible_Destino_Nuevo1 = rutas.index(i)



				if i[0] == Lista_Estaciones_Cercanas_Destino_Tiempo[1][0]:

					Posicion_Posible_Destino_Nuevo2 = rutas.index(i)

		

				if i[0] == origenNuevo:

					Posicion_origenNuevo = rutas.index(i)



			



				

			

			if Posicion_Posible_Destino_Nuevo1 != Posicion_origenNuevo and Posicion_Posible_Destino_Nuevo2 != Posicion_origenNuevo:



				if Posicion_Posible_Destino_Nuevo1 < Posicion_origenNuevo:

					Ruta_Posible_Destino1 = list(rutas[ Posicion_Posible_Destino_Nuevo1 : Posicion_origenNuevo + 1])



				if Posicion_origenNuevo < Posicion_Posible_Destino_Nuevo1:

					Ruta_Posible_Destino1 = list(rutas[ Posicion_origenNuevo : Posicion_Posible_Destino_Nuevo1 + 1])



				if Posicion_Posible_Destino_Nuevo2 < Posicion_origenNuevo:

					Ruta_Posible_Destino2 = list(rutas[ Posicion_Posible_Destino_Nuevo2 : Posicion_origenNuevo + 1])



				if Posicion_origenNuevo < Posicion_Posible_Destino_Nuevo2:

					Ruta_Posible_Destino2 = list(rutas[ Posicion_origenNuevo : Posicion_Posible_Destino_Nuevo2 + 1])



		

				Coordenadas_Ruta_Destino_Posible1 = []

				Coordenadas_Ruta_Destino_Posible2 = []



				for i in Ruta_Posible_Destino1:

					for m in i[1]:

						Coordenadas_Ruta_Destino_Posible1.append(m)



				for i in Ruta_Posible_Destino2:

					for m in i[1]:

						Coordenadas_Ruta_Destino_Posible2.append(m)

			



				A4 = 0

				B4 = 1

				C4 = 2

				D4 = 3

				P4 = int(len(Coordenadas_Ruta_Destino_Posible1))

				M4 = (P4//2)-1

				K4 = 0

				R4 = 0

				TIEMPO4 = 30

				for i in range(M4):

					T4 = Haversine(float(Coordenadas_Ruta_Destino_Posible1[A4]),float(Coordenadas_Ruta_Destino_Posible1[B4]),float(Coordenadas_Ruta_Destino_Posible1[C4]),float(Coordenadas_Ruta_Destino_Posible1[D4]))

					A4 += 2

					B4 += 2

					C4 += 2

					D4 += 2

					K4 += T4

					Q4 = T4/velocidad

					R4 += Q4

					W4 = (Coordenadas_Ruta_Destino_Posible1[A4] , Coordenadas_Ruta_Destino_Posible1[B4])

					for i in Ruta_Posible_Destino1:

						if W4 == i[1]:

							if  i[0] in busB:

								TIEMPO4 += 45

	

				N4 = TIEMPO4/60

				S4 = R4*60

				Tiempo_Ruta_Destino_Posible1 = N4 + S4



				A5 = 0

				B5 = 1

				C5 = 2

				D5 = 3

				P5 = int(len(Coordenadas_Ruta_Destino_Posible2))

				M5 = (P5//2)-1

				K5 = 0

				R5 = 0

				TIEMPO5 = 30

				for i in range(M5):

					T5 = Haversine(float(Coordenadas_Ruta_Destino_Posible2[A5]),float(Coordenadas_Ruta_Destino_Posible2[B5]),float(Coordenadas_Ruta_Destino_Posible2[C5]),float(Coordenadas_Ruta_Destino_Posible2[D5]))

					A5 += 2

					B5 += 2

					C5 += 2

					D5 += 2

					K5 += T5

					Q5 = T5/velocidad

					R5 += Q5

					W5 = (Coordenadas_Ruta_Destino_Posible2[A5] , Coordenadas_Ruta_Destino_Posible2[B5])

					for i in Ruta_Posible_Destino2:

						if W5 == i[1]:

							if  i[0] in busB:

								TIEMPO5 += 45

	

				N5 = TIEMPO5/60

				S5 = R5*60

				Tiempo_Ruta_Destino_Posible2 = N5 + S5



				Tiempo_Total_Ruta_Destino_Nuevo1 = Tiempo_Ruta_Destino_Posible1 + float(Lista_Estaciones_Cercanas_Destino_Tiempo[0][1])

				Tiempo_Total_Ruta_Destino_Nuevo2 = Tiempo_Ruta_Destino_Posible2 + float(Lista_Estaciones_Cercanas_Destino_Tiempo[1][1])



			

			

				if Tiempo_Total_Ruta_Destino_Nuevo1 < Tiempo_Total_Ruta_Destino_Nuevo2:

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[0][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[0][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[0][1])



				else:

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[1][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[1][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[1][1])





			else:

			

				if (Posicion_Posible_Destino_Nuevo1 == Posicion_origenNuevo): 

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[1][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[1][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[1][1])



				if (Posicion_Posible_Destino_Nuevo2 == Posicion_origenNuevo):

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[0][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[0][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[0][1])



		



			Tiempo_Sumado_Por_Los_Transbordo = Tiempo_Origen_origenNuevo + Tiempo_DestinoNuevo_Destino

			Distancia_Sumada_Por_Los_Transbordo = Distancia_Origen_origenNuevo + Distancia_DestinoNuevo_Destino



	



		

#---------------------------------------------------------------------------- TOMA EN CUENTA LOS SIGUIENTES CASOS  --------------------------------------------------------------------------

			

			posicionOrigenNuevo = Lista_Rutas_Primer_Elemento.index(origenNuevo)

			posicionDestinoNuevo = Lista_Rutas_Primer_Elemento.index(DestinoNuevo)

		

			if posicionOrigenNuevo == posicionDestinoNuevo:



				print("Lo mejor es que tome el bus8")

				posicionOrigen = Lista_Rutas_Primer_Elemento.index(origen)

				posicionDestino = Lista_Rutas_Primer_Elemento.index(destino)



				if posicionOrigen < posicionDestino:

				

					for i in Lista_Rutas_Primer_Elemento:

						if i == origen:

							s = Lista_Rutas_Primer_Elemento.index(i)

				

					for i in Lista_Rutas_Primer_Elemento:

						if i == destino:

							b = Lista_Rutas_Primer_Elemento.index(i)

						

					ListaDeTuplas_Origen_Destino = list(rutas[s:b+1])

					

					for i in ListaDeTuplas_Origen_Destino:

						Tupla_Coordenadas_Estaciones.append(i[1])



					for i in Tupla_Coordenadas_Estaciones:

						for z in i:

							Lista_Coordenadas_Estaciones.append(z)

								    

				if posicionDestino < posicionOrigen:

		

					for i in rutasInversas:

						Lista_Rutas_Inversas_Primer_Elemento.append(i[0])



					for i in Lista_Rutas_Inversas_Primer_Elemento:

						if i == origen:

							s = Lista_Rutas_Inversas_Primer_Elemento.index(i)



					for i in Lista_Rutas_Inversas_Primer_Elemento:

						if i == destino:

							b = Lista_Rutas_Inversas_Primer_Elemento.index(i)



					ListaDeTuplas_Origen_Destino = list(rutasInversas[s:b+1])

					

					for i in ListaDeTuplas_Origen_Destino:

						Tupla_Coordenadas_Estaciones.append(i[1])

				

					for i in Tupla_Coordenadas_Estaciones:

						for z in i:

							Lista_Coordenadas_Estaciones.append(z)





				q = 0

				w = 1

				e = 2

				l = 3

				p = int(len(Lista_Coordenadas_Estaciones))

				k = (p//2)-1

				r = 0

				velocidad = 45

				x = 0

				f = 0 

				tiempo = 30

			

				for i in range(k):

					t = Haversine(float(Lista_Coordenadas_Estaciones[q]),float(Lista_Coordenadas_Estaciones[w]),float(Lista_Coordenadas_Estaciones[e]),float(Lista_Coordenadas_Estaciones[l]))

					q += 2

					w += 2

					e += 2

					l += 2

					f += t

					y = t/velocidad

					x += y

					c = (Lista_Coordenadas_Estaciones[q] , Lista_Coordenadas_Estaciones[w])

					for i in ListaDeTuplas_Origen_Destino:

						if c == i[1]:

							if  i[0] in bus8:

								tiempo += 45

			

				n = tiempo/60

				s = x*60

				tiempoTotal = n + s

				print("La distancia a recorrer es {0} y el tiempo aproximado es {1} minutos, sin embargo puede que tomando el bus 8 el tiempo sea menor".format(f, int(tiempoTotal)))

				sys.exit()





			



			if posicionOrigenNuevo < posicionDestinoNuevo :



				for i in Lista_Rutas_Primer_Elemento:

					if i == origenNuevo:

						s = Lista_Rutas_Primer_Elemento.index(i)

				    

				for i in Lista_Rutas_Primer_Elemento:

					if i == DestinoNuevo:

						b = Lista_Rutas_Primer_Elemento.index(i)

				        

				ListaDeTuplas_Origen_Destino = list(rutas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])



				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)

				



			if posicionDestinoNuevo < posicionOrigenNuevo :

		

				for i in rutasInversas:

					Lista_Rutas_Inversas_Primer_Elemento.append(i[0])



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == origenNuevo:

						s = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == DestinoNuevo:

						b = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				ListaDeTuplas_Origen_Destino = list(rutasInversas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])

				    

				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)



			print("Debe ir en un bus 8 hasta {0}, despues tomar el bus B hasta {1} y finalmente tomar el bus 8 hasta {2}, sin embargo puede que tomando el bus 8 el tiempo sea menor".format(origenNuevo, DestinoNuevo, destino))



			

	#-----------------------------------------------------------------------------------------------------------------------------------------------------------	 			



		if origen in busB and destino not in busB:

			

			for i in rutas:

				if i[0] == destino :

					PosicionDestino = rutas.index(i)

				if i[0] == "Calle26":

					PosicionCalle26 = rutas.index(i)

				if i[0] == "Heroes":

					PosicionHeroes = rutas.index(i)

				if i[0] == "Calle100":

					PosicionCalle100 = rutas.index(i)

				if i[0] == "PortalNorte":

					PosicionPortalNorte = rutas.index(i)

				

			

			Ruta1_Destino = list(rutas[ PosicionCalle26 : PosicionDestino + 1])



			if PosicionDestino < PosicionHeroes:

				Ruta2_Destino = list(rutas[ PosicionDestino : PosicionHeroes  + 1])



			if PosicionDestino > PosicionHeroes:

				Ruta2_Destino = list(rutas[ PosicionHeroes : PosicionDestino + 1])



			if PosicionDestino < PosicionCalle100:

				Ruta3_Destino = list(rutas[ PosicionDestino : PosicionCalle100  + 1])



			if PosicionDestino > PosicionCalle100:

				Ruta3_Destino = list(rutas[ PosicionCalle100 : PosicionDestino + 1])



			if PosicionDestino < PosicionPortalNorte:

				Ruta4_Destino = list(rutas[ PosicionDestino : PosicionPortalNorte  + 1])

		

			if PosicionDestino > PosicionPortalNorte:

				Ruta4_Destino = list(rutas[ PosicionPortalNorte : PosicionDestino + 1])



			Coordenadas_Ruta1_Destino = []

			Coordenadas_Ruta2_Destino = []

			Coordenadas_Ruta3_Destino = []

			Coordenadas_Ruta4_Destino = []



			for i in Ruta1_Destino:

				for m in i[1]:

					Coordenadas_Ruta1_Destino.append(m)



			for i in Ruta2_Destino:

				for m in i[1]:

					Coordenadas_Ruta2_Destino.append(m)



			for i in Ruta3_Destino:

				for m in i[1]:

					Coordenadas_Ruta3_Destino.append(m)



			for i in Ruta4_Destino:

				for m in i[1]:

					Coordenadas_Ruta4_Destino.append(m)





			

			A = 0

			B = 1

			C = 2

			D = 3

			P = int(len(Coordenadas_Ruta1_Destino))

			M = (P//2)-1

			K = 0

			R = 0

			TIEMPO = 30

			velocidad = 45

			for i in range(M):

				T = Haversine(float(Coordenadas_Ruta1_Destino[A]),float(Coordenadas_Ruta1_Destino[B]),float(Coordenadas_Ruta1_Destino[C]),float(Coordenadas_Ruta1_Destino[D]))

				A += 2

				B += 2

				C += 2

				D += 2

				K += T

				Q = T/velocidad

				R += Q

				W = (Coordenadas_Ruta1_Destino[A] , Coordenadas_Ruta1_Destino[B])

				for i in Ruta1_Destino:

					if W == i[1]:

						if  i[0] in bus8:

							TIEMPO += 45

	

			N = TIEMPO/60

			S = R*60

			Tiempo_Destino_Calle26 = N + S

			Distancia_Destino_Calle26 = K



			A1 = 0

			B1 = 1

			C1 = 2

			D1 = 3

			P1 = int(len(Coordenadas_Ruta2_Destino))

			M1 = (P1//2)-1

			K1 = 0

			R1 = 0

			TIEMPO1 = 30

			for i in range(M1):

				T1 = Haversine(float(Coordenadas_Ruta2_Destino[A1]),float(Coordenadas_Ruta2_Destino[B1]),float(Coordenadas_Ruta2_Destino[C1]),float(Coordenadas_Ruta2_Destino[D1]))

				A1 += 2

				B1 += 2

				C1 += 2

				D1 += 2

				K1 += T1

				Q1 = T1/velocidad

				R1 += Q1

				W1 = (Coordenadas_Ruta2_Destino[A1] , Coordenadas_Ruta2_Destino[B1])

				for i in Ruta2_Destino:

					if W1 == i[1]:

						if  i[0] in bus8:

							TIEMPO1 += 45

	

			N1 = TIEMPO1/60

			S1 = R1*60

			Tiempo_Destino_Heroes = N1 + S1

			Distancia_Destino_Heroes = K1



			A2 = 0

			B2 = 1

			C2 = 2

			D2 = 3

			P2 = int(len(Coordenadas_Ruta3_Destino))

			M2 = (P2//2)-1

			K2 = 0

			R2 = 0

			TIEMPO2 = 30

			for i in range(M2):

				T2 = Haversine(float(Coordenadas_Ruta3_Destino[A2]),float(Coordenadas_Ruta3_Destino[B2]),float(Coordenadas_Ruta3_Destino[C2]),float(Coordenadas_Ruta3_Destino[D2]))

				A2 += 2

				B2 += 2

				C2 += 2

				D2 += 2

				K2 += T2

				Q2 = T2/velocidad

				R2 += Q2

				W2 = (Coordenadas_Ruta3_Destino[A2] , Coordenadas_Ruta3_Destino[B2])

				for i in Ruta3_Destino:

					if W2 == i[1]:

						if  i[0] in bus8:

							TIEMPO2 += 45

	

			N2 = TIEMPO2/60

			S2 = R2*60

			Tiempo_Destino_Calle100 = N2 + S2

			Distancia_Destino_Calle100 = K2

			

			A3 = 0

			B3 = 1

			C3 = 2

			D3 = 3

			P3 = int(len(Coordenadas_Ruta4_Destino))

			M3 = (P3//2)-1

			K3 = 0

			R3 = 0

			TIEMPO3 = 30

			for i in range(M3):

				T3 = Haversine(float(Coordenadas_Ruta4_Destino[A3]),float(Coordenadas_Ruta4_Destino[B3]),float(Coordenadas_Ruta4_Destino[C3]),float(Coordenadas_Ruta4_Destino[D3]))

				A3 += 2

				B3 += 2

				C3 += 2

				D3 += 2

				K3 += T3

				Q3 = T3/velocidad

				R3 += Q3

				W3 = (Coordenadas_Ruta4_Destino[A3] , Coordenadas_Ruta4_Destino[B3])

				for i in Ruta4_Destino:

					if W3 == i[1]:

						if  i[0] in bus8:

							TIEMPO3 += 45

	

			N3 = TIEMPO3/60

			S3 = R3*60

			Tiempo_Destino_PortalNorte = N3 + S3

			Distancia_Destino_PortalNorte = K3

			

			Lista_Distancias = []

			Lista_Tiempos = [] 

	

			Lista_Tiempos.append(Tiempo_Destino_Calle26)

			Lista_Tiempos.append(Tiempo_Destino_Heroes)

			Lista_Tiempos.append(Tiempo_Destino_Calle100)

			Lista_Tiempos.append(Tiempo_Destino_PortalNorte)



			Lista_Distancias.append(Distancia_Destino_Calle26)

			Lista_Distancias.append(Distancia_Destino_Heroes)

			Lista_Distancias.append(Distancia_Destino_Calle100)

			Lista_Distancias.append(Distancia_Destino_PortalNorte)

	

			C = list(zip(busB, Lista_Distancias))

			B = list(zip(busB, Lista_Tiempos))



			Lista_Estaciones_Cercanas_Destino_Tiempo = []

			Lista_Estaciones_Cercanas_Destino_Distancia = []



			for i in B:

				if i[1] == min(Lista_Tiempos):

					Lista_Estaciones_Cercanas_Destino_Tiempo.append(i)

					Lista_Tiempos.remove(i[1])

					B.remove(i)





			for x in B:

				if x[1] == min(Lista_Tiempos):

					Lista_Estaciones_Cercanas_Destino_Tiempo.append(x)

					Lista_Tiempos.remove(x[1])

					B.remove(x)





			for i in C:

				if i[1] == min(Lista_Distancias):

					Lista_Estaciones_Cercanas_Destino_Distancia.append(i)

					Lista_Distancias.remove(i[1])

					C.remove(i)





			for x in C:

				if x[1] == min(Lista_Distancias):

					Lista_Estaciones_Cercanas_Destino_Distancia.append(x)

					Lista_Distancias.remove(x[1])

					C.remove(x)



			for i in rutas:

				if i[0] == Lista_Estaciones_Cercanas_Destino_Tiempo[0][0]:

					Posicion_Posible_Destino_Nuevo1 = rutas.index(i)



				if i[0] == Lista_Estaciones_Cercanas_Destino_Tiempo[1][0]:

					Posicion_Posible_Destino_Nuevo2 = rutas.index(i)

		

				if i[0] == origen:

					Posicion_origen = rutas.index(i)

	



			if Posicion_Posible_Destino_Nuevo1 != Posicion_origen and Posicion_Posible_Destino_Nuevo2 != Posicion_origen:



				if Posicion_Posible_Destino_Nuevo1 < Posicion_origen:

					Ruta_Posible_Destino1 = list(rutas[ Posicion_Posible_Destino_Nuevo1 : Posicion_origen + 1])



				if Posicion_origen < Posicion_Posible_Destino_Nuevo1:

					Ruta_Posible_Destino1 = list(rutas[ Posicion_origen : Posicion_Posible_Destino_Nuevo1 + 1])



				if Posicion_Posible_Destino_Nuevo2 < Posicion_origen:

					Ruta_Posible_Destino2 = list(rutas[ Posicion_Posible_Destino_Nuevo2 : Posicion_origen + 1])



				if Posicion_origen < Posicion_Posible_Destino_Nuevo2:

					Ruta_Posible_Destino2 = list(rutas[ Posicion_origen : Posicion_Posible_Destino_Nuevo2 + 1])



		

				Coordenadas_Ruta_Destino_Posible1 = []

				Coordenadas_Ruta_Destino_Posible2 = []



				for i in Ruta_Posible_Destino1:

					for m in i[1]:

						Coordenadas_Ruta_Destino_Posible1.append(m)



				for i in Ruta_Posible_Destino2:

					for m in i[1]:

						Coordenadas_Ruta_Destino_Posible2.append(m)

			



				A4 = 0

				B4 = 1

				C4 = 2

				D4 = 3

				P4 = int(len(Coordenadas_Ruta_Destino_Posible1))

				M4 = (P4//2)-1

				K4 = 0

				R4 = 0

				TIEMPO4 = 30

				for i in range(M4):

					T4 = Haversine(float(Coordenadas_Ruta_Destino_Posible1[A4]),float(Coordenadas_Ruta_Destino_Posible1[B4]),float(Coordenadas_Ruta_Destino_Posible1[C4]),float(Coordenadas_Ruta_Destino_Posible1[D4]))

					A4 += 2

					B4 += 2

					C4 += 2

					D4 += 2

					K4 += T4

					Q4 = T4/velocidad

					R4 += Q4

					W4 = (Coordenadas_Ruta_Destino_Posible1[A4] , Coordenadas_Ruta_Destino_Posible1[B4])

					for i in Ruta_Posible_Destino1:

						if W4 == i[1]:

							if  i[0] in busB:

								TIEMPO4 += 45

	

				N4 = TIEMPO4/60

				S4 = R4*60

				Tiempo_Ruta_Destino_Posible1 = N4 + S4



				A5 = 0

				B5 = 1

				C5 = 2

				D5 = 3

				P5 = int(len(Coordenadas_Ruta_Destino_Posible2))

				M5 = (P5//2)-1

				K5 = 0

				R5 = 0

				TIEMPO5 = 30

				for i in range(M5):

					T5 = Haversine(float(Coordenadas_Ruta_Destino_Posible2[A5]),float(Coordenadas_Ruta_Destino_Posible2[B5]),float(Coordenadas_Ruta_Destino_Posible2[C5]),float(Coordenadas_Ruta_Destino_Posible2[D5]))

					A5 += 2

					B5 += 2

					C5 += 2

					D5 += 2

					K5 += T5

					Q5 = T5/velocidad

					R5 += Q5

					W5 = (Coordenadas_Ruta_Destino_Posible2[A5] , Coordenadas_Ruta_Destino_Posible2[B5])

					for i in Ruta_Posible_Destino2:

						if W5 == i[1]:

							if  i[0] in busB:

								TIEMPO5 += 45

	

				N5 = TIEMPO5/60

				S5 = R5*60

				Tiempo_Ruta_Destino_Posible2 = N5 + S5



				Tiempo_Total_Ruta_Destino_Nuevo1 = Tiempo_Ruta_Destino_Posible1 + float(Lista_Estaciones_Cercanas_Destino_Tiempo[0][1])

				Tiempo_Total_Ruta_Destino_Nuevo2 = Tiempo_Ruta_Destino_Posible2 + float(Lista_Estaciones_Cercanas_Destino_Tiempo[1][1])



			

			

				if Tiempo_Total_Ruta_Destino_Nuevo1 < Tiempo_Total_Ruta_Destino_Nuevo2:

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[0][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[0][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[0][1])



				else:

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[1][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[1][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[1][1])





			else:

			

				if (Posicion_Posible_Destino_Nuevo1 == Posicion_origen): 

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[1][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[1][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[1][1])

					



				if (Posicion_Posible_Destino_Nuevo2 == Posicion_origen):

					DestinoNuevo = Lista_Estaciones_Cercanas_Destino_Tiempo[0][0]

					Tiempo_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Tiempo[0][1])

					Distancia_DestinoNuevo_Destino = float(Lista_Estaciones_Cercanas_Destino_Distancia[0][1])

	

			Tiempo_Sumado_Por_Los_Transbordo = Tiempo_DestinoNuevo_Destino

			Distancia_Sumada_Por_Los_Transbordo =  Distancia_DestinoNuevo_Destino





			posicionOrigen = Lista_Rutas_Primer_Elemento.index(origen)

			posicionDestinoNuevo = Lista_Rutas_Primer_Elemento.index(DestinoNuevo)

		



			if posicionOrigen < posicionDestinoNuevo:

			

				for i in Lista_Rutas_Primer_Elemento:

					if i == origen:

						s = Lista_Rutas_Primer_Elemento.index(i)

				    

				for i in Lista_Rutas_Primer_Elemento:

					if i == DestinoNuevo:

						b = Lista_Rutas_Primer_Elemento.index(i)

				        

				ListaDeTuplas_Origen_Destino = list(rutas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])



				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)

							    



			if posicionDestinoNuevo < posicionOrigen:

		

				for i in rutasInversas:

					Lista_Rutas_Inversas_Primer_Elemento.append(i[0])



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == origen:

						s = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == DestinoNuevo:

						b = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				ListaDeTuplas_Origen_Destino = list(rutasInversas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])

				    

				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)

				

			print("Debe ir en el bus B hasta {0} y finalmente tomar el bus 8 hasta {1}, sin embargo puede que tomando el bus 8 el tiempo sea menor".format(DestinoNuevo, destino))



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------					



		if origen not in busB and destino in busB:

			amigos = []

			jiji = []

			jojo = []

			blabla = []

			mm = []

			



			

			for i in rutas:

				if i[0] == origen:

					PosicionOrigen = rutas.index(i)

				if i[0] == "Calle26":

					PosicionCalle26 = rutas.index(i)

				if i[0] == "Heroes":

					PosicionHeroes = rutas.index(i)

				if i[0] == "Calle100":

					PosicionCalle100 = rutas.index(i)

				if i[0] == "PortalNorte":

					PosicionPortalNorte = rutas.index(i)

			

			Ruta1 = list(rutas[ PosicionCalle26 : PosicionOrigen + 1])



			if PosicionOrigen < PosicionHeroes:

				Ruta2 = list(rutas[ PosicionOrigen : PosicionHeroes  + 1])



			if PosicionOrigen > PosicionHeroes:

				Ruta2 = list(rutas[ PosicionHeroes : PosicionOrigen + 1])



			if PosicionOrigen < PosicionCalle100:

				Ruta3 = list(rutas[ PosicionOrigen : PosicionCalle100  + 1])



			if PosicionOrigen > PosicionCalle100:

				Ruta3 = list(rutas[ PosicionCalle100 : PosicionOrigen + 1])



			if PosicionOrigen < PosicionPortalNorte:

				Ruta4 = list(rutas[ PosicionOrigen : PosicionPortalNorte  + 1])

		

			if PosicionOrigen > PosicionPortalNorte:

				Ruta4 = list(rutas[ PosicionPortalNorte : PosicionOrigen + 1])



			Coordenadas_Ruta1 = []

			Coordenadas_Ruta2 = []

			Coordenadas_Ruta3 = []

			Coordenadas_Ruta4 = []



			for i in Ruta1:

				for m in i[1]:

					Coordenadas_Ruta1.append(m)



			for i in Ruta2:

				for m in i[1]:

					Coordenadas_Ruta2.append(m)



			for i in Ruta3:

				for m in i[1]:

					Coordenadas_Ruta3.append(m)



			for i in Ruta4:

				for m in i[1]:

					Coordenadas_Ruta4.append(m)



			a = 0

			b = 1

			c = 2

			d = 3

			p = int(len(Coordenadas_Ruta1))

			m = (p//2)-1

			k = 0

			velocidad = 45

			r = 0

			tiempo = 30

			for i in range(m):

				t = Haversine(float(Coordenadas_Ruta1[a]),float(Coordenadas_Ruta1[b]),float(Coordenadas_Ruta1[c]),float(Coordenadas_Ruta1[d]))

				a += 2

				b += 2

				c += 2

				d += 2

				k += t

				q = t/velocidad

				r += q

				w = (Coordenadas_Ruta1[a] , Coordenadas_Ruta1[b])

				for i in Ruta1:

					if w == i[1]:

						if  i[0] in bus8:

							tiempo += 45

	

			n = tiempo/60

			s = r*60

			Tiempo_Origen_Calle26 = n + s

			Distancia_Origen_Calle26 = k

			

			

			

			a1 = 0

			b1 = 1

			c1 = 2

			d1 = 3

			p1 = int(len(Coordenadas_Ruta2))

			m1 = (p1//2)-1

			k1 = 0

			r1 = 0

			tiempo1 = 30

			for i in range(m1):

				t1 = Haversine(float(Coordenadas_Ruta2[a1]),float(Coordenadas_Ruta2[b1]),float(Coordenadas_Ruta2[c1]),float(Coordenadas_Ruta2[d1]))

				a1 += 2

				b1 += 2

				c1 += 2

				d1 += 2

				k1 += t1

				q1 = t1/velocidad

				r1 += q1

				w1 = (Coordenadas_Ruta2[a1] , Coordenadas_Ruta2[b1])

				for i in Ruta2:

					if w1 == i[1]:

						if  i[0] in bus8:

							tiempo1 += 45

	

			n1 = tiempo1/60

			s1 = r1*60

			Tiempo_Origen_Heroes = n1 + s1

			Distancia_Origen_Heroes = k1

			

			a2 = 0

			b2 = 1

			c2 = 2

			d2 = 3

			p2 = int(len(Coordenadas_Ruta3))

			m2 = (p2//2)-1

			k2 = 0

			r2 = 0

			tiempo2 = 30

			for i in range(m2):

				t2 = Haversine(float(Coordenadas_Ruta3[a2]),float(Coordenadas_Ruta3[b2]),float(Coordenadas_Ruta3[c2]),float(Coordenadas_Ruta3[d2]))

				a2 += 2

				b2 += 2

				c2 += 2

				d2 += 2

				k2 += t2

				q2 = t2/velocidad

				r2 += q2

				w2 = (Coordenadas_Ruta3[a2] , Coordenadas_Ruta3[b2])

				for i in Ruta3:

					if w2 == i[1]:

						if  i[0] in bus8:

							tiempo2 += 45

	

			n2 = tiempo2/60

			s2 = r2*60

			Tiempo_Origen_Calle100 = n2 + s2

			Distancia_Origen_Calle100 = k2



			a3 = 0

			b3 = 1

			c3 = 2

			d3 = 3

			p3 = int(len(Coordenadas_Ruta4))

			m3 = (p3//2)-1

			k3 = 0

			r3 = 0

			tiempo3 = 30

			for i in range(m3):

				t3 = Haversine(float(Coordenadas_Ruta4[a3]),float(Coordenadas_Ruta4[b3]),float(Coordenadas_Ruta4[c3]),float(Coordenadas_Ruta4[d3]))

				a3 += 2

				b3 += 2

				c3 += 2

				d3 += 2

				k3 += t3

				q3 = t3/velocidad

				r3 += q3

				w3 = (Coordenadas_Ruta4[a3] , Coordenadas_Ruta4[b3])

				for i in Ruta4:

					if w3 == i[1]:

						if  i[0] in bus8:

							tiempo3 += 45

	

			n3 = tiempo3/60

			s3 = r3*60

			Tiempo_Origen_PortalNorte = n3 + s3

			Distancia_Origen_PortalNorte = k3



			ddd = []

	

			jojo.append(Tiempo_Origen_Calle26)

			jojo.append(Tiempo_Origen_Heroes)

			jojo.append(Tiempo_Origen_Calle100)

			jojo.append(Tiempo_Origen_PortalNorte)



			ddd.append(Distancia_Origen_Calle26)

			ddd.append(Distancia_Origen_Heroes)

			ddd.append(Distancia_Origen_Calle100)

			ddd.append(Distancia_Origen_PortalNorte)

	

			c = list(zip(busB, ddd))

			b = list(zip(busB, jojo))



			Lista_Estaciones_Cercanas_Tiempo = []

			Lista_Estaciones_Cercanas_Distancia = []



			for i in b:

				if i[1] == min(jojo):

					Lista_Estaciones_Cercanas_Tiempo.append(i)

					jojo.remove(i[1])

					b.remove(i)





			for x in b:

				if x[1] == min(jojo):

					Lista_Estaciones_Cercanas_Tiempo.append(x)

					jojo.remove(x[1])

					b.remove(x)





			for i in c:

				if i[1] == min(ddd):

					Lista_Estaciones_Cercanas_Distancia.append(i)

					ddd.remove(i[1])

					c.remove(i)





			for x in c:

				if x[1] == min(ddd):

					Lista_Estaciones_Cercanas_Distancia.append(x)

					ddd.remove(x[1])

					c.remove(x)

	

			hhh = []

			kkk = []

			mmm = []



			for i in rutas:

				if destino == i[0]:

					hhh.append(i[1])



			for i in rutas:		

				for j in busB:

					if i[0] == j:

						hhh.append(i[1])



			for i in hhh:

				for m in i:

					kkk.append(m)

		

			C = 2

			D = 3

			J = int(len(kkk))

			M = (J//2)-1

			for i in range(M):

				Dist = Haversine(float(kkk[0]),float(kkk[1]),float(kkk[C]),float(kkk[D]))

				C += 2

				D += 2

				mmm.append(Dist) 

		

			Union = list(zip(busB, mmm))



			for i in Union:

				if i[1] == min(mmm):

					Estacion_Mas_Cercana_Al_Destino = str(i[0])

	

			for i in rutas:

				if i[0] == Lista_Estaciones_Cercanas_Tiempo[0][0]:

					Posicion_Posible_Origen_Nuevo1 = rutas.index(i)



				if i[0] == Lista_Estaciones_Cercanas_Tiempo[1][0]:

					Posicion_Posible_Origen_Nuevo2 = rutas.index(i)

		

				if i[0] == Estacion_Mas_Cercana_Al_Destino:

					Posicion_Estacion_Mas_Cercana_Al_Destino = rutas.index(i)



				

			if Posicion_Posible_Origen_Nuevo1 != Posicion_Estacion_Mas_Cercana_Al_Destino and Posicion_Posible_Origen_Nuevo2 != Posicion_Estacion_Mas_Cercana_Al_Destino:



				if Posicion_Posible_Origen_Nuevo1 < Posicion_Estacion_Mas_Cercana_Al_Destino:

					Ruta_Posible1 = list(rutas[ Posicion_Posible_Origen_Nuevo1 : Posicion_Estacion_Mas_Cercana_Al_Destino  + 1])



				if Posicion_Estacion_Mas_Cercana_Al_Destino < Posicion_Posible_Origen_Nuevo1:

					Ruta_Posible1 = list(rutas[ Posicion_Estacion_Mas_Cercana_Al_Destino : Posicion_Posible_Origen_Nuevo1  + 1])



				if Posicion_Posible_Origen_Nuevo2 < Posicion_Estacion_Mas_Cercana_Al_Destino:

					Ruta_Posible2 = list(rutas[ Posicion_Posible_Origen_Nuevo2 : Posicion_Estacion_Mas_Cercana_Al_Destino  + 1])



				if Posicion_Estacion_Mas_Cercana_Al_Destino < Posicion_Posible_Origen_Nuevo2:

					Ruta_Posible2 = list(rutas[ Posicion_Estacion_Mas_Cercana_Al_Destino : Posicion_Posible_Origen_Nuevo2 + 1])



				Coordenadas_Ruta_Posible1 = []

				Coordenadas_Ruta_Posible2 = []



				for i in Ruta_Posible1:

					for m in i[1]:

						Coordenadas_Ruta_Posible1.append(m)



				for i in Ruta_Posible2:

					for m in i[1]:

						Coordenadas_Ruta_Posible2.append(m)

			



				a4 = 0

				b4 = 1

				c4 = 2

				d4 = 3

				p4 = int(len(Coordenadas_Ruta_Posible1))

				m4 = (p4//2)-1

				k4 = 0

				r4 = 0

				tiempo4 = 30

				for i in range(m4):

					t4 = Haversine(float(Coordenadas_Ruta_Posible1[a4]),float(Coordenadas_Ruta_Posible1[b4]),float(Coordenadas_Ruta_Posible1[c4]),float(Coordenadas_Ruta_Posible1[d4]))

					a4 += 2

					b4 += 2

					c4 += 2

					d4 += 2

					k4 += t4

					q4 = t4/velocidad

					r4 += q4

					w4 = (Coordenadas_Ruta_Posible1[a4] , Coordenadas_Ruta_Posible1[b4])

					for i in Ruta_Posible1:

						if w4 == i[1]:

							if  i[0] in busB:

								tiempo4 += 45

	

				n4 = tiempo4/60

				s4 = r4*60

				Tiempo_Ruta_Posible1 = n4 + s4



				a5 = 0

				b5 = 1

				c5 = 2

				d5 = 3

				p5 = int(len(Coordenadas_Ruta_Posible2))

				m5 = (p5//2)-1

				k5 = 0

				r5 = 0

				tiempo5 = 30

				for i in range(m5):

					t5 = Haversine(float(Coordenadas_Ruta_Posible2[a5]),float(Coordenadas_Ruta_Posible2[b5]),float(Coordenadas_Ruta_Posible2[c5]),float(Coordenadas_Ruta_Posible2[d5]))

					a5 += 2

					b5 += 2

					c5 += 2

					d5 += 2

					k5 += t5

					q5 = t5/velocidad

					r5 += q5

					w5 = (Coordenadas_Ruta_Posible2[a5] , Coordenadas_Ruta_Posible2[b5])

					for i in Ruta_Posible2:

						if w5 == i[1]:

							if  i[0] in busB:

								tiempo5 += 45

	

				n5 = tiempo5/60

				s5 = r5*60

				Tiempo_Ruta_Posible2 = n5 + s5



				Tiempo_Total_Ruta_Origen_Nuevo1 = Tiempo_Ruta_Posible1 + float(Lista_Estaciones_Cercanas_Tiempo[0][1])

				Tiempo_Total_Ruta_Origen_Nuevo2 = Tiempo_Ruta_Posible2 + float(Lista_Estaciones_Cercanas_Tiempo[1][1])



			

			

			

		

				if Tiempo_Total_Ruta_Origen_Nuevo1 < Tiempo_Total_Ruta_Origen_Nuevo2:

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[0][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[0][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[0][1])



				else:

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[1][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[1][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[1][1])



			

			else: 

			

				if (Posicion_Posible_Origen_Nuevo1 == Posicion_Estacion_Mas_Cercana_Al_Destino): 

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[1][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[1][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[1][1])



				if (Posicion_Posible_Origen_Nuevo2 == Posicion_Estacion_Mas_Cercana_Al_Destino):

					origenNuevo = Lista_Estaciones_Cercanas_Tiempo[0][0]

					Tiempo_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Tiempo[0][1])

					Distancia_Origen_origenNuevo = float(Lista_Estaciones_Cercanas_Distancia[0][1])





			



			Tiempo_Sumado_Por_Los_Transbordo = Tiempo_Origen_origenNuevo 

			Distancia_Sumada_Por_Los_Transbordo = Distancia_Origen_origenNuevo 

		





			posicionOrigenNuevo = Lista_Rutas_Primer_Elemento.index(origenNuevo)

			posicionDestino = Lista_Rutas_Primer_Elemento.index(destino)





			if posicionOrigenNuevo < posicionDestino:

			

				for i in Lista_Rutas_Primer_Elemento:

					if i == origenNuevo:

						s = Lista_Rutas_Primer_Elemento.index(i)

				    

				for i in Lista_Rutas_Primer_Elemento:

					if i == destino:

						b = Lista_Rutas_Primer_Elemento.index(i)

				        

				ListaDeTuplas_Origen_Destino = list(rutas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])



				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)

							    



			if posicionDestino < posicionOrigenNuevo:

		

				for i in rutasInversas:

					Lista_Rutas_Inversas_Primer_Elemento.append(i[0])



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == origenNuevo:

						s = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				for i in Lista_Rutas_Inversas_Primer_Elemento:

					if i == destino:

						b = Lista_Rutas_Inversas_Primer_Elemento.index(i)



				ListaDeTuplas_Origen_Destino = list(rutasInversas[s:b+1])

				

				for i in ListaDeTuplas_Origen_Destino:

					Tupla_Coordenadas_Estaciones.append(i[1])

				    

				for i in Tupla_Coordenadas_Estaciones:

					for z in i:

						Lista_Coordenadas_Estaciones.append(z)

			

			print("Debe ir en el bus 8 hasta {0} y finalmente tomar el bus B hasta {1}, sin embargo puede que tomando el bus 8 el tiempo sea menor".format(origenNuevo, destino))

			




	a = 0

	b = 1

	c = 2

	d = 3

	p = int(len(Lista_Coordenadas_Estaciones))

	m = (p//2)-1

	k = 0

	velocidad = 45

	r = 0

	tiempo = 30

	

	for i in range(m):

		t = Haversine(float(Lista_Coordenadas_Estaciones[a]),float(Lista_Coordenadas_Estaciones[b]),float(Lista_Coordenadas_Estaciones[c]),float(Lista_Coordenadas_Estaciones[d]))

		a += 2

		b += 2

		c += 2

		d += 2

		k += t

		p = t/velocidad

		r += p

		w = (Lista_Coordenadas_Estaciones[a] , Lista_Coordenadas_Estaciones[b])

		for i in ListaDeTuplas_Origen_Destino:

			if w == i[1]:

				for j in Buses_Guillermo_Ramirez:

					if bus == j[0]:                  

						if i[0] in j[1]:

							tiempo +=45

	

	

	n = tiempo/60

	s = r*60

	tiempoFinal = n + s

	Tiempo_De_Transcurso_Total = Tiempo_Sumado_Por_Los_Transbordo + tiempoFinal

	Distancia_Total_De_Recorrido = Distancia_Sumada_Por_Los_Transbordo + k

	print("La distancia a recorrer es {0:.2f} km y el tiempo aproximado es {1: .2f} minutos".format(Distancia_Total_De_Recorrido, Tiempo_De_Transcurso_Total))

	

		

Prueba()

