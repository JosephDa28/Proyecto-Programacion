
from math import *
#Tupla con nombres de las estaciones y sus respectivas coordenadas geograficas
rutas = (("Calle26", (4.617126, -74.071939)), ("Profamilia", (4.621319, -74.069789)), ("Avenida39", (4.627178, -74.068641)), ("Calle45", (4.632655, -74.067666)), ("Marly", (4.636969, -74.066865)), ("Calle57", (4.643053, -74.065801)), ("Calle63", (4.649191, -74.064731)), ("Flores", (4.654843, -74.063077)), ("Calle72", (4.658098, -74.062120)), ("Calle76", (4.663326, -74.061221)), ("Heroes", (4.668309, -74.060212)), ("Calle85", (4.671860, -74.059724)), ("Virrey", (4.676202, -74.058983)), ("Calle100", (4.685606, -74.057353)), ("Calle106", (4.692131, -74.056339)), ("PepeSierra", (4.698403, -74.055299)), ("Calle127", (4.705319, -74.054134)), ("Prado", (4.714349, -74.052605)), ("Alcala", (4.720781, -74.051531)), ("Calle142", (4.726377, -74.050614)), ("Calle146", (4.731601, -74.049726)), ("Mazuren", (4.734492, -74.049245)), ("CardioInfantil", (4.742144, -74.047965)), ("Toberin", (4.746806, -74.047176)), ("PortalNorte", (4.754229, -74.046133)), ("Calle187", (4.763601, -74.044363)), ("Terminal", (4.768818, -74.043506)))
#Tupla con nombres de las estaciones y sus respectivas coordenadas geograficas pero al reves
rutasInversas =  (("Terminal", (4.768818, -74.043506)), ("Calle187", (4.763601, -74.044363)), ("PortalNorte", (4.754229, -74.046133)), ("Toberin", (4.746806, -74.047176)), ("CardioInfantil", (4.742144, -74.047965)), ("Mazuren", (4.734492, -74.049245)), ("Calle146", (4.731601, -74.049726)), ("Calle142", (4.726377, -74.050614)), ("Alcala", (4.720781, -74.051531)), ("Prado", (4.714349, -74.052605)), ("Calle127", (4.705319, -74.054134)), ("PepeSierra", (4.698403, -74.055299)), ("Calle106", (4.692131, -74.056339)), ("Calle100", (4.685606, -74.057353)), ("Virrey", (4.676202, -74.058983)), ("Calle85", (4.671860, -74.059724)), ("Heroes", (4.668309, -74.060212)), ("Calle76", (4.663326, -74.061221)), ("Calle72", (4.658098, -74.062120)), ("Flores", (4.654843, -74.063077)), ("Calle63", (4.649191, -74.064731)), ("Calle57", (4.643053, -74.065801)), ("Marly", (4.636969, -74.066865)), ("Calle45", (4.632655, -74.067666)), ("Avenida39", (4.627178, -74.068641)), ("Profamilia", (4.621319, -74.069789)), ("Calle26", (4.617126, -74.071939)))
#Tupla con nombres de los buses y sus respectivas paradas
Buses = (("bus8", {"Calle26":"Vagon1", "Profamilia":"Vagon2", "Avenida39":"Vagon1", "Calle45":"Vagon2", "Marly":"Vagon2", "Calle57":"Vagon3", "Calle63":"Vagon1", "Flores":"Vagon1", "Calle72":"Vagon3", "Calle76":"Vagon2", "Heroes":"Vagon2", "Calle85":"Vagon2", "Virrey":"Vagon2", "Calle100":"Vagon1", "Calle106":"Vagon1", "PepeSierra":"Vagon1", "Calle127":"Vagon1", "Prado":"Vagon2", "Alcala":"Vagon2", "Calle142":"Vagon1", "Calle146":"Vagon1", "Mazuren":"Vagon1", "CardioInfantil":"Vagon2", "Toberin":"Vagon2", "PortalNorte":"Vagon0", "Calle187":"Vagon1", "Terminal":"Vagon1"}),("busB74", {"Avenida39":"Vagon0", "Calle57":"Vagon0" , "Calle72":"Vagon0", "Calle76":"Vagon0", "Heroes":"Vagon0", "Virrey":"Vagon0", "Calle100":"Vagon3", "Prado":"Vagon0", "Calle142":"Vagon0", "Toberin":"Vagon0", "PortalNorte":"Vagon0"}), ("busB27",{"Marly":"Vagon1", "Calle72":"Vagon2", "Calle76":"Vagon1", "Calle85":"Vagon3", "Virrey":"Vagon1", "PortalNorte":"Vagon0"}), ("busB75",{"Marly":"Vagon1", "Calle63":"Vagon2", "Calle72":"Vagon3", "Calle76":"Vagon3", "Heroes":"Vagon3", "Calle100":"Vagon2", "Calle127":"Vagon2", "Prado":"Vagon2", "Alcala":"Vagon2", "Calle142":"Vagon2", "Calle146":"Vagon2", "Toberin":"Vagon1", "PortalNorte":"Vagon0"}), ("busB12",{"Calle100":"Vagon1", "Calle127":"Vagon1", "Prado":"Vagon3", "Calle142":"Vagon1", "Toberin":"Vagon3", "PortalNorte":"Vagon0"}), ("busB13", {"Avenida39":"Vagon1", "Calle63":"Vagon2", "Flores":"Vagon1", "Calle85":"Vagon1", "Calle100":"Vagon1", "Calle106":"Vagon1", "Calle142":"Vagon1", "Mazuren":"Vagon2", "CardioInfantil":"Vagon2", "PortalNorte":"Vagon0"}), ("busB14", {"Calle26":"Vagon1", "Profamilia":"Vagon1", "Calle45":"Vagon1", "Marly":"Vagon1", "Heroes":"Vagon1", "Callee85":"Vagon1", "Calle100":"Vagon3", "Calle127":"Vagon2", "Alcala":"Vagon2", "Calle146":"Vagon3", "PortalNorte":"Vagon0"}), ("busB18", {"Profamilia":"Vagon1", "Calle45":"Vagon1", "Calle57":"Vagon1", "Calle63":"Vagon2", "Virrey":"Vagon2", "PepeSierra":"Vagon2", "Calle127":"Vagon2", "Alcala":"Vagon1", "Calle187":"Vagon1", "Terminal":"Vagon1"}), ("busD24", {"Calle26":"Vagon3", "Avenida39":"Vagon3", "Calle57":"Vagon2"}), ("busD20", {"Calle26":"Vagon3", "Profamilia":"Vagon2", "Calle45":"Vagon2"}), ("bus6", {"Calle26":"Vagon2", "Profamilia":"Vagon2", "Avenida39":"Vagon1", "Calle45":"Vagon2", "Marly":"Vagon2", "Calle57":"Vagon2", "Calle63":"Vagon3", "Flores":"Vagon2", "Calle72":"Vagon1", "Calle76":"Vagon2"}))


def Haversine (lat1,lon1,lat2,lon2):
	rad = pi/180
	dlat = lat2 - lat1
	dlon = lon2 - lon1
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
   
	
    
	while True:
		print("Escriba su estacion de origen todo en pegado y con la primera en mayuscula")
		
		origen = (str(input("Escriba su estacion de origen: ")))	
		
		if origen in Lista_Rutas_Primer_Elemento:
				break
	
	
	while True:
		print("Escriba su estacion de destino todo en pegado y con la primera en mayuscula")
		
		destino = (str(input("Escriba su estacino de destino: ")))
		
		if destino in Lista_Rutas_Primer_Elemento:
				break
	 
	
	for i in Buses:
		if origen in i[1] and destino in i[1]:
			Lista_De_Error1.append(i[0])

	print("Si desea tomar una ruta directa desde su origen y destino le recomendamos los siguientes buses: {0}".format(Lista_De_Error1))

	for i in Buses:
		if origen in i[1]:
			lista.append(i[0])


	for i in Buses:
		Lista_De_Error.append(i[0])


	while True:
		bus = (str(input("Escriba el bus que desea tomar: ")))
		if bus not in Lista_De_Error:
			print("Escriba el bus que desea tomar como se muestra en este ejemplo; busB75") 

		if bus not in lista and bus in Lista_De_Error:
			print("Este bus no tiene como parada el origen puesto, recuerde que puede tomar alguno de los siguientes buses {0}".format(lista))
	
		if bus in Lista_De_Error and bus in lista:
			break
		   
	for i in Buses:
		if bus == i[0]:
			for z in Buses:
				for t in z[1]:
					for m in i[1]:
						if m == t:
							if i[1][m]==z[1][t]:
								ParadasEnComun.append(m)

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
                                
	a = 0
	b = 1
	c = 2
	d = 3
	p = int(len(Lista_Coordenadas_Estaciones))
	m = (p//2)-1
	k = 0
	velocidad = 45
	r = 0

    
	if ParadasEnComun.count(origen) == 1:
		tiempo = 45
	elif ParadasEnComun.count(origen) == 2:
		tiempo = 60
	elif ParadasEnComun.count(origen) == 3:
		tiempo = 70
	elif ParadasEnComun.count(origen) == 4:
		tiempo = 100
	elif ParadasEnComun.count(origen) == 5:
		tiempo =110
	elif ParadasEnComun.count(origen) == 6:
		tiempo = 120
	elif ParadasEnComun.count(origen) == 7:
		tiempo = 130
	elif ParadasEnComun.count(origen) == 8:
		tiempo = 140
	else:
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
				for j in Buses:
					if bus == j[0]:                  
						if i[0] in j[1]:
							if ParadasEnComun.count(i[0]) == 1:
								tiempo += 45
							elif ParadasEnComun.count(i[0]) == 2:
								tiempo += 60
							elif ParadasEnComun.count(i[0]) == 3:
								tiempo +=70
							elif ParadasEnComun.count(i[0]) == 4:
								tiempo += 100
							elif ParadasEnComun.count(i[0]) == 5:
								tiempo +=110
							elif ParadasEnComun.count(i[0]) == 6:
								tiempo += 120
							elif ParadasEnComun.count(i[0]) == 7:
								tiempo += 130
							elif ParadasEnComun.count(i[0]) == 8:
								tiempo += 140
							else:
								tiempo += 30


	n = tiempo/60
	s = r*60
	tiempoTotal = n + s
	print("La distancia a recorrer es {0} y el tiempo aproximado es {1} minutos".format(k, int(tiempoTotal)))
	


Prueba()

                      
                


               
                    

    
                
        
    






