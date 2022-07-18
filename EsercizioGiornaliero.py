def perimetro():
	print("Il programma calcola il perimetro di una figura geometrica")
	print("""
	-Quadrato>>1
	-Rettangolo >>2
	-Cerchio>>3
	-Triangolo>>4""")
#Quelli con l'asterisco sono con l'uso di float e mentre quelli senza sono con l'uso del eval
	print("Inserire la scelta: ")	#qui inizierà il gioco e dovrai fare la scelta
	scelta = int(input(">>> "))
	if scelta == 1:	#Scegliere 1-2-3-4 e poi usciranno le varie opzioni possibilii
               print("Hai selezionato il perimetro del quadrato")
               lato = eval(input("Inserisci il valore del lato del quadrato"))
               print("Il perimetro del quadrato, avente lato", lato, "è:" , lato +4)

#	if scelta == 1:
#		print("Hai selezionato il perimetro del quadrato")
#		lato = float(input("Inserisci il valore del lato del quadrato"))
#		print("Il perimetro del quadrato, avente lato", lato, "è:" , lato +4)

	elif scelta == 2:
		print("inserisci di seguito i dati che ti vengono richiesti:\n\n")
		Base=eval(input("inserire il valore della base:"))
		Altezza=eval(input("inserire il valore dell altezza"))
		print("il valore dell area è;", Base*Altezza)

#	elif scelta == 2:
#		print("Hai selezionato il perimetro del rettangolo")
#		base = float(input("Inserisci il valore del lato del rettangolo"))
#		altezza = float(input("Inserisci il valore dell'altezza"))
#		print("Il perimetro del rettangolo, avente base", base, "e altezza" ,altezza, "è: ", base*2 + 2*altezza)
	elif scelta == 3:
		print("Hai selezionato il perimetro del cerchio")
		diametro=eval(input("Inserisci il diametro del cerchio:"))
		print("Il perimetro del cerchio, avente diametro ",diametro, "e: ", 3.14 *diametro)

#	elif scelta == 3:
#		print("Hai selezionato il perimetro del cerchio")
#		diametro = float(input("Inserisci il diametro del cerchio:"))
#		print("Il perimetro del erchio ,avente diametro ", diametro, "e: " ,3.14 *diametro)
	elif scelta == 4: #Qui ho deciso di spingermi un po' oltre e rendere più divertente il gioco e qui una volta messi i vari parametri ti dirà la tipologia del triangolo
		print("Calcola perimetro di un triangolo e scopri la tipologia")
		lato1=eval(input("inserisci primo lato: "))
		lato2=eval(input("inserisci secondo lato: "))
		lato3=eval(input("inserisci terzo lato: "))
	if lato1<lato2+lato3 and lato2<lato1+lato3 and lato3<lato1+lato2:
        	if lato1==lato2 and lato2==lato3:
                	print("il triangolo è equilatero")
        	elif lato1==lato2 or lato2==lato3 or lato3==lato1:
                	print("Il triangolo è isoscele")
        	else:
                	print("il triangolo è scaleno")
	else:
		print("Inserire una scelta valida")
perimetro();
