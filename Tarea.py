while True:

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    meme_dict = {
                "CRINGE": "cuando te da pena agena",
                "LOL": "'Laugh Out Loud', Que en español es 'Riete Fuerte'o 'Risa Fuerte'",
                "XD": "si lo volteas es una carita riendose",
                "RANDOM": "algo aleatorio, al azar o inesperado", 
                "CRUSH": "para referirte a una persona que te gusta mucho",
                "PVP": "un duelo entre un jugador y otro"
                }
                
    if word in meme_dict.keys():
        print("El significado de", word, "es", meme_dict[word])
    else:
        print("No encontre", word, "en mi diccionario, creo que debes buscarla en internet")
